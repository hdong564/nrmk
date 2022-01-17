from datetime import datetime as dt, timedelta
from .worker import Worker
from .event_args import EventArgs
from .event_manager import *
from typing import Any
import logging, queue, threading

class Job:
    # The unit of duration is one second.
    def __init__(self, sender: Any, event_args: EventArgs, duration: float=0, is_repeatable: bool=False) -> None:
        self.Sender = sender
        self.EventArgs = event_args
        self.Duration = duration
        self.Repeatable = is_repeatable
        self.__duration = duration
    
    def descend_duration(self, duration: float) -> bool:
        self.__duration -= duration
        if self.__duration < 0:
            return True
        
    def reset_duration(self):
        self.__duration = self.Duration

class Scheduler:
    
    def __init__(self) -> None:
        self._worker = Worker()
        self._worker.add_co_routine(self._co_routine)
        self._worker.set_main_loop_callback(self.__scheduler__)
        self._worker.set_main_loop_logger_name("Scheduler")
        self._worker.set_coroutine_logger_name("Scheduler-coroutine")

        self._event_manager = EventManager()

        self._schedules = []
        self._schedules_lock = threading.Lock()
        self._performable_jobs = queue.Queue()
    
    def init(self):
        self._worker.start()
    
    def dispose(self):
        self._worker.stop()
    
    @classmethod
    def __get_instance(cls):
        return cls.__instance

    @classmethod
    def get_instance(cls):
        cls.__instance = Scheduler()
        cls.get_instance = cls.__get_instance
        return cls.__instance
    
    def _co_routine(self, worker: Worker, deltatime: timedelta, logger: logging.Logger):
        while not self._performable_jobs.empty():
            job = self._performable_jobs.get()
            self._event_manager.raise_event(job.Sender, job.EventArgs)

    def __scheduler__(self, worker: Worker, deltatime: timedelta, logger: logging.Logger):
        now = dt.now()
        removable = list()
        self._schedules_lock.acquire()
        for idx, job in enumerate(self._schedules):
            cur = dt.now() - now
            delta = (cur + deltatime).total_seconds()
            if job.descend_duration(delta):
                self._performable_jobs.put_nowait(job)
                if not job.Repeatable:
                    removable.append(idx)
                else:
                    job.reset_duration()
        
        removable.reverse()
        for idx in removable:
            del self._schedules[idx]
        self._schedules_lock.release()

    def get_event_manager(self) -> EventManager:
        return self._event_manager
    
    def add_event_listener(self, event_args_class: property, listener: EventCallback) -> 'Scheduler':
        self._event_manager.add_event_listener(event_arg_class=event_args_class, event_listener=listener)
        return self
    
    def remove_event_listener(self, listener: EventCallback) -> bool:
        return self._event_manager.remove_event_listener(listener)

    def add_schedule(self, job: Job) -> 'Scheduler':
        self._schedules_lock.acquire()
        self._schedules.append(job)
        self._schedules_lock.release()
        return self
    
    def remove_schedule(self, job: Job) -> 'Scheduler':
        self._schedules_lock.acquire()
        if job not in self._schedules:
            self._schedules_lock.release()
            return self
        idx = self._schedules.index(job)
        del self._schedules[idx]
        self._schedules_lock.release()
        return self
