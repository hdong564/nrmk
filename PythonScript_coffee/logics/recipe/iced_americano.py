from devices.ice_disp import IceDispArgs
from events.scheduler import Job
from .event_args import CoffeeRecipeDoneEventArgs
from devices.kiosk import Coffee
from Config import *
from context import Context
import time

is_waiting_ice = False

def is_using_milk() -> bool:
    return False

def wait_move(shm, context:Context):
    worker = context.get_worker()
    while shm.read_direct_variable('B', INDY_ADDR_COMMAND) != 0 and not worker.is_stopping():
        context.release_shm()
        time.sleep(0.5)
        shm = context.acquire_shm()

def do_recipe(context: Context, coffee: Coffee):
    global is_waiting_ice
    worker = context.get_worker()
    shm = context.acquire_shm()
    shm.write_direct_variable('B', INDY_ADDR_MENU, coffee.get_real_menu_number())
    shm.write_direct_variable('B', INDY_ADDR_COMMAND, INDY_CMD_MOVE_ICE)
    wait_move(shm, context)
    context.release_shm()
    if worker.is_stopping():
        return

    context.get_scheduler().add_event_listener(
        IceDispArgs, on_ice_listener
    ).add_schedule(
        Job(None, IceDispArgs(IceDispArgs.EVENT_CODE_REQUEST, coffee))
    )
    is_waiting_ice = True
    while is_waiting_ice and not worker.is_stopping():
        time.sleep(0.2)
    if worker.is_stopping():
        return
     
    cm_idx = coffee.get_cm_index()
    config_key = ESPRESSO_LONG_DELAY_KEY_LIST[cm_idx]

    shm = context.acquire_shm()
    shm.write_direct_variable('B', INDY_ADDR_CM_SLOT, cm_idx)
    shm.write_direct_variable('B', INDY_ADDR_COMMAND, INDY_CMD_MOVE_CM_SLOT)
    wait_move(shm, context)
    if worker.is_stopping():
        context.release_shm()

    #TODO: If you want to change DO num. for espresso machine, you have to modify below codes.
    do_idx = cm_idx * 2
    shm.set_do(do_idx, True)
    time.sleep(0.3)
    shm.set_do(do_idx,False)
    context.release_shm()
    context.get_scheduler().add_schedule(
        Job(None, CoffeeRecipeDoneEventArgs(0, coffee), context.get_config()[config_key])
    ).remove_event_listener(on_ice_listener)

def on_ice_listener(sender, args: IceDispArgs):
    global is_waiting_ice
    if args.get_event_code() != IceDispArgs.EVENT_CODE_DONE:
        return
    is_waiting_ice = False
