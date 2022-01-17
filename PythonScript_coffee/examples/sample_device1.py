from datetime import timedelta
from logging import Logger
import time
from events.event_args import EventArgs
from events.scheduler import Job
from events.worker import Worker
# import os, sys
# sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../"))
from devices import device
import threading
from context import Context


class CupDispArgs(EventArgs):
    pass


class SampleEventArgs(EventArgs):
    pass


class SampleDevice1(device.BaseDevice):
    def __init__(self) -> None:
        super().__init__()
        self.context: Context = None
        self.loop_cnt = 0
        self._job_list = []

        self._is_running = False
        self._thread = None

    @classmethod
    def get_device_name(cls) -> str:
        return "SampleDevice1"

    def on_create(self, context: Context) -> None:
        self.context = context
        with context.logger() as logger:
            logger.info(f"{self.get_device_name()} - OnCreate")

        # context.get_worker().add_co_routine(self._co_routine) # add corutine예저

        scheduler = context.get_scheduler()
        self._job_list.append(
            Job(self, CupDispArgs(0, 0), 1, False))  # flag = 0
        # self._job_list.append(Job(self, SampleEventArgs(2, None), 2, is_repeatable=True))  -> 이벤트 추가 예제
        for job in self._job_list:
            scheduler.add_schedule(job)

    def _co_routine(self, worker: Worker, deltatime: timedelta, logger: Logger):
        pass
        # self.context.get_scheduler().add_schedule(Job(self, SampleEventArgs(3, self.loop_cnt)))

        # Shared memory example
        # shm = self.context.acquire_shm()
        # shm.write_direct_variable('B', 20, 1)
        # self.context.release_shm()

    def on_dispose(self) -> None:
        self.context.acquire_logger().info(
            f"{self.get_device_name()} - OnDispose")
        self.context.release_logger()

        scheduler = self.context.get_scheduler()
        for job in self._job_list:
            scheduler.remove_schedule(job)
        self._job_list.clear()
        if self._thread:
            self._is_running = False
            self._thread.join()

    def execute(self):
        self.context.acquire_logger().info(
            f"{self.get_device_name()} - Execute")
        self.context.release_logger()

    def execute_async(self) -> None:
        self.context.acquire_logger().info(
            f"{self.get_device_name()} - Execute_Async")
        self.context.release_logger()
