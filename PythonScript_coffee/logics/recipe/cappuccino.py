import os, sys
print(os.path.abspath(os.path.dirname(__file__) + "/../../"))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../../"))

from events.scheduler import Job
from .event_args import CoffeeRecipeDoneEventArgs
from devices.kiosk import Coffee
from Config import *
from context import Context
import time

def is_using_milk() -> bool:
    return True

def wait_move(shm, context:Context):
    worker = context.get_worker()
    while shm.read_direct_variable('B', INDY_ADDR_COMMAND) != 0 and not worker.is_stopping():
        context.release_shm()
        time.sleep(0.5)
        shm = context.acquire_shm()

def do_recipe(context: Context, coffee: Coffee):
    worker = context.get_worker()
    shm = context.acquire_shm()
    shm.write_direct_variable('B', INDY_ADDR_MENU, coffee.get_real_menu_number())
    shm.write_direct_variable('B', INDY_ADDR_COMMAND, INDY_CMD_MOVE_MILK)
    wait_move(shm, context)
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
        context.release_shm()
        time.sleep(0.5)
        shm = context.acquire_shm()
    if worker.is_stopping():
        context.release_shm()
        return

    do_idx = cm_idx * 2
    shm.set_do(do_idx, True)
    time.sleep(0.3)
    context.get_scheduler().add_schedule(
        Job(None, CoffeeRecipeDoneEventArgs(0, coffee), context.get_config()[config_key])
    )
    context.release_shm()
