from events.event_args import EventArgs
from events.scheduler import Job

from . import device
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

        self.barcode_serial = serial.Serial("/dev/BARCODE", 115200)
        self.thread = threading.Thread(target=self.barcode_thread)
        logger.info("barcode thread start")
        self.thread.start()
    
    def on_dispose(self) -> None:
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - OnDispose")
        self.thread.join()
        logger.info("barcode thread end")

    def barcode_thread(self):
        serial = self.barcode_serial
        worker = self.context.get_worker()
        while not worker.is_stopping():
            if serial.in_waiting:
                self.barcode_data = None
                self.barcode_data = serial.readline()
                self.barcode_data = self.barcode_data.decode('utf-8')
                print("device :", self.barcode_data)
                self.context.get_scheduler().add_schedule(Job(self, BarcodeArgs(0, self.barcode_data.strip())))
      
