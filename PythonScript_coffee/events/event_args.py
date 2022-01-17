from typing import Any


class EventArgs:
    
    def __init__(self, event_code: int, args: Any):
        self._event_code = event_code
        self._args = args
    
    def get_event_code(self) -> int:
        return self._event_code
    
    def get_arguments(self) -> Any:
        return self._args
