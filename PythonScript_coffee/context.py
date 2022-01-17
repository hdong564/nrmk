from events.scheduler import Scheduler
import os
try:
    from indy_utils import indy_shm
    NO_INDY_SHM = False
except:
    class indy_shm:
        class IndyShmCommand:
            pass
    NO_INDY_SHM = True
import threading, logging, events
import events

class Context:
    pass

from devices.device import BaseDevice
class Context:
    TEST_MODE_ON = 0b00000001

    class LockedLogger:
        def __init__(self, logger_lock: threading.Lock, logger: logging.Logger) -> None:
            self._logger_lock = logger_lock
            self._logger = logger
        
        def __enter__(self):
            self._logger_lock.acquire()
            return self._logger
        
        def __exit__(self, exc_type, exc_value, traceback):
            self._logger_lock.release()
        
        def acquire(self) -> logging.Logger:
            self._logger_lock.acquire()
            return self._logger
        
        def release(self):
            self._logger_lock.release()

    def __init__(self) -> None:
        self.__shm = None
        self._shm_lock = threading.Lock()
        self._logger_lock = threading.Lock()
        self._logger = None
        self._config = None
        self._worker = None
        self._devices = {}
        self._bundle = {}
        self._scheduler = None
        self._test_mode = 0
        self._root_path = os.path.dirname(os.path.realpath(__file__))
    
    def set_test_mode(self, modes: int):
        self._test_mode = modes
    
    def get_test_mode(self) -> int:
        return self._test_mode
    
    def set_root_path(self, path: str):
        self._root_path = path
    
    def get_root_path(self) -> str:
        return self._root_path

    def add_test_mode(self, mode: int):
        self._test_mode = self._test_mode | mode
    
    def remove_test_mode(self, mode: int):
        if self._test_mode & mode:
            self._test_mode = self._test_mode ^ mode
    
    def is_test_mode(self) -> bool:
        return self._test_mode != 0
    
    def set_indy_shm_config(self, sync_mode: bool, joint_dof: int=6) -> None:
        if not NO_INDY_SHM:
            self.__shm = indy_shm.IndyShmCommand(sync_mode=sync_mode, joint_dof=joint_dof)
    
    def set_indy_shm(self, shm: indy_shm.IndyShmCommand) -> None:
        self.__shm = shm
    
    def set_logger(self, logger: logging.Logger) -> None:
        self._logger = logger
    
    def set_config(self, config: dict) -> None:
        self._config = config
    
    def get_config(self) -> dict:
        return self._config
    
    def set_worker(self, worker: events.Worker):
        self._worker = worker
    
    def get_worker(self) -> events.Worker:
        return self._worker
    
    def set_scheduler(self, scheduler: Scheduler):
        self._scheduler = scheduler

    def get_scheduler(self) -> Scheduler:
        return self._scheduler
    
    def get_bundle(self) -> dict:
        return self._bundle

    def add_device(self, device: BaseDevice) -> None:
        dev_name = device.get_device_name()
        if dev_name in self._devices.keys():
            return
        self._devices[dev_name] = device
    
    def remove_device(self, device: BaseDevice) -> None:
        dev_name = device.get_device_name()
        if dev_name in self._devices.keys():
            del self._devices[dev_name]
        
    def clear_devices(self) -> None:
        self._devices.clear()
    
    def get_device_by_name(self, device_name: str) -> BaseDevice:
        device = None
        if device_name in self._devices.keys():
            device = self._devices[device_name]
        return device
    
    def get_devices(self) -> list:
        return self._devices.values()

    @classmethod
    def __get_instance(cls):
        return cls.__instance

    @classmethod
    def get_instance(cls):
        cls.__instance = Context()
        cls.get_instance = cls.__get_instance
        return cls.__instance
    
    def acquire_logger(self) -> logging.Logger:
        self._logger_lock.acquire()
        return self._logger
    
    def acquire_shm(self) -> indy_shm.IndyShmCommand:
        self._shm_lock.acquire()
        return self.__shm
    
    def release_logger(self) -> None:
        self._logger_lock.release()
    
    def release_shm(self) -> None:
        self._shm_lock.release()
    
    def logger(self) -> 'Context.LockedLogger':
        return Context.LockedLogger(self._logger_lock, self._logger)

    def is_logger_locked(self) -> bool:
        return self._logger_lock.locked()

    def is_shm_locked(self) -> bool:
        return self._shm_lock.locked()
