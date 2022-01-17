from events.scheduler import Job
from devices.kiosk import Coffee
from examples.cup_disp import CupDispenser

import time
import serial
from devices import device
from context import Context
from events.event_args import EventArgs

class IceDispArgs(EventArgs):
    EVENT_CODE_REQUEST    = 0
    EVENT_CODE_DONE        = 1
    pass

class IceDispenser(device.BaseDevice):
    def __init__(self) -> None:
        super().__init__()
        self.context: Context = None
        self.serialIceDispenser = None
        self._is_test = False
        self.packet_len = None

    @classmethod
    def get_device_name(cls) -> str:
        return "IceDispenser"

    def on_create(self, context: Context) -> None:
        self.context = context
        config = self.context.get_config()
        print(config["ice_only"])
        print(config["ice_and_water"])
        self.packet_len = config["ice_disp_packet_len"]
        try:
            self.serialIceDispenser = serial.Serial("/dev/ICEDISP", 9600, timeout=0.1,write_timeout = 0.1)
        except:
            self._is_test = True
        context.get_scheduler().add_event_listener(IceDispArgs, self.event_listener)

    def on_dispose(self) -> None:
        if self._is_test:
            return
        self.serialIceDispenser.close()
        self.context.get_scheduler().remove_event_listener(self.event_listener)

    def event_listener(self, sender: CupDispenser, args: IceDispArgs):
        with self.context.logger() as logger:
            logger.info(f"Event occurred! Event Type: {args.get_event_code()}, Args: {args.get_arguments()}")
        if self.serialIceDispenser.is_open:
            logger.info("ice serial is already opend!")
        else:
            self.serialIceDispenser = serial.Serial("/dev/ICEDISP",9600,timeout = 0.1, write_timeout = 0.1)
            logger.info("create new icedisp serial")
        if args.get_event_code() != IceDispArgs.EVENT_CODE_REQUEST:
            return
        coffee : Coffee = args.get_arguments()
        self.ejection(coffee.get_real_menu_number())
        self.EnableManualEjection()
        if self.serialIceDispenser.is_open:
            self.serialIceDispenser.close()
            logger.info("Close icedisp serial done")
    def execute(self):
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - Execute")

    def execute_async(self) -> None:
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - Execute_Async")

    def ejection(self, menu: int):
        self.CheckIceDispenser()
        config = self.context.get_config()
        ice_only = config["ice_only"]
        water_only = config["water_only"]
        ice_and_water = config["ice_and_water"]
        self.DisableManualEjection()
        milk_ice = ice_only - 0.5
        ame_ice = ice_only + 0.7
        if(menu == 0):
            print("b11 is 0")
            shm = self.context.acquire_shm()
            shm.set_do(16,1)
            self.EjectIceDispenser(ame_ice, ice_and_water)
            self.context.release_shm()
            time.sleep(2)
            shm = self.context.acquire_shm()
            shm.set_do(16,0)
            self.context.release_shm()
            print("complete ejection")
        elif(menu == 1 or menu == 2):
            print("b11 is 1 or 2")
            shm = self.context.acquire_shm()
            shm.set_do(16,1)
            self.EjectIceDispenser(milk_ice, water_only)
            self.context.release_shm()
            time.sleep(2)
            shm = self.context.acquire_shm()
            shm.set_do(16,0)
            self.context.release_shm()
            print("complete ejection")

        self.context.get_scheduler().add_schedule(Job(self, IceDispArgs(IceDispArgs.EVENT_CODE_DONE, None)))
    def CheckIceDispenser(self):
        packet = b'\x7A\x10\x00\x00\x7B'  # stx cmd1 cmd2 cmd3 etx
        with self.context.logger() as logger:
            logger.info(f"Called CheckIceDispenser")
        logger.info("ice status check: {packet}")
        worker = self.context.get_worker()
        packet_check = False
        packet_len = self.packet_len

        while packet_check is not True and not worker.is_stopping():
            time.sleep(0.01)
            if packet_check == True:
                break
            logger.info("Try read packet...")
            try:
                if packet_check == False:
                    self.serialIceDispenser.close()
                    logger.info("reconnet to serialIceDispenser...")
                    self.serialIceDispenser = serial.Serial("/dev/ICEDISP", 9600, timeout=0.1,write_timeout = 0.1)
                    self.serialIceDispenser.write(packet)
                    self.serialIceDispenser.flush()
                timeout = time.time()+1
                while not worker.is_stopping() and (packet_check is not True):
                    time.sleep(0.01)
                    if self.serialIceDispenser.in_waiting:
                        time.sleep(0.05)
                        status_packet = self.serialIceDispenser.read(self.serialIceDispenser.in_waiting)
                        if self.serialIceDispenser.in_waiting:
                            leftover_num = self.serialIceDispenser.in_waiting
                            status_packet += self.serialIceDispenser.read(leftover_num)
                        if len(status_packet) == packet_len:                      
                            is_error = False
                            if status_packet[1] == 0x01:
                                print("unable to sell")
                                is_error = True
                            elif status_packet[1] == 0x00:
                                print("able to sell")
                            else:
                                print("cmd1 error")
                                is_error = True
                            if is_error:
                                if status_packet[2] == 0x01:
                                    print("cleaning mode")
                                elif status_packet[2] == 0x02:
                                    print("initial drainage mode")
                                elif status_packet[2] == 0x03:
                                    print("safety mode")
                                elif status_packet[2] == 0x04:
                                    print("ice making error")
                                elif status_packet[2] == 0x05:
                                    print("EVA exit temperature sensor error")
                                elif status_packet[2] == 0x06:
                                    print("condenser temperature sensor error")
                                elif status_packet[2] == 0x07:
                                    print("high pressure error")
                                elif status_packet[2] == 0x08:
                                    print("high pressure error repeated 3 times")
                                elif status_packet[2] == 0x09:
                                    print("water level sensor(upper limit) bad")
                                    #TODO here
                                elif status_packet[2] == 0x0A:
                                    print("water level sensor(lower limit) bad")
                                elif status_packet[2] == 0x0B:
                                    print("motor is bound")
                                elif status_packet[2] == 0x0C:
                                    print("is selling now")
                                elif status_packet[2] == 0x00:
                                    print("mod switch off")
                                else:
                                    print("cmd2 error")

                                is_error = False
                            packet_check = True
                            logger.info("status check done")
                        break
            except:
                logger.info("read packet failed... try again.....")

    def EjectIceDispenser(self,ice_time, water_time):  # time in seconds(0.0s~25.5s)
        packet = bytearray(b'\x7A\x11\x00\x00\x7B')  # stx cmd1 cmd2 cmd3 etx
        packet[2] = int(float(ice_time) * 10)
        packet[3] = int(float(water_time) * 10)
        self.serialIceDispenser.write(packet)
        print("eject ice:", packet)
        worker = self.context.get_worker()
        while not worker.is_stopping():
            if self.serialIceDispenser.in_waiting:
                print("eject ice Disp starting!!!!!!")
                time.sleep(0.05)
                status_packet = self.serialIceDispenser.readline()
                leftover_num = self.serialIceDispenser.in_waiting
                status_packet += self.serialIceDispenser.read(leftover_num)
                print("ejection result:", status_packet)
                break
            time.sleep(0.05)

    def DisableManualEjection(self):
        packet = b'\x7A\x14\x00\x00\x7B'  # stx cmd1 cmd2 cmd3 etx
        self.serialIceDispenser.write(packet)
        print("Disable Manual Ejection:", packet)

    def EnableManualEjection(self):
        packet = b'\x7A\x13\x00\x00\x7B'  # stx cmd1 cmd2 cmd3 etx
        self.serialIceDispenser.write(packet)
        time.sleep(0.3)
        print("Enable Manual Ejection:", packet)
