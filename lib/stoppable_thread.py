from threading import (Thread, Event)

class StoppableThread(Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = Event()
        self.__return_value = None

    def stop(self):
        self._stop_event.set()

    def set_return_value(self, return_value):
        self.__return_value = return_value
    
    def get_return_value(self):
        return self.__return_value

    def stopped(self):
        return self._stop_event.is_set()