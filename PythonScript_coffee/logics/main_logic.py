from devices.barcode_reader import BarcodeArgs
from events.worker import Worker
from Config import *
from events.scheduler import Job, Scheduler
from events.event_args import EventArgs
from logics.recipe.americano import is_using_milk
from .recipe.event_args import *
from devices.cup_disp import CupDispenser
from devices.ice_disp import IceDispenser
from devices.kiosk import Coffee, Kiosk, KioskEventArgs
from logging import FileHandler, Logger, StreamHandler
from logging.handlers import RotatingFileHandler
import events, logging
from context import Context
from enum import Enum, auto
from queue import Queue, PriorityQueue
from . import recipe
from datetime import datetime as dt, timedelta
import time
from . import mail
import os
import os.path
from fcntl import ioctl


test_mode = False

class LogicState(Enum):
    IDLE                = auto()
    PREPARE             = auto()
    PREPARE_DONE        = auto()
    RECIPE              = auto()
    RECIPE_DONE         = auto()
    LIFT                = auto()
    CLEAN               = auto()
    TRASH               = auto()
    WAIT                = auto()

_context: Context = None
_scheduler: Scheduler = None
_dev_kiosk: Kiosk = None
_dev_ice: IceDispenser = None
_dev_cup: CupDispenser = None

_job_list = PriorityQueue()

_order_list = Queue()
_cm_slot = {}
for i in range(2): _cm_slot[i] = None
_lift_slot = {}
_lift_usage = {}
_lift_delay = {}
_lift_exists = {}
_lift_exists_delay = {}
_lift_di_check = {}
_lift_error_flag = {}
_lift_delay_timer = {} #for checking error detection
for i in range(3):
    _lift_slot[i] = None
    _lift_usage[i] = False
    _lift_delay[i] = 0
    _lift_exists[i] = False
    _lift_exists_delay[i] = 0
    _lift_di_check[i] = 0
    _lift_error_flag[i] = 0
    _lift_delay_timer[i] = 0 #for checking error detection
#_lift_slot[0] = 1 # Not used lift slot
_state: LogicState = LogicState.IDLE
_job_refresh_milk: Job = None
_job_wait_pos: Job = None
_job_mailing: Job = None
_coffee_logger: Logger = None
_coffee_logger_fh: FileHandler = None
_coffee_logger_sh: StreamHandler = None

def _create_logger(name, path, log_size=(1 * 1024 * 1024), log_backup_count=10):
    global _coffee_logger, _coffee_logger_fh, _coffee_logger_sh
    _coffee_logger = logging.getLogger(name)
    _coffee_logger_fh = RotatingFileHandler(path, log_size, log_backup_count)
    formatter = logging.Formatter('[%(levelname)s | %(filename)s:%(lineno)s]\t%(asctime)s\t> %(message)s')
    _coffee_logger_sh = logging.StreamHandler()
    _coffee_logger_fh.setFormatter(formatter)
    _coffee_logger_sh.setFormatter(formatter)
    _coffee_logger.addHandler(_coffee_logger_fh)
    _coffee_logger.addHandler(_coffee_logger_sh)
    _coffee_logger.setLevel(logging.DEBUG)

def _dispose_logger():
    global _coffee_logger, _coffee_logger_fh, _coffee_logger_sh
    if _coffee_logger is not None:
        _coffee_logger.removeHandler(_coffee_logger_fh)
        _coffee_logger.removeHandler(_coffee_logger_sh)
        del _coffee_logger, _coffee_logger_fh, _coffee_logger_sh

