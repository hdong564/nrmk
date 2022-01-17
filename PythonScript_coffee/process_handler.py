from datetime import timedelta
from context import Context
from devices.ice_disp import IceDispenser
from devices.cup_disp import CupDispenser
from devices.barcode_reader import BarcodeReader
from devices.kiosk import Kiosk
from events.scheduler import Scheduler
import events, time, Config, os
from logging import Logger
from indy_utils.indy_shm import IndyShmCommand

from logics import main_logic as logic

class ProcessHandler:
    _worker = None

    def __init__(self) -> None:
        self._shm: IndyShmCommand = None
        self._worker = events.Worker(thread_interval=0.1)
        self._worker.set_callbacks(
            prerun=self.__prepare__,
            main_loop=self.__main__,
            postrun=self.__dispose__
        )
        self._config = Config.load_config()
        self._context = Context.get_instance()
        # self._context.set_indy_shm_config(sync_mode=False, joint_dof=self._config[Config.CONFIG_KEY_ROBOT_DOF])
        self._context.set_config(self._config)
        self._context.set_scheduler(Scheduler.get_instance())

        self._system_logger, self._system_file_handler, self._system_stream_handler = self._worker.create_logger("System")
        self._context_logger, self._context_file_handler, self._context_stream_handler = self._worker.create_logger("Context")
        self._system_logger.info(f"Configurations_\n{self._config}")

        self._device_list = [
            Kiosk,
            IceDispenser,
            CupDispenser,
            BarcodeReader
        ]
    
    def __prepare__(self, worker: events.Worker, logger: Logger):
        logger.info(f"Preparing program...")
        self._context.set_indy_shm(self._shm)
        self._context.get_scheduler().init()
        self._context.set_logger(self._context_logger)
        self._context.set_worker(worker)
        self._context.set_root_path(os.path.dirname(os.path.realpath(__file__)))
        new_list = []
        for dev_class in self._device_list:
            try:
                logger.info(f"initializing device '{dev_class}'...")

                if dev_class.is_singleton():
                    dev = dev_class.get_instance()
                else:
                    dev = dev_class()
                logger.debug(f"Called on_create of device '{dev_class}'")
                dev.on_create(context=self._context)
                logger.debug(f"on_create of device '{dev_class}' done.")
                new_list.append(dev)

                logger.info(f"Successfully initialized. Device name: {dev.get_device_name()}")
            except:
                logger.exception(f"Failed to initialize with device '{dev_class}'")
                self._device_list = new_list
                worker.stop(0)
        self._device_list = new_list

        self._context.clear_devices()
        for dev in self._device_list:
            self._context.add_device(dev)

        logic.init(self._context)
        logger.info(f"Preparing program...Done.")
    
    def __main__(self, worker: events.Worker, deltatime, logger: Logger) -> bool or None:
        return logic.main_loop(worker, deltatime, logger)

    def __dispose__(self, worker: events.Worker, logger: Logger) -> None:
        logger.info(f"Shutting down...")
        logic.dispose()
        for dev in self._device_list:
            dev_name = dev.get_device_name()
            try:
                logger.info(f"Disposing device '{dev.get_device_name()}'...")
                dev.on_dispose()
                logger.info(f"Successfully disposed device '{dev_name}'")
            except:
                logger.exception(f"Failed to disposing device '{dev_name}'")
        self._worker.dispose_logger(self._context_logger, self._context_file_handler, self._context_stream_handler)
        self._worker.dispose_logger(self._system_logger, self._system_file_handler, self._system_stream_handler)
        self._context.get_scheduler().dispose()
        logger.info(f"Shutting down...Done.")
    
    def run(self, shm: IndyShmCommand) -> None:
        self._shm = shm
        self._system_logger.info("Program started.")
        self._worker.start()
        while self._worker.is_running():
            time.sleep(0.5)
        self._system_logger.info("Program finished.")
    
    def terminate(self) -> None:
        self._system_logger.info("Program terminating was requested.")
        self._worker.stop()
        Config.save_config(self._config)
