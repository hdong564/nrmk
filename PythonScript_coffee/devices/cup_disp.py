from devices.ice_disp import IceDispArgs
from examples.sample_device1 import SampleDevice1, CupDispArgs
import os,sys
from datetime import datetime as dt

from devices.kiosk import Coffee
from logics.recipe.event_args import MainEventArgs, PreparedDoneArgs
from devices import device
from context import Context
from events.event_args import EventArgs
from events.scheduler import Job
from events.worker import Worker
import serial,time

def _serial_comm(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        is_hot = args[1]
        result = None
        worker = self.context.get_worker()
        while not worker.is_stopping():
            try:
                conn = self._serial_hot if is_hot else self._serial_ice
                if conn is None:
                    if is_hot:
                        self._serial_hot = self._create_serial(is_hot)
                    else:
                        self._serial_ice = self._create_serial(is_hot)
                else:
                    if len(args) > 3:
                        result = func(self, is_hot, conn, *(args[3:]), **kwargs)
                    else:
                        result = func(self, is_hot, conn, *[], **kwargs)
                    break
                
            except Exception as err:
                with self.context.logger() as logger:
                    logger.exception("Cup dispenser Error.")
                try:
                    if is_hot:
                        if self._serial_hot.isOpen():
                            self._serial_hot.close()
                        self._serial_hot = None
                    else:
                        if self._serial_ice.isOpen():
                            self._serial_ice.close()
                        self._serial_ice = None
                except Exception as err:
                    if is_hot:
                        self._serial_hot = None
                    else:
                        self._serial_ice = None

            time.sleep(0.1)
        return result
    return wrapper

class CupDispenser(device.BaseDevice):
    def __init__(self) -> None:
        super().__init__()
        self.context: Context = None
        self._baudrate = 9600
        self._timeout_conn = 1
        self._timeout_write = 0.2
        self._serial_hot: serial.Serial = None
        self._serial_ice: serial.Serial = None
        self.packet_len = 11

    @classmethod
    def get_device_name(cls) -> str:
        return "CupDispenser"

    def on_create(self, context: Context):
        self.context = context
        config = self.context.get_config()
        self.packet_len = config["cup_disp_packet_len"]

        self._serial_hot: serial.Serial = self._create_serial(is_hot=True)
        self._serial_ice: serial.Serial = self._create_serial(is_hot=False)

        context.get_scheduler().add_event_listener(MainEventArgs, self.event_listener) #주문 입력 이벤트 받

    def on_dispose(self):
        if isinstance(self._serial_hot, serial.Serial) and self._serial_hot.isOpen():
            self._serial_hot.close()
            self._serial_hot = None
        if isinstance(self._serial_ice, serial.Serial) and self._serial_ice.isOpen():
            self._serial_ice.close()
            self._serial_ice = None

        self.context.get_scheduler().remove_event_listener(self.event_listener)
    
    def _create_serial(self, is_hot: bool) -> serial.Serial:
        return serial.Serial(
            "/dev/HOTBOARD",
            self._baudrate,
            timeout=self._timeout_conn,
            write_timeout=self._timeout_write
        ) if is_hot else \
            serial.Serial(
                "/dev/ICEBOARD",
                self._baudrate,
                timeout=self._timeout_conn,
                write_timeout=self._timeout_write
        )
    
    def event_listener(self, sender: None, args: MainEventArgs):
        if args.get_event_code() != MainEventArgs.EVENT_CODE_NEW_COFFEE:
            return
        with self.context.logger() as logger:
            logger.info(f"Event occurred! Event Type: {args.get_event_code()}, Args: {args.get_arguments()}")
        
        # flag 0 1 = hot / 2 3 = ice
        coffee: Coffee = args.get_arguments()
        is_hot = not coffee.is_iced()

        shm = self.context.acquire_shm()
        shm.write_direct_variable("B", 20, coffee.get_cm_index()) # 이동해야하는 컵 위치 = 핫 1 번 설정
        self.context.release_shm()

        worker = self.context.get_worker()
        
        cup_idx = -1
        for _ in range(5):
            if worker.is_stopping():
                return
            cup_idx = self.get_filled_cup_index(is_hot, None)
            if cup_idx != -1:
                break
            with self.context.logger() as logger:
                logger.info(f"Not found filled cup slot. Now Re-trying... is_hot: {is_hot}")
            time.sleep(0.1)
        if cup_idx == -1:
            raise RuntimeError(f"Cup is empty. is_hot: {is_hot}")
        
        shm = self.context.acquire_shm()
        shm.write_direct_variable("B", 10, cup_idx + (0 if is_hot else 2)) # 이동해야하는 컵 위치 = 핫 1 번 설정
        shm.write_direct_variable("B", 0, 1) #포터필터 머신에 끼우는 이동명령
        self.context.release_shm()

        while not worker.is_stopping():
            shm = self.context.acquire_shm()
            move = shm.read_direct_variable('B',0)
            self.context.release_shm()
            if(move == 0):
                break
            time.sleep(0.02)
        if worker.is_stopping():
            return
        move = -1
        while not worker.is_stopping():
            shm = self.context.acquire_shm()
            shm.write_direct_variable("B", 0, 10) # 컵 잡으러 이동
            self.context.release_shm()
            while not worker.is_stopping():
                shm = self.context.acquire_shm()
                move = shm.read_direct_variable('B',0)
                self.context.release_shm()
                if(move == 0):
                    break
                time.sleep(0.02)
            is_extracted = False
            for _ in range(5):
                if worker.is_stopping():
                    return
                self.extract_cup(is_hot, None, cup_idx)
                for _ in range(5):
                    if worker.is_stopping():
                        return
                    is_extracted = self.is_extracted(is_hot, None)
                    if is_extracted:
                        break
                    time.sleep(0.2)
                if is_extracted:
                    break
                time.sleep(0.5)
            shm = self.context.acquire_shm()
            shm.write_direct_variable("B",0,20) 
            self.context.release_shm()   
            while not worker.is_stopping():
                shm = self.context.acquire_shm()
                move = shm.read_direct_variable('B',0)
                self.context.release_shm()
                if(move == 21 or move == 0):
                    break
                time.sleep(0.02)
            shm = self.context.acquire_shm()
            move = shm.read_direct_variable('B',0)
            self.context.release_shm()
            time.sleep(0.02)
            if(move == 0):
                break
      
        self.context.get_scheduler().add_schedule(Job(None,PreparedDoneArgs(0,0)))
    
    def _read_data(self, conn: serial.Serial, packet_len: int, timeout=1) -> bytearray:
        worker = self.context.get_worker()
        result = bytearray()
        prev_time = dt.now()
        while not worker.is_stopping():
            if (dt.now() - prev_time).total_seconds() > timeout:
                return None
            left_size = packet_len - len(result)
            in_waiting = conn.in_waiting
            if left_size == 0:
                break
            elif conn.in_waiting:
                diff = in_waiting - left_size
                size = left_size if diff >= 0 else in_waiting
                result.extend(bytearray(conn.read(size=size)))
            time.sleep(0.02)
        return result

    @_serial_comm
    def get_filled_cup_index(self, is_hot: bool, conn: serial.Serial):
        packet = b'\x02\x01\x40\x03\x44'  # stx len cmd etx bcc
        worker = self.context.get_worker()
        packet_len = self.packet_len

        cup_index = -1
        conn.write(packet)
        conn.flush()
        while not worker.is_stopping():
            result = self._read_data(conn=conn, packet_len=packet_len, timeout=self._timeout_conn)
            if result is not None:
                cup_flag = result[8]
                if cup_flag & 1:
                    cup_index = 0
                elif cup_flag & 2:
                    cup_index = 1
                break
            else:
                conn.write(packet)
                conn.flush()
            time.sleep(0.5)
        return cup_index
    
    @_serial_comm
    def extract_cup(self, is_hot: bool, conn: serial.Serial, index: int):
        packet = bytearray(b'\x02\x03\x41\x00\x00\x03\x00')
        
        packet[3] = index + 1
        packet[4] = 1 # the number of cups
        for i in range(1, 6):  # packet[6] is checksum byte
            packet[6] += packet[i]
        packet[6] %= 256

        cup_index = -1
        conn.write(packet)
        conn.flush()
        time.sleep(0.1)
        
    @_serial_comm
    def is_extracted(self, is_hot: bool, conn: serial.Serial):
        # Dispensing finish check
        packet = b'\x02\x01\x40\x03\x44'  # stx len cmd etx bcc
        packet_len = self.packet_len
        worker = self.context.get_worker()

        while not worker.is_stopping():
            result = self._read_data(conn=conn, packet_len=packet_len, timeout=self._timeout_conn)
            if result is not None:
                cup_flag = result[6]
                if cup_flag & 0x01:
                    return True
                elif cup_flag & 0x10:
                    return False
            else:
                conn.write(packet)
                conn.flush()
            time.sleep(0.5)
