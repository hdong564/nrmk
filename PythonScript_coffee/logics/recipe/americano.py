import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../../"))

from events.scheduler import Job
from .event_args import CoffeeRecipeDoneEventArgs
from devices.kiosk import Coffee
from Config import *
from context import Context
import time

def is_using_milk() -> bool:
    return False

def do_recipe(context: Context, coffee: Coffee):
    worker = context.get_worker()
    shm = context.acquire_shm()
    shm.write_direct_variable('B', INDY_ADDR_MENU, coffee.get_real_menu_number())
    shm.write_direct_variable('B', INDY_ADDR_COMMAND, INDY_CMD_MOVE_HOT_WATER)
    while shm.read_direct_variable('B', INDY_ADDR_COMMAND) != 0 and not worker.is_stopping():
        temp = shm.read_direct_variable('B',INDY_ADDR_COMMAND)
        print(f"testing1....{temp}")
        context.release_shm()
        time.sleep(0.5)
        shm = context.acquire_shm()
    context.release_shm()
    if worker.is_stopping():
        return

    #TODO: If you want to change DO num. for espresso machine, you have to modify below codes.
    cm_idx = coffee.get_cm_index()
    config_key = ESPRESSO_LONG_DELAY_KEY_LIST[cm_idx]

    shm = context.acquire_shm()
    shm.write_direct_variable('B', INDY_ADDR_CM_SLOT, cm_idx)
    shm.write_direct_variable('B', INDY_ADDR_COMMAND, INDY_CMD_MOVE_CM_SLOT)
    while shm.read_direct_variable('B', INDY_ADDR_COMMAND) != 0 and not worker.is_stopping():
        temp = shm.read_direct_variable('B',11)
        print(f"testing2....b11: {temp}")
        context.release_shm()
        time.sleep(0.5)
        shm = context.acquire_shm()
        if worker.is_stopping():
            context.release_shm()
            return

    do_idx = cm_idx * 2
    shm.set_do(do_idx, True)
    time.sleep(0.3)
    context.get_scheduler().add_schedule(Job(None, CoffeeRecipeDoneEventArgs(0, coffee), context.get_config()[config_key]))
    shm.set_do(do_idx,False)
    context.release_shm()