def init(context: Context) -> None:
    global _context, _scheduler, _dev_kiosk, _dev_ice, _dev_cup, _job_refresh_milk, _job_mailing, _coffee_logger, _job_wait_pos
    _context = context
    _dev_kiosk = _context.get_device_by_name(Kiosk.get_device_name())
    _dev_ice = _context.get_device_by_name(IceDispenser.get_device_name())
    _dev_cup = _context.get_device_by_name(CupDispenser.get_device_name())

    _job_refresh_milk = Job(None, RefreshMilkArgs(0, None), context.get_config()[CONFIG_KEY_MILK_REFRESH_DURATION], True)
    _job_mailing = Job(None, MailingArgs(0, None), 600, True)
    _job_wait_pos = Job(None, WaitPosArgs(0,None))

    _create_logger("CoffeeOrder", f"{_context.get_root_path()}/order.log")

    _context.get_worker().add_co_routine(co_routine)
    _context.get_worker().set_coroutine_interval((1.0 / 30.0))

    _scheduler = _context.get_scheduler()\
        .add_event_listener(KioskEventArgs, on_kiosk_listener)\
        .add_event_listener(BarcodeArgs, on_barcode_listener)\
        .add_event_listener(recipe.CoffeeRecipeDoneEventArgs, on_coffee_done)\
        .add_event_listener(PreparedDoneArgs,on_preapre_done)\
        .add_event_listener(RefreshMilkArgs, on_refresh_milk)\
        .add_event_listener(WaitPosArgs, on_wait_pos)\
        .add_event_listener(MailingArgs, on_mailing)\
        .add_schedule(_job_refresh_milk)\
        .add_schedule(_job_mailing)

def dispose():
    if _context is not None:
        _context.get_worker().remove_co_routine(co_routine)
    if _scheduler is not None:
        _scheduler.remove_event_listener(on_kiosk_listener)
    _dispose_logger()

