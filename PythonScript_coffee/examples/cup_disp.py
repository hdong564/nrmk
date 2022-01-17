from examples.sample_device1 import SampleDevice1, CupDispArgs
import os, sys
# sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../"))
from devices import device
from context import Context
from events.event_args import EventArgs
from events.scheduler import Job
from events.worker import Worker
import serial,time

class CupDispenser(device.BaseDevice):
    def __init__(self) -> None:
        super().__init__()
        self.context: Context = None
        self.serialCupDispenser1 = None
        self.serialCupDispenser2 = None
        self.serialCupDispenser = None
        self.current_boad = 0
        self.b10 = -1
    @classmethod
    def get_device_name(cls) -> str:
        return "CupDispenser"
    
    def on_create(self, context: Context) -> None:
        self.context = context
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - OnCreate")
        context.get_scheduler().add_event_listener(CupDispArgs, self.event_listener) #주문 입력 이벤트 받기
    
    def on_dispose(self) -> None:
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - OnDispose")
        self.context.get_scheduler().remove_event_listener(self.event_listener)
    
    def event_listener(self, sender: SampleDevice1, args: CupDispArgs): #sender 교체 (작업 시작하는 devices)
        with self.context.logger() as logger:
            logger.info(f"Event occurred! Event Type: {args.get_event_code()}, Args: {args.get_arguments()}")
        # flag 0 = hot / 1 = ice
        self.b10 = args.get_arguments()
        if (self.b10 == 0 or self.b10 == 1):

            logger.info(f"Order : Hot")
            if (self.IsDispenserFilled(self.b10)): #비어있는 조건  제대로 실행되는지 확인 해야함
                self.EjectDispenser(self.b10)
            elif (self.IsDispenserFilled(self.b10)):
                self.EjectDispenser(self.b10)
            else:
                raise NotImplementedError()
        elif (self.b10 == 2 or self.b10 == 3):
            logger.info(f"Order: Ice")
            if (self.IsDispenserFilled(self.b10)):
                self.EjectDispenser(self.b10)
            elif(self.IsDispenserFilled(self.b10)):
                self.EjectDispenser(self.b10)
            else:
                raise NotImplementedError()
    def execute(self):
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - Execute")
    
    def execute_async(self) -> None:
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - Execute_Async")


    def EjectDispenser(self,b10):
        # b10 : 0,1 = 1번보드(hot) / 2,3 = 2번보드(ice)
        packet = bytearray(b'\x02\x03\x41\x00\x00\x03\x00')
        column = b10
        packet[3] = column + 1
        packet[4] = 1  # number of cups

        for i in range(1, 6):  # packet[6] is checksum byte
            packet[6] += packet[i]

        packet[6] %= 256  # lsb만 취한다

        if(b10 == 0 or b10 == 1):
            self.current_boad = 1
            self.serialCupDispenser = serial.Serial("/dev/ttyUSB1",9600,timeout=0)
        elif(b10 == 2 or b10 == 3):
            self.current_boad = 2
            self.serialCupDispenser = serial.Serial("/dev/ttyUSB2",9600,timeout=0)
            column -= 2
        self.serialCupDispenser.write(packet)
        worker = self.context.get_worker()
        while not worker.is_stopping():
            
            if self.IsEjectionFinished(self,b10):
                print(f"boad{self.current_boad}'s coulumn{column} ejection finished")
                #TODO b변수 변경
                break
            elif not self.IsEjectionFinished(self,b10):
                print("ejection not finished")

            if self.serialCupDispenser.in_waiting:
                time.sleep(0.05)
                status_packet = self.serialCupDispenser1.readline()
                leftover_num = self.serialCupDispenser1.in_waiting
                status_packet += self.serialCupDispenser1.read(leftover_num)
                if status_packet[6] & 0x01:
                    print(f"boad{self.current_boad}'s coulumn{column} ejecting now...")
                    time.sleep(4)  # 컵 사출되는데 걸리는 시간
                    #TODO 완료 신호 정상작동 하는지 확인해야함. 정상작동 시 완료신호 전송

    def IsDispenserFilled(self,b10):
        # b10 : 0,1 = 1번보드(hot) / 2,3 = 2번보드(ice)
        packet = b'\x02\x01\x40\x03\x44'  # stx len cmd etx bcc
        column = b10
        if(b10 == 0 or b10 == 1):
            self.current_boad = 1
            self.serialCupDispenser = serial.Serial("/dev/ttyUSB1",9600,timeout=0)
        elif(b10 == 2 or b10 == 3):
            self.current_boad = 2
            self.serialCupDispenser = serial.Serial("/dev/ttyUSB2",9600,timeout=0)
            column -= 2
        self.serialCupDispenser.write(packet)

        worker = self.context.get_worker()
        while not worker.is_stopping():
            if self.serialCupDispenser.in_waiting:
                time.sleep(0.05)
                status_packet = self.serialCupDispenser.readline()
                leftover_num = self.serialCupDispenser.in_waiting
                status_packet += self.serialCupDispenser.read(leftover_num)

                if status_packet[8] & (1 << (column)):
                    print(f"boad{self.current_boad} Column", column, " is Filled")
                    return True
                elif ~status_packet[8] & (1 << (column)):
                    print(f"boad{self.current_boad} Column", column, " is Empty")
                    return False
                break

    def IsEjectionFinished(self,b10):
        # b10 : 0,1 = 1번보드(hot) / 2,3 = 2번보드(ice)
        packet = b'\x02\x01\x40\x03\x44'  # stx len cmd etx bcc
        column = b10
        if(b10 == 0 or b10 == 1):
            self.current_boad = 1
            self.serialCupDispenser = serial.Serial("/dev/ttyUSB1",9600,timeout=0)
        elif(b10 == 2 or b10 == 3):
            self.current_boad = 2
            self.serialCupDispenser = serial.Serial("/dev/ttyUSB2",9600,timeout=0)
            column -= 2
        self.serialCupDispenser.write(packet)

        worker = self.context.get_worker()
        while not worker.is_stopping():
            if self.serialCupDispenser.in_waiting:
                time.sleep(0.05)
                status_packet = self.serialCupDispenser.readline()
                leftover_num = self.serialCupDispenser.in_waiting
                status_packet += self.serialCupDispenser.read(leftover_num)

                if status_packet[6] & 0x01:
                    print(f"boad{self.current_boad} Column", column, " is Filled")
                    return True
                elif status_packet[6] & 0x10:
                    print(f"boad{self.current_boad} Column", column, " is Empty")
                    return False
                break
        

        

