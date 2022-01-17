from examples.sample_device1 import SampleDevice1, SampleEventArgs
import os, sys
# sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../"))
from devices import device
from context import Context

class SampleDevice2(device.BaseDevice):
    def __init__(self) -> None:
        super().__init__()
        self.context: Context = None

    @classmethod
    def get_device_name(cls) -> str:
        return "SampleDevice2"
    
    def on_create(self, context: Context) -> None:
        self.context = context
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - OnCreate")

        context.get_scheduler().add_event_listener(SampleEventArgs, self.event_listener)
    
    def on_dispose(self) -> None:
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - OnDispose")
        self.context.get_scheduler().remove_event_listener(self.event_listener)
    
    def event_listener(self, sender: SampleDevice1, args: SampleEventArgs):
        with self.context.logger() as logger:
            logger.info(f"Event occurred! Event Type: {args.get_event_code()}, Args: {args.get_arguments()}")
    
    def execute(self):
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - Execute")
    
    def execute_async(self) -> None:
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - Execute_Async")