def co_routine(worker: Worker, deltatime: timedelta, logger: Logger):
    shm = _context.acquire_shm()
    di_list = shm.get_di()
    if not di_list[INDY_DI_ADDR_BTN_RUN_STATE] and _state == LogicState.IDLE:
        logger.warning("Stop button pushed. Requesting stop entire program from the co-routine in the main logic process.")
        _context.release_shm()
        worker.stop(0)
        return
    elif di_list[INDY_DI_ADDR_BTN_RESET] or shm.get_robot_status()['emergency']:
        logger.error("Reset button pushed. Requesting stop entire program from the co-routine in the main logic process.")
        if _state != LogicState.IDLE and not shm.get_robot_status()['emergency']:
            shm.stop_emergency()
            logger.error("Robot state was changed with Emergency because the logic state is not IDEL state.")
        _context.release_shm()
        worker.stop(0)
        return
    
    di_lift_up_addresses = [x for x in
        range(INDY_DI_ADDR_LIFT1_STATE_UP, INDY_DI_ADDR_LIFT3_STATE_DOWN  + 1)
        if (x - INDY_DI_ADDR_LIFT1_STATE_UP) % 2 == 0]
    di_lift_down_addresses = [x for x in
        range(INDY_DI_ADDR_LIFT1_STATE_UP, INDY_DI_ADDR_LIFT3_STATE_DOWN  + 1)
        if (x - INDY_DI_ADDR_LIFT1_STATE_UP) % 2 == 1]
    do_lift_up_addresses = [x for x in
        range(INDY_DO_ADDR_LIFT1_UP, INDY_DO_ADDR_LIFT3_DOWN  + 1)
        if (x - INDY_DO_ADDR_LIFT1_UP) % 2 == 0]
    do_lift_down_addresses = [x for x in
        range(INDY_DO_ADDR_LIFT1_UP, INDY_DO_ADDR_LIFT3_DOWN  + 1)
        if (x - INDY_DO_ADDR_LIFT1_UP) % 2 == 1]
    di_lift_cup_exists_addresses = [x for x in
        range(INDY_DI_ADDR_LIFT1_CUP_EXISTS, INDY_DI_ADDR_LIFT3_CUP_EXISTS  + 1)]
    
    hand_detected = not di_list[INDY_DI_ADDR_HAND_PROTECTION]
    lift_delay_time = float(_context.get_config()[CONFIG_KEY_LIFT_DELAY])
    lift_cup_delay_time = float(_context.get_config()[CONFIG_KEY_LIFT_CUP_DELAY])
    
    for idx in _lift_usage.keys():
        addr_di_lift_up = di_lift_up_addresses[idx]
        addr_di_lift_down = di_lift_down_addresses[idx]
        di_up_state = di_list[addr_di_lift_up]
        di_down_state = di_list[addr_di_lift_down]
        addr_do_lift_up = do_lift_up_addresses[idx]
        addr_do_lift_down = do_lift_down_addresses[idx]
        cup_exists = di_list[di_lift_cup_exists_addresses[idx]]
        prev_cup_exists = _lift_exists[idx]

        if (int(_lift_di_check[idx]) !=  int(di_list[di_lift_cup_exists_addresses[idx]])):
            logger.info(f"di idx {di_lift_cup_exists_addresses[idx]} : {di_list[di_lift_cup_exists_addresses[idx]]    }")
            if _lift_di_check[idx] == 0:
                _lift_di_check[idx] = 1
            else:
                _lift_di_check[idx] = 0

        if not cup_exists:
            if prev_cup_exists:
                _lift_exists_delay[idx] += deltatime.total_seconds()
                logger.info(f"lift delay idx: {_lift_exists_delay[idx]}")
                if _lift_exists_delay[idx] > lift_cup_delay_time:
                    _lift_exists_delay[idx] = 0
                    _lift_exists[idx] = False
                else:
                    cup_exists = True
        else:
            _lift_exists_delay[idx] = 0
            _lift_exists[idx] = True

        is_coffee_slot = _lift_slot[idx] is not None and isinstance(_lift_slot[idx], Coffee)
        is_expired_coffee = is_coffee_slot and _lift_slot[idx].is_expired()
        #if is_coffee_slot:
        #    logger.info(f"di idx {di_lift_cup_exists_addresses[idx]} : {di_list[di_lift_cup_exists_addresses[idx]]}")

        if _lift_usage[idx]:
            if not di_down_state:
                shm.set_do(addr_do_lift_down, True)
                shm.set_do(addr_do_lift_up, False)
                lift_down_timerStart = 1 
            elif di_down_state and not cup_exists and not hand_detected: 
                # start delay timer at initial point
                # wait for lift_delay_timer 
                # if timer expires, set that coffee to gotta expired coffee
                # if expired, let lift_usage[idx] = False and exit this block
                if lift_down_timerStart == 1:
                    # start timer
                    _lift_delay_timer[idx] = 0
                    lift_down_timerStart = 0
                
                # timer += total_seconds
                if _lift_delay_timer[idx] > 10:
                # if timer > 10 -> expire !!!
                    is_exception = 1 # notify
                    _lift_usage[idx] = False
                else:
                    _lift_delay_timer[idx] += deltatime.total_seconds()
                
                    
            elif not hand_detected and (not cup_exists or is_expired_coffee):
                is_exception = 0
                _lift_usage[idx] = False
                coffee: Coffee = _lift_slot[idx]
                if not cup_exists:
                    logger.info(f"Removed cup by customer. Index: {idx}")
                    _coffee_logger.info(f"Removed cup by customer. lift_index: {idx}, PE_ID: {coffee.get_order_data().PE_ID}, menu: {coffee._menu.name}")
                else: # elif is_expired_coffee:
                    logger.info(f"Removed cup by expired time. Index: {idx}")
                    _coffee_logger.info(f"Expired Coffee. lift_index: {idx}, PE_ID: {coffee.get_order_data().PE_ID}, menu: {coffee._menu.name}")
                coffee.finish()
        else:
            if not di_up_state: 
                if hand_detected: 
                    _lift_delay[idx] = 0 
                    shm.set_do(addr_do_lift_down, True)
                    shm.set_do(addr_do_lift_up, False)
                    #_lift_error_flag[idx] = 0 # no error if no hand detection 
                    # 정상상태
                elif (not cup_exists or is_expired_coffee) and (not is_exception): # if is_exception should not come here
                    #_lift_error_flag[idx] = 1 
                    if _lift_delay[idx] > lift_delay_time:
                        shm.set_do(addr_do_lift_down, False)
                        shm.set_do(addr_do_lift_up, True) 
                    else:
                        _lift_delay[idx] += deltatime.total_seconds()
            elif is_coffee_slot and (not cup_exists or is_expired_coffee) or is_exception:
                # process exception
                if is_exception:
                    if not di_up_state:
                        shm.set_do(addr_do_lift_down,False)
                        shm.set_do(addr_do_lift_up, True)
                        lift_exception = 1
                        
                if lift_exception == 1:
                    is_expired_coffee = 1

                _lift_delay[idx] = 0
                _lift_delay_timer[idx] = 0
                coffee: Coffee = _lift_slot[idx]
                order_data: Kiosk.OrderData = coffee.get_order_data()
                
                if is_expired_coffee:
                    if not coffee.is_junk():
                        coffee.set_junk()
                        coffee.finish()
                        logger.debug(f"Job appending - TRASH : lift_index: {idx}, expired: {is_expired_coffee}, menu: {coffee._menu.name}")
                        _job_list.put(JOB_PRIORITY_TRASH)
                    
                if coffee.is_finished():
                    logger.debug(f"Removing Coffee confirmed : lift_index: {idx}, PE_ID: {coffee.get_order_data().PE_ID}, menu: {coffee._menu.name}")
                    _coffee_logger.info(f"Coffee was removed successfully. lift_index: {idx}, PE_ID: {coffee.get_order_data().PE_ID}, menu: {coffee._menu.name}")
                    coffee.dispose()
                    _lift_slot[idx] = None
                try:
                    if order_data.OJ_STATUS == Kiosk.OrderData.ORDER_DATA_STATE_DONE and not cup_exists:
                        if order_data.get_remaining_coffee_count() == 0:
                            logger.info(f"State changed [{order_data.OJ_STATUS}] -> [{Kiosk.OrderData.ORDER_DATA_STATE_REMOVED}], lift_index: {idx}, PE_ID: {coffee.get_order_data().PE_ID}, menu: {coffee._menu.name}")
                            _dev_kiosk.update_order_state(order_data, Kiosk.OrderData.ORDER_DATA_STATE_REMOVED)
                        else:
                            logger.info(f"State changed [{order_data.OJ_STATUS}] -> [{Kiosk.OrderData.ORDER_DATA_STATE_PREPARE}], lift_index: {idx}, PE_ID: {coffee.get_order_data().PE_ID}, menu: {coffee._menu.name}")
                            _dev_kiosk.update_order_state(order_data, Kiosk.OrderData.ORDER_DATA_STATE_PREPARE)
                except:
                    logger.exception("Got exception on DB_UPDATE")

                           

    _context.release_shm()

