from devices.ice_disp import IceDispArgs
from examples.sample_device1 import SampleDevice1, CupDispArgs
import os,sys

from devices.kiosk import Coffee
from logics.recipe.event_args import MainEventArgs, PreparedDoneArgs
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
        self.serialCupDispenser = None
        self.current_boad = 0
        self.b10 = -1
        self.packet_len = None
    @classmethod
    def get_device_name(cls) -> str:
        return "CupDispenser"
    def on_create(self, context: Context) -> None:
        self.context = context
        config = self.context.get_config()
        self.packet_len = config["cup_disp_packet_len"]
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - OnCreate")
        context.get_scheduler().add_event_listener(MainEventArgs, self.event_listener) #주문 입력 이벤트 받
    def on_dispose(self) -> None:
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - OnDispose")
        self.serialCupDispenser.close()
        self.context.get_scheduler().remove_event_listener(self.event_listener)

    def event_listener(self, sender: None, args: MainEventArgs):
        with self.context.logger() as logger:
            logger.info(f"Event occurred! Event Type: {args.get_event_code()}, Args: {args.get_arguments()}")
        # flag 0 1 = hot / 2 3 = ice
        coffee: Coffee = args.get_arguments()
        if coffee is not None:
            if coffee.is_iced():
                self.b10 = 2
            else:
                self.b10 = 0
            shm = self.context.acquire_shm()
            shm.write_direct_variable("B",20,coffee.get_cm_index()) # 이동해야하는 컵 위치 = 핫 1 번 설정
            self.context.release_shm()
        #Loop Test code start
        worker = self.context.get_worker()
        '''
        if (self.b10 == 0):
            logger.info("This Order : Hot")
            logger.info("hot 1 eject start")
            shm = self.context.acquire_shm()
            shm.write_direct_variable("B",10,0) # 이동해야하는 컵 위치 = 핫 1 번 설정
            shm.write_direct_variable("B",0,1)
            self.context.release_shm()
            while not worker.is_stopping():
                shm = self.context.acquire_shm()
                move = shm.read_direct_variable('B',0)
                self.context.release_shm()
                if(move == 0):
                    print("move start")
                    self.context.get_scheduler().add_schedule(Job(None,PreparedDoneArgs(0,0)))
                    break
        elif (self.b10 == 2):
            logger.info("This Order: Ice")
            logger.info("Ice 1 eject start")
            shm = self.context.acquire_shm()
            shm.write_direct_variable("B",10,2) # 이동해야하는 컵 위치 = 아이스 1번(0,1,2,3)
            shm.write_direct_variable("B",0,1) # move start
            self.context.release_shm()
            while not worker.is_stopping():
                shm = self.context.acquire_shm()
                move = shm.read_direct_variable('B',0)
                self.context.release_shm()
                if(move == 0):
                    print("move start")
                    self.context.get_scheduler().add_schedule(Job(None,PreparedDoneArgs(0,0)))
                    break
        #Loop Test code end
        '''
        #'''
        if (self.b10 == 0):
            logger.info("This Order : Hot")
            if (self.IsDispenserFilled(self.b10)):#비어있는 조건  제대로 실행되는지 확인 해야함
                logger.info("hot 1 eject start")
                shm = self.context.acquire_shm()
                shm.write_direct_variable("B",10,0) # 이동해야하는 컵 위치 = 핫 1 번 설정
                shm.write_direct_variable("B",0,1)
                self.context.release_shm()
                while not worker.is_stopping():
                    shm = self.context.acquire_shm()
                    move = shm.read_direct_variable('B',0)
                    self.context.release_shm()
                    if(move == 0):
                        logger.info("move start")
                        self.EjectDispenser(self.b10)
                        break
            elif (self.IsDispenserFilled(self.b10+1)):
                logger.info("hot 2 eject start")
                shm = self.context.acquire_shm()
                shm.write_direct_variable("B",10,1) # 이동해야하는 컵 위치 = 핫 1 번 설정
                shm.write_direct_variable("B",0,1)
                self.context.release_shm()
                while not worker.is_stopping():
                    shm = self.context.acquire_shm()
                    move = shm.read_direct_variable('B',0)
                    self.context.release_shm()
                    if(move == 0):
                        logger.info("move start")
                        self.EjectDispenser(self.b10+1)
                        break
            else:
                raise NotImplementedError()
        elif (self.b10 == 2):
            logger.info("This Order: Ice")
            #일단 아이스1번일때만 테스트 해보고 정상 작동하면 작동
            if (self.IsDispenserFilled(self.b10)):
            #if (True):
                logger.info("Ice 1 eject start")
                shm = self.context.acquire_shm()
                shm.write_direct_variable("B",10,2) # 이동해야하는 컵 위치 = 아이스 1번(0,1,2,3)
                shm.write_direct_variable("B",0,1) # move start
                self.context.release_shm()
                #while문에 예외처리 해야함(worker 의 is_stopping)
                while not worker.is_stopping():
                    shm = self.context.acquire_shm()
                    move = shm.read_direct_variable('B',0)
                    self.context.release_shm()
                    if(move == 0):
                        logger.info("move start")
                        self.EjectDispenser(self.b10)
                        break
            elif(self.IsDispenserFilled(self.b10+1)):
                logger.info("Ice 2 eject start")
                shm = self.context.acquire_shm()
                shm.write_direct_variable("B",10,3) # 이동해야하는 컵 위치 = 아이스2 번 설정
                shm.write_direct_variable("B",0,1)
                self.context.release_shm()
                while not worker.is_stopping():
                    shm = self.context.acquire_shm()
                    move = shm.read_direct_variable('B',0)
                    self.context.release_shm()
                    if(move == 0):
                        logger.info("move start")
                        self.EjectDispenser(self.b10+1)
                        break
            else:
                raise NotImplementedError()
        logger.info("serialCupDispenser close...")
        #'''
    def execute(self):
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - Execute")
    def execute_async(self) -> None:
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - Execute_Async")
    def EjectDispenser(self,b10):
        with self.context.logger() as logger:
            logger.info("Called EjectDispenser")
        # b10 : 0,1 = 1번보드(hot) / 2,3 = 2번보드(ice)
        packet = bytearray(b'\x02\x03\x41\x00\x00\x03\x00')
        column = b10
        
        worker = self.context.get_worker()
          # lsb만 취한다
        while not worker.is_stopping():
            time.sleep(0.01)
            try:
                if(b10 == 0 or b10 == 1):
                    self.current_boad = 1
                    self.serialCupDispenser = serial.Serial("/dev/HOTBOARD",9600,timeout = 0.1,write_timeout=0.1)
                    break
                elif(b10 == 2 or b10 == 3):
                    self.current_boad = 2
                    self.serialCupDispenser = serial.Serial("/dev/ICEBOARD",9600,timeout = 0.1,write_timeout=0.1)
                    column -= 2
                    break
            except serial.SerialException as e:
                logger.info(f"{e}....")
        if self.serialCupDispenser is None:
            logger.info("Serial connect Failed... Exit EjectDispenser Fnc")
            return
        packet[3] = column + 1
        packet[4] = 1  # number of cups
        for i in range(1, 6):  # packet[6] is checksum byte
            packet[6] += packet[i]
        packet[6] %= 256
        packet_check = False
        packet_len = self.packet_len

        while packet_check is not True and not worker.is_stopping():
            time.sleep(0.01)
            if packet_check == True:
                break
            # logger.info("Try read packet...")
            try:
                if packet_check == False:
                    self.serialCupDispenser.write(packet)
                    self.serialCupDispenser.flush()
                timeout = time.time()+1
                while not worker.is_stopping() and (packet_check is not True):
                    if self.IsEjectionFinished(b10):
                        logger.info(f"boad{self.current_boad}'s column {column} ejection finished")
                        self.context.get_scheduler().add_schedule(Job(None,PreparedDoneArgs(0,0)))
                        packet_check = True
                        break
                    elif not self.IsEjectionFinished(b10):
                        logger.info("ejection not finished")
                    if time.time() > timeout:
                        logger.info("time out with in_waiting... read request again...")
                        break
                    #아래 코드 나오는지 테스트 필요
                    '''
                    if self.serialCupDispenser.in_waiting:
                        logger.info("ejecting........")
                        time.sleep(0.05)
                        status_packet = self.serialCupDispenser.readline()
                        leftover_num = self.serialCupDispenser.in_waiting
                        status_packet += self.serialCupDispenser.read(leftover_num)
                        if status_packet[6] & 0x01:
                            logger.info(f"boad{self.current_boad}'s coulumn{column} ejecting now...")
                            time.sleep(4)  # 컵 사출되는데 걸리는 시간
                    '''
            except:
                pass

    def IsDispenserFilled(self,b10):
        # b10 : 0,1 = 1번보드(hot) / 2,3 = 2번보드(ice)
        with self.context.logger() as logger:
            logger.info(f"Called IsDispenserFilled")
        packet = b'\x02\x01\x40\x03\x44'  # stx len cmd etx bcc
        column = b10
        packet_check = False
        packet_len = self.packet_len
        worker = self.context.get_worker()

        while not worker.is_stopping():
            time.sleep(0.01)
            logger.info("reconnect to serialCupDispenser...")
            try:
                if(b10 == 0 or b10 == 1):
                    self.current_boad = 1
                    self.serialCupDispenser = serial.Serial("/dev/HOTBOARD",9600,timeout = 0.1,write_timeout=0.1)
                    break
                elif(b10 == 2 or b10 == 3):
                    self.current_boad = 2
                    self.serialCupDispenser = serial.Serial("/dev/ICEBOARD",9600,timeout = 0.1,write_timeout=0.1)
                    column -= 2
                    break
            except serial.SerialException as e:
                logger.info(f"{e}....request again...")
        if self.serialCupDispenser is None:
            logger.info("Serial connect Failed... Exit IsEispenserFilled Fnc")
            return
        while packet_check is not True and not worker.is_stopping():
            time.sleep(0.01)
            if packet_check == True:
                break
            # logger.info("Try read packet...")
            try:
                if packet_check == False:
                    self.serialCupDispenser.close()
                    if(b10 == 0 or b10 == 1):
                        self.serialCupDispenser = serial.Serial("/dev/HOTBOARD",9600,timeout = 0.1,write_timeout=0.1)
                    elif(b10 == 2 or b10 == 3):
                        self.serialCupDispenser = serial.Serial("/dev/ICEBOARD",9600,timeout = 0.1,write_timeout=0.1)
                    self.serialCupDispenser.write(packet)
                    self.serialCupDispenser.flush()
                timeout = time.time()+1
                while not worker.is_stopping() and (packet_check is not True):
                    time.sleep(0.01)
                    if self.serialCupDispenser.in_waiting:
                        time.sleep(0.05)
                        status_packet = self.serialCupDispenser.read(self.serialCupDispenser.in_waiting)
                        if self.serialCupDispenser.in_waiting:
                            leftover_num = self.serialCupDispenser.in_waiting
                            status_packet += self.serialCupDispenser.read(leftover_num)
                        if len(status_packet) == packet_len:
                            if status_packet[8] & (1 << (column)):
                                logger.info(f"boad{self.current_boad} Column {column} is Filled")
                                return True
                            elif ~status_packet[8] & (1 << (column)):
                                logger.info(f"boad{self.current_boad} Column {column} is Empty")
                                return False
                            packet_check = True
                        break
                    if time.time() > timeout:
                        logger.info("time out with in_waiting... read request again...")
                        break
            except:
                logger.info("read packet failed... try again.....")

    def IsEjectionFinished(self,b10):
        # b10 : 0,1 = 1번보드(hot) / 2,3 = 2번보드(ice)
        with self.context.logger() as logger:
            logger.info(f"Called IsEjectionFinished")
        packet = b'\x02\x01\x40\x03\x44'  # stx len cmd etx bcc
        column = b10
        worker = self.context.get_worker()
        packet_len = self.packet_len
        packet_check = False
        while not worker.is_stopping():
            time.sleep(0.01)
            try:
                if(b10 == 0 or b10 == 1):
                    self.current_boad = 1
                    self.serialCupDispenser = serial.Serial("/dev/HOTBOARD",9600,timeout = 0.1,write_timeout=0.1)
                    break
                elif(b10 == 2 or b10 == 3):
                    self.current_boad = 2
                    self.serialCupDispenser = serial.Serial("/dev/ICEBOARD",9600,timeout = 0.1,write_timeout=0.1)
                    column -= 2
                    break
            except serial.SerialException as e:
                logger.info(f"{e}.... request agian...")
        if self.serialCupDispenser is None:
            logger.info("Serial connect Failed... Exit isEjectionFinished Fnc")
            return
        while packet_check is not True and not worker.is_stopping():
            time.sleep(0.01)
            if packet_check == True:
                break
            # logger.info("Try read packet...")
            try:
                if packet_check == False:
                    self.serialCupDispenser.write(packet)
                    self.serialCupDispenser.flush()
                timeout = time.time()+1
                while not worker.is_stopping() and (packet_check is not True):
                    if self.serialCupDispenser.in_waiting:
                        time.sleep(0.05)
                        status_packet = self.serialCupDispenser.read(self.serialCupDispenser.in_waiting)
                        if self.serialCupDispenser.in_waiting:
                            leftover_num = self.serialCupDispenser.in_waiting
                            status_packet += self.serialCupDispenser.read(leftover_num)
                        if len(status_packet) == packet_len:
                            if status_packet[6] & 0x01:
                                logger.info(f"[Ejection] boad{self.current_boad} Column {column}, b10 {b10} eject complete")
                                packet_check = True
                                return True
                            elif status_packet[6] & 0x10:
                                logger.info(f"[Ejcetion] boad{self.current_boad} Column {column}, b10 {b10} eject not complete")
                        break  
                    if time.time() > timeout:
                        logger.info("time out with in_waiting... read request again...")
            except:
                logger.info("read packet failed... try again.....")
