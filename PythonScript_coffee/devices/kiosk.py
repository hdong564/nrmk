from Config import CONFIG_KEY_COFFEE_MAP
from datetime import datetime, timedelta
from events.scheduler import Job
from events.event_args import EventArgs
from logging import Logger
from events.worker import Worker
from context import Context
from .device import BaseDevice
import pymssql as sql
from pymssql import _mssql
import time
from threading import Lock

class Kiosk(BaseDevice):
    class OrderData:
        pass
from logics.coffee import Coffee

class KioskEventArgs(EventArgs):
    EVENT_CODE_NEW_DATA = 0b00000001


class Kiosk(BaseDevice):
    SQL_READ_NEW_DATA       = "SELECT TOP 1 * FROM TB_OrderJoin WHERE OJ_STATUS IS NULL ORDER BY OJ_NO ASC;"
    SQL_UPDATE_READ_DATA    = "UPDATE TB_OrderJoin SET OJ_STATUS='%d' WHERE PE_ID=%s AND OJ_NO=%s;"
    SQL_INITIALIZE_DATA     = "UPDATE TB_OrderJoin SET OJ_STATUS=NULL WHERE OJ_STATUS <> '3'"
    SQL_FINALIZE_DATA       = "UPDATE TB_OrderJoin SET OJ_STATUS=NULL WHERE OJ_STATUS <> '3'"

    class OrderData:
        ORDER_DATA_UNKNOWN          = 0
        ORDER_DATA_STATE_PREPARE    = 1
        ORDER_DATA_STATE_DONE       = 2
        ORDER_DATA_STATE_REMOVED    = 3

        PE_ID: str
        OJ_WAITNUM: str
        OJ_NO: int
        OJ_DATE: datetime
        OJ_PRCODE: str
        OJ_PRNAME: str
        OJ_STATUS: int
        OJ_BAN: str
        def __init__(self,
                pe_id: str,
                oj_waitnum: str,
                oj_no: int,
                oj_date: datetime,
                oj_prcode: str,
                oj_prname: str,
                oj_qty: int,
                oj_status: int,
                oj_ban: str) -> None:
            self.PE_ID = pe_id
            self.OJ_WAITNUM = oj_waitnum
            self.OJ_NO = oj_no
            self.OJ_DATE = oj_date
            self.OJ_PRCODE = oj_prcode
            self.OJ_PRNAME = oj_prname
            self.OJ_QTY = int(oj_qty)
            self.OJ_STATUS = oj_status if oj_status is not None else self.ORDER_DATA_UNKNOWN
            self.OJ_BAN = oj_ban
            self._remaining_coffee_cnt = self.OJ_QTY
            self._coffee_list = []
        
        def get_remaining_coffee_count(self) -> int:
            return self._remaining_coffee_cnt
        
        def decrease_remaining_coffee_count(self):
            self._remaining_coffee_cnt -= 1
        
        def append_new_coffee(self, coffee: Coffee):
            self._coffee_list.append(coffee)
        
        def get_coffee_list(self) -> list:
            return self._coffee_list

    def __init__(self) -> None:
        super().__init__()
        self.context: Context = None
        self._db_conn = None
        self._cm_slot: dict = None
        self._lift_slot: dict = None
        self._is_test_mode = False
        self._deltatime = 85
        self._total_deltattime = 0
        self._db_lock = Lock()

    @classmethod
    def get_device_name(cls) -> str:
        return "Kiosk"

    def _log(self, msg: str):
        with self.context.logger() as logger:
            logger.info(f"{self.get_device_name()} - {msg}")

    def on_create(self, context: Context) -> None:
        self.context = context
        self._is_test_mode = context.is_test_mode()
        # self._is_test_mode = True
        self._log("OnCreate")

        if self._is_test_mode:
            self._log("Now starting Kiosk with TEST mode.")
            context.get_worker().add_co_routine(self._co_routine)
            self._log("OnCreate Done.")
            return

        config = context.get_config()
        self._log(f"Trying to connect to Database - host: {config['db_host']}, db: {config['db_name']}.")
        try:
            self._db_conn = sql.connect(
                host=config['db_host'],
                database=config['db_name'],
                user=config['db_user'],
                password=config['db_pwd'],
                charset=config['db_charset'],
                as_dict=True,
                login_timeout=config['db_login_timeout'],
                timeout=config['db_timeout'],
                autocommit=True
            )
            cursor = self._db_conn.cursor()
            cursor.execute(Kiosk.SQL_INITIALIZE_DATA)
            cursor.close()
            self._log("Successfully connected to Database.")
            context.get_worker().add_co_routine(self._co_routine)
        except:
            self._log("Failed to connect to Database.")
            self.context.acquire_logger().exception("[Error Log]")
            self.context.release_logger()
            self._db_conn = None

        self._log("OnCreate Done.")

    def on_dispose(self) -> None:
        self._log("OnDispose")

        self.context.get_worker().remove_co_routine(self._co_routine)

        if not self._is_test_mode:
            self._log(f"Trying to disconnect to Database.")
            try:
                self._db_lock.acquire()
                if self._db_conn is not None:
                    cursor = self._db_conn.cursor()
                    cursor.execute(Kiosk.SQL_FINALIZE_DATA)
                    cursor.close()
                    self._db_conn.close()
                self._db_lock.release()
                self._log("Successfully disconnected to Database.")
            except:
                self._log("Failed to disconnect to Database.")
                self.context.acquire_logger().exception("[Error Log]")
                self.context.release_logger()

        self._log("OnDispose Done.")

    def _co_routine(self, worker: Worker, deltatime: timedelta, logger: Logger):
        if self._is_test_mode:
            from random import Random
            self._deltatime += deltatime.total_seconds()
            self._total_deltattime += deltatime.total_seconds()
            if self._deltatime > 90:
                coffee_index = Random().randint(0, 5)
                coffee_map: dict = self.context.get_config()[CONFIG_KEY_COFFEE_MAP]
                coffee_prcode = "00000001"
                for key in coffee_map.keys():
                    if coffee_map[key] == coffee_index:
                        coffee_prcode = key
                        break
                dummy_data = Kiosk.OrderData("2021100100010000", '1', 1, datetime.now(), coffee_prcode, "Test coffee", 1, Kiosk.OrderData.ORDER_DATA_STATE_PREPARE, '')
                self.context.get_scheduler().add_schedule(Job(self, KioskEventArgs(
                    KioskEventArgs.EVENT_CODE_NEW_DATA,
                    Coffee(self.context, dummy_data)
                )))
                self._deltatime = 0
            return

        self._db_lock.acquire()
        cursor = self._db_conn.cursor()
        cursor.execute(self.SQL_READ_NEW_DATA)
        rows = cursor.fetchall()
        cursor.close()
        self._db_lock.release()
        if len(rows) != 0:
            self.notify_new_coffee(rows[0])
    
    def update_order_state(self, order_data: 'Kiosk.OrderData', state):
        assert state in [
            Kiosk.OrderData.ORDER_DATA_STATE_PREPARE,
            Kiosk.OrderData.ORDER_DATA_STATE_DONE,
            Kiosk.OrderData.ORDER_DATA_STATE_REMOVED
            ], "Incorrect state data was given in 'update_order_state'."
        if not self._is_test_mode:
            trying_count = 5
            for _ in range(trying_count):
                try:
                    self._db_lock.acquire()
                    cursor = self._db_conn.cursor()
                    cursor.execute(self.SQL_UPDATE_READ_DATA, (state, order_data.PE_ID, order_data.OJ_NO))
                    cursor.close()
                    self._db_lock.release()
                    break
                except _mssql.MssqlDriverException:
                    with self.context.logger() as logger:
                        logger.exception("A MSSQLDriverException has been caught.")

                except _mssql.MssqlDatabaseException as e:
                    with self.context.logger() as logger:
                        logger.exception("A MSSQLDatabaseException has been caught.")
                        logger.error('Number = ',e.number)
                        logger.error('Severity = ',e.severity)
                        logger.error('State = ',e.state)
                        logger.error('Message = ',e.message)
                except sql.OperationalError:
                    with self.context.logger() as logger:
                        logger.exception("An unknown error has been caught.")
                except:
                    with self.context.logger() as logger:
                        logger.exception("An unknown error has been caught.")
                time.sleep(0.1)

        order_data.OJ_STATUS = state
    
    def notify_new_coffee(self, data_row):
        data = Kiosk.OrderData(
            data_row["PE_ID"],
            data_row["OJ_WAITNUM"],
            data_row["OJ_NO"],
            data_row["OJ_DATE"],
            data_row["OJ_PRCODE"],
            data_row["OJ_PRNAME"],
            data_row["OJ_QTY"],
            Kiosk.OrderData.ORDER_DATA_STATE_PREPARE,
            data_row["OJ_BAN"],
        )
        self.update_order_state(data, Kiosk.OrderData.ORDER_DATA_STATE_PREPARE)

        scheduler = self.context.get_scheduler()
        for _ in range(data.get_remaining_coffee_count()):
            scheduler.add_schedule(Job(self, KioskEventArgs(
                KioskEventArgs.EVENT_CODE_NEW_DATA,
                Coffee(self.context, data)
            )))
        