def main_loop(worker: events.Worker, deltatime, logger: Logger) -> bool or None:
    global _state

    path_USB0 = '/dev/ICEDISP'
    if os.path.exists(path_USB0):
        USB0_connect = 1
    else:
        USB0_connect = 0
        logger.info("ICEDISP connect failed")
    if USB0_connect == 0:
        # implement USB hub reset
        # first get USB hub's Bus #num and Device #num 
        stream = os.popen('lsusb').read()
        vendor_name = '2817' #Realtek Semiconductor Corp
        idx_vendor_name = stream.find(vendor_name) 
        BUS_num = '/'+stream[idx_vendor_name-24:idx_vendor_name-21]+'/'
        DEVICE_num = stream[idx_vendor_name - 13:idx_vendor_name - 10]
                 #cmd = 'sudo ./usbreset /dev/bus/usb' + BUS_num + DEVICE_num 
                 #------------------------finding Bus num, Device num complete
                 #os.system('chmod +x usbreset') # make program executable
        reset_error = reset_usb(BUS_num,DEVICE_num)
        if(reset_error):
            logger.info('USB reset failure!!')
            return
                         #exit? or not? 
                     # if successful, Reset Successful! on terminal console

    if _state == LogicState.IDLE:
        if _job_list.empty():
            _scheduler.add_schedule(_job_wait_pos)
            return
        job = _job_list.get()

        if job == JOB_PRIORITY_ORDER_CHECK:
            if not _order_list.empty():
                cm_idx = -1
                for idx in _cm_slot.keys():
                    if _cm_slot[idx] is None:
                        cm_idx = idx
                        break
                
                lift_idx = -1
                for idx in _lift_slot.keys():
                    if _lift_slot[idx] is None:
                        lift_idx = idx
                        break
                if cm_idx < 0 or lift_idx < 0:
                    _job_list.put(job)
                    return

                _state = LogicState.PREPARE
                logger.info(f"Logic job retrieved <{_state}>.")
                coffee: Coffee = _order_list.get()
                coffee.set_cm_index(cm_idx)
                _cm_slot[cm_idx] = coffee
                _lift_slot[lift_idx] = True
                _scheduler.add_schedule(Job(None, MainEventArgs(MainEventArgs.EVENT_CODE_NEW_COFFEE, coffee)))
            else:
                _job_list.put(job)
                return
        elif job == JOB_PRIORITY_LIFT:
            _state = LogicState.LIFT
            logger.info(f"Logic job retrieved <{_state}>.")

        elif job == JOB_PRIORITY_CLEAN:
            _state = LogicState.CLEAN
            logger.info(f"Logic job retrieved <{_state}>.")

        elif job == JOB_PRIORITY_TRASH:
            _state = LogicState.TRASH
            logger.info(f"Logic job retrieved <{_state}>.")
        
        # elif job == JOB_PRIORITY_REFRESH_MILK:
        #     logger.info(f"Milk refreshing...")
        #     shm = _context.acquire_shm()
        #     shm.write_direct_variable('B', INDY_ADDR_COMMAND, INDY_CMD_REFRESH_MILK)
        #     while shm.read_direct_variable('B', INDY_ADDR_COMMAND) != INDY_CMD_IDLE and not worker.is_stopping():
        #         _context.release_shm()
        #         time.sleep(0.5)
        #         shm = _context.acquire_shm()
        #     _context.release_shm()
        #     logger.info(f"Milk refreshing...Done.")
        
        elif job == JOB_PRIORITY_WAIT_POS:
            _state = LogicState.WAIT
