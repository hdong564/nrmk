import abc, os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from context import Context

class BaseDevice:
    def __init__(self) -> None:
        self._name = self.get_device_name()
        self._on_complete_callback = None
    
    @classmethod
    def is_singleton(cls) -> bool:
        return False
    
    @classmethod
    def get_device_name(cls) -> str:
        raise NotImplementedError()
    
    def set_on_complete_callback(self, callback):
        self._on_complete_callback = callback
    
    @abc.abstractmethod
    def on_create(self, context: Context) -> None:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def on_dispose(self) -> None:
        raise NotImplementedError()

    

class BaseDeviceSingleton(BaseDevice):
    @classmethod
    def is_singleton(cls) -> bool:
        return True

    @classmethod
    def __get_instance(cls):
        return cls.__instance

    @classmethod
    def get_instance(cls):
        cls.__instance = BaseDeviceSingleton()
        cls.get_instance = cls.__get_instance
        return cls.__instance
