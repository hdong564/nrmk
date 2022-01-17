from events import *
from enum import Enum, auto
from context import Context
from devices.kiosk import *
from Config import *

class Coffee:
    class Menu(Enum):
        """
        get_menu_number(): returns sequencial index of menu. (e.g.: 0: Iced Americano, 2: Iced Cappuccino, 4: Cafelatte, 5: Cappuccino)
        get_real_menu_number(): returns identified menu number. (e.g.: 0: Americano, 1: Cafelatte, 2: Cappuccino)
        """
        ICED_AMERICANO = 0
        ICED_CAFFELATTE = auto()
        ICED_CAPPUCCINO = auto()
        AMERICANO = auto()
        CAFFELATTE = auto()
        CAPPUCCINO = auto()
    class CoffeeEventArgs(EventArgs):
        COFFEE_REMOVE = 0

    class Position(Enum):
        NONE                = 0
        COFFEE_MACHINE      = auto()
        LIFT                = auto()
        RECYCLE_BIN         = auto()

    def __init__(self, context: Context, order_data: Kiosk.OrderData) -> None:
        config = context.get_config()
        self._menu = Coffee.Menu(int(config[CONFIG_KEY_COFFEE_MAP][order_data.OJ_PRCODE]))

        self._order_data = order_data
        final_ice_index = Coffee.Menu.ICED_CAPPUCCINO.value

        self._is_iced = (0 <= self._menu.value <= final_ice_index)
        self._is_dropped = False
        self._context = context
        self._pos_state = Coffee.Position.NONE
        self._cm_idx = -1
        self._lift_idx = -1
        self._remove_job = None
        self._is_expired = False
        self._is_junk = False
        self._is_finished = False
        if self._is_iced:
            self._real_menu = self._menu.value
        else:
            self._real_menu = self._menu.value - final_ice_index - 1
        
    def get_order_data(self) -> Kiosk.OrderData:
        return self._order_data

    def get_menu_number(self) -> int:
        """
        returns sequencial index of menu. (e.g.: 0: Iced Americano, 2: Iced Cappuccino, 4: Cafelatte, 5: Cappuccino)
        """
        return self._menu.value

    def get_real_menu_number(self) -> int:
        """
        returns identified menu number. (e.g.: 0: Americano, 1: Cafelatte, 2: Cappuccino)
        """
        return self._real_menu

    def is_iced(self) -> bool:
        return self._is_iced

    def set_drop_done(self):
        self._is_dropped = True
        self._remove_job = Job(self, Coffee.CoffeeEventArgs(0, self), int(self._context.get_config()[CONFIG_KEY_COFFEE_EXPIRY_TIME]))
        self._context.get_scheduler()\
            .add_schedule(self._remove_job)\
            .add_event_listener(Coffee.CoffeeEventArgs, self.on_expired_listener)
    
    def on_expired_listener(self, sender, args: 'Coffee.CoffeeEventArgs'):
        logger = self._context.acquire_logger()
        if sender is not self:
            self._context.release_logger()
            return
        if self._lift_idx < 0:
            self._remove_job.Duration = self._remove_job.Duration / 2
            self._remove_job.reset_duration()
            self._context.get_scheduler().add_schedule(self._remove_job)
            logger.info(f"Coffee expired. But, not lifted coffee. Rewind half of expiry time. ({self._remove_job.Duration})")
            self._context.release_logger()
            return
        logger.info(f"Coffee expired. CM Slot: {self._cm_idx}, Lift slot: {self._lift_idx}, Menu: {self._menu.name}, PEID: {self._order_data.PE_ID}, OJ_NO: {self._order_data.OJ_NO}")
        self._is_expired = True
        self._context.release_logger()
    
    def set_junk(self):
        self._is_junk = True
    
    def is_junk(self) -> bool:
        return self._is_junk

    def is_expired(self) -> bool:
        return self._is_expired

    def is_dropped(self) -> bool:
        return self._is_dropped

    def finish(self):
        self._is_finished = True

    def is_finished(self) -> bool:
        return self._is_finished

    def set_position_state(self, pos: 'Coffee.Position'):
        self._pos_state = pos

    def get_position_state(self) -> 'Coffee.Position':
        return self._pos_state

    def set_cm_index(self, idx):
        if idx is None:
            self._cm_idx = -1
        self._cm_idx = idx

    def get_cm_index(self) -> int:
        return self._cm_idx

    def set_lift_index(self, idx):
        if idx is None:
            self._lift_idx = -1
        self._lift_idx = idx
    
    def get_lift_index(self) -> int:
        return self._lift_idx

    def dispose(self):
        self._context.get_scheduler().remove_schedule(self._remove_job)