#           logger.info(f"Logic job retrieved <{_state}>.")

    elif _state == LogicState.PREPARE_DONE:
        logger.info(f"Logic state <{_state.name}> begin.")
        logger.info(f"Logic state <{_state.name}> finish.")
        _state = LogicState.RECIPE
    elif _state == LogicState.RECIPE:
        logger.info(f"Logic state <{_state.name}> begin.")
        cm_idx = -1
        for idx in _cm_slot.keys():
            slot = _cm_slot[idx]
            if slot is not None and isinstance(slot, Coffee) and _cm_slot[idx].get_position_state() == Coffee.Position.NONE:
                cm_idx = idx
                break
        if cm_idx < 0:
            _state = LogicState.IDLE

        coffee: Coffee = _cm_slot[cm_idx]
        coffee.set_position_state(Coffee.Position.COFFEE_MACHINE)
        menu = recipe.RECIPE_BY_INDEX[coffee.get_menu_number()]
        if menu.is_using_milk():
            _job_refresh_milk.reset_duration()
        menu.do_recipe(_context, coffee)
        if menu.is_using_milk():
            _job_refresh_milk.reset_duration()
        logger.info(f"Logic state <{_state.name}> finish.")
        _state = LogicState.IDLE
    elif _state == LogicState.LIFT:
        logger.info(f"Logic state <{_state.name}> begin.")
        lift_idx = -1

        for idx in _lift_slot.keys():
            if _lift_slot[idx] is True:
                lift_idx = idx
                break

        if lift_idx < 0:
            return

        cm_idx = -1
        for idx in _cm_slot.keys():
            if _cm_slot[idx] is not None and isinstance(_cm_slot[idx], Coffee) and _cm_slot[idx].is_dropped():
                cm_idx = idx
                break
        
        if cm_idx < 0:
            return

        if test_mode:
            with _context.logger() as logger:
                logger.debug("Lifting")
        else:
            shm = _context.acquire_shm()
            logger.info(f"CM Slot[{cm_idx}] -> Lift Slot[{lift_idx}]")
            shm.write_direct_variable('B', INDY_ADDR_CM_SLOT, cm_idx)
            shm.write_direct_variable('B', INDY_ADDR_LIFT_SLOT, lift_idx)
            shm.write_direct_variable('B', INDY_ADDR_COMMAND, INDY_CMD_MOVE_LIFT_SLOT)
            while shm.read_direct_variable('B', INDY_ADDR_COMMAND) != INDY_CMD_IDLE and not worker.is_stopping():
                _context.release_shm()
                time.sleep(0.5)
                shm = _context.acquire_shm()
            _context.release_shm()
        
        # Update coffee state
        coffee: Coffee = _cm_slot[cm_idx]
        _lift_slot[lift_idx] = coffee
        coffee.set_position_state(Coffee.Position.LIFT)
        coffee.set_lift_index(lift_idx)
        _cm_slot[cm_idx] = True
        order_data = coffee.get_order_data()
        order_data.decrease_remaining_coffee_count()
        logger.info(f"CM Slot[{cm_idx}] -> Lift Slot[{lift_idx}] - Logically done.")
        _coffee_logger.info(f"Coffee lifted. CM: {cm_idx}, Lift: {lift_idx}, PE_ID: {coffee.get_order_data().PE_ID}, menu: {coffee._menu.name}")
        
        lift_fulled = True
        for idx in _lift_slot.keys():
            if _lift_slot[idx] is None:
                lift_fulled = False
                break

        if order_data.get_remaining_coffee_count() == 0 or lift_fulled:
            logger.info(f"Set order state to DONE. PE_ID:{order_data.PE_ID}")
            _dev_kiosk.update_order_state(order_data, Kiosk.OrderData.ORDER_DATA_STATE_DONE)

        # Clean check
        clean_required = True
        for idx in _cm_slot.keys():
            if _cm_slot[idx] is None:
                clean_required = False
                break
        
        if _order_list.empty() or lift_fulled:
            clean_required = True
        
        # Do clean
        if clean_required:
            _job_list.put(JOB_PRIORITY_CLEAN)
            logger.info("Clear job appended.")

        # Job initialize
        logger.info(f"Logic state <{_state.name}> finish.")
        _state = LogicState.IDLE
    elif _state == LogicState.CLEAN:
        logger.info(f"Logic state <{_state.name}> begin.")
        if test_mode:
            with _context.logger() as logger:
                logger.debug("Cleaning")
        else:
            for cm_idx in _cm_slot.keys():
                if _cm_slot[cm_idx] is True:
                    logger.info(f"Trying to clean filter - idx: {cm_idx} ...")
                    shm = _context.acquire_shm()
                    shm.write_direct_variable('B', INDY_ADDR_CM_SLOT, cm_idx)
                    shm.write_direct_variable('B', INDY_ADDR_COMMAND, INDY_CMD_CLEAN)
                    while shm.read_direct_variable('B', INDY_ADDR_COMMAND) != INDY_CMD_IDLE and not worker.is_stopping():
                        _context.release_shm()
                        time.sleep(0.5)
                        shm = _context.acquire_shm()
                    _context.release_shm()
                    _cm_slot[cm_idx] = None
                    logger.info(f"Trying to clean filter - idx: {cm_idx} ... Done.")
        
        logger.info(f"Logic state <{_state.name}> finish.")
        _state = LogicState.IDLE
    elif _state == LogicState.TRASH:
        logger.info(f"Logic state <{_state.name}> begin.")
        if test_mode:
            with _context.logger() as logger:
                logger.debug("Cleaning")
        else:
            for idx in _lift_slot.keys():
                if _lift_slot[idx] is not None and isinstance(_lift_slot[idx], Coffee) and _lift_slot[idx].is_expired():
                    logger.info(f"Trying to throw the coffee away - idx: {idx} ...")
                    shm = _context.acquire_shm()
                    shm.write_direct_variable('B', INDY_ADDR_LIFT_SLOT, idx)
                    shm.write_direct_variable('B', INDY_ADDR_COMMAND, INDY_CMD_MOVE_TRASH)
                    while shm.read_direct_variable('B', INDY_ADDR_COMMAND) != INDY_CMD_IDLE and not worker.is_stopping():
                        _context.release_shm()
                        time.sleep(0.5)
                        shm = _context.acquire_shm()
                    _context.release_shm()
                    logger.info(f"Trying to throw the coffee away - idx: {idx} ... Done.")
        logger.info(f"Logic state <{_state.name}> finish.")
        _state = LogicState.IDLE
    elif _state == LogicState.WAIT:
        #logger.info(f"Logic state <{_state.name}> begin.")
        if test_mode:
            with _context.logger() as logger:
                logger.debug("Wait")
        else:
            shm = _context.acquire_shm()
            shm.write_direct_variable('B', INDY_ADDR_COMMAND, INDY_CMD_WAIT_POS)
            while shm.read_direct_variable('B', INDY_ADDR_COMMAND) != INDY_CMD_IDLE and not worker.is_stopping():
                _context.release_shm()
                time.sleep(0.5)
                shm = _context.acquire_shm()
            _context.release_shm()
            _state = LogicState.IDLE
        #logger.info(f"Logic state <{_state.name}> finish.")
    return

