from examples.sample_device1 import SampleDevice1, SampleEventArgs
import os, sys
# sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../"))

from events.event_args import EventArgs
from events.scheduler import Job
from events.worker import Worker

from devices import device
from context import Context
import threading
import serial

class BarcodeArgs(EventArgs):
    pass

class BarcodeReader(device.BaseDevice):
    def __init__(self) -> None:
        super().__init__()
        self.context: Context = None
        self.thread: threading.Thread = None
        self.barcode_serial = None
        self.barcode_data = None
    @classmethod
    def get_device_name(cls) -> str:
        return "BarcodeReader"
    
    def on_create(self, context: Context) -> None:
        self.context = context
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - OnCreate")

        self.barcode_serial = serial.Serial("/dev/ttyACM0", 115200)
        self.thread = threading.Thread(target=self.barcode_thread)
        if(self.thread.is_alive):
            print("kill barcode thread before start ")
            self.thread.join()
        logger.info("barcode thread start")
        self.thread.start()

        context.get_scheduler().add_event_listener(SampleEventArgs, self.event_listener)
    
    def on_dispose(self) -> None:
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - OnDispose")
        self.thread.join()
        logger.info("barcode thread end")
        self.context.get_scheduler().remove_event_listener(self.event_listener)

    def barcode_thread(self):
        serial = self.barcode_serial
        worker = self.context.get_worker()
        while not worker.is_stopping():
            if serial.in_waiting:
                self.barcode_data = None
                self.barcode_data = serial.readline()
                self.barcode_data = self.barcode_data.decode('utf-8').strip()
                print("device :", self.barcode_data)
                self.context.get_scheduler().add_schedule(BarcodeArgs, Job(self, BarcodeArgs(0,self.barcode_data)))
      
    
    def event_listener(self, sender: SampleDevice1, args: SampleEventArgs):
        with self.context.logger() as logger:
            logger.info(f"Event occurred! Event Type: {args.get_event_code()}, Args: {args.get_arguments()}")
    
    def execute(self):
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - Execute")
    
    def execute_async(self) -> None:
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - Execute_Async")