def set_state(state: LogicState):
    global _state
    _state = state

def get_state() -> LogicState:
    return _state

def reset_usb(bus_nm,dev_nm):
    with _context.logger() as logger:
        logger.info("Trying USB reset")
    filename = "/dev/bus/usb" + bus_nm + dev_nm
    USBDEVFS_RESET = ord('U') << (4*2) | 20
    fd = open(filename,"wb")
    rc = ioctl(fd,USBDEVFS_RESET,0)
    fd.close()
    if(rc<0):
        logger.info("Failed reset usb, error in ioctl")
        return 1
    logger.info("Reset successful")
    return 0

def on_kiosk_listener(sender, args: KioskEventArgs):
    if args.get_event_code() == KioskEventArgs.EVENT_CODE_NEW_DATA:
        if _dev_kiosk._is_test_mode and _order_list.qsize() > 10:
            return
        data: Coffee = args.get_arguments()
        with _context.logger() as logger:
            logger.info(f"Event on_kiosk_listener called. New Menu: {data._menu.name}, PEID: {data.get_order_data().PE_ID}, OJ_NO: {data.get_order_data().OJ_NO}")
        _coffee_logger.info(f"Coffee ordered. PE_ID: {data.get_order_data().PE_ID}, menu: {data._menu.name}")
        _context.get_bundle()[BUNDLE_KEY_COFFEE_DATA] = data
        _order_list.put(data)
        _job_list.put(JOB_PRIORITY_ORDER_CHECK)

def on_barcode_listener(sender, args: BarcodeArgs):
    barcode: str = args.get_arguments()
    with _context.logger() as logger:
        logger.info(f"Event on_barcode_listener called. Barcode: {barcode}")
    for idx in _lift_slot.keys():
        slot = _lift_slot[idx]
        with _context.logger() as logger:
            state = slot is not None and isinstance(slot, Coffee) # check weather slot type is Coffee
            if state:
                logger.info(f"State: {state}, position: {slot.get_position_state().name}")
            else:
                logger.info(f"State: {state}, The slot[{idx}] is None. Skip this index.") # no coffee in slot -> skip index
                
            if state and slot.get_position_state() == Coffee.Position.LIFT:
                logger.info(f"Barcode: {barcode.strip()}, PE ID: {slot.get_order_data().PE_ID.strip()}, Compare: {barcode.strip() == slot.get_order_data().PE_ID.strip()}")
                logger.info(f"Expired: {slot.is_expired()}")
                if barcode.strip() == slot.get_order_data().PE_ID.strip() and not slot.is_expired(): # barcode mattches to slot coffee PE ID
                    _lift_usage[idx] = True
                    _coffee_logger.info(f"Barcode confirmed. Lift: {idx}, PE_ID: {slot.get_order_data().PE_ID}, menu: {slot._menu.name}")

def on_coffee_done(sender, args: recipe.CoffeeRecipeDoneEventArgs):
    with _context.logger() as logger:
        logger.info("Event on_coffee_done called.")
    coffee: Coffee = args.get_arguments()
    coffee.set_drop_done()
    cm_idx = coffee.get_cm_index()
    do_idx = cm_idx * 2
    shm = _context.acquire_shm()
    shm.set_do(do_idx, False)
    _context.release_shm()
    _coffee_logger.info(f"Coffee created. CM: {cm_idx}, PE_ID: {coffee.get_order_data().PE_ID}, menu: {coffee._menu.name}")
    _job_list.put(JOB_PRIORITY_LIFT)
    
def on_preapre_done(sender, args: PreparedDoneArgs):
    with _context.logger() as logger:
        logger.info("Event on_prepare_done called.")
    set_state(LogicState.PREPARE_DONE)

def on_refresh_milk(sender, args: RefreshMilkArgs):
    with _context.logger() as logger:
        logger.info("Refresh milk called, but")
    # _job_list.put(JOB_PRIORITY_REFRESH_MILK)

def on_wait_pos(sender,args:WaitPosArgs):
    _job_list.put(JOB_PRIORITY_WAIT_POS)

def on_mailing(sender, args: MailingArgs):
    t = dt.now().strftime('%y-%m-%d %H:%M:%S')
    # with _context.logger() as logger:
    #     logger.info("Sending E-Mail...")
    # root_path = _context.get_root_path()
    # mail.send_mail(send_from="pasteldew@gmail.com",
    #     send_to=["pasteldew@gmail.com", "kimjisuk145@gmail.com"],
    #     subject="Ochang log",
    #     text=f"Send date - {t}",
    #     files=[
    #         f"{root_path}/events/worker.log",
    #         f"{root_path}/order.log"
    #         ],
    #     server="smtp.gmail.com",
    #     port=587)
    # with _context.logger() as logger:
    #     logger.info("Sending E-Mail...Done.")



