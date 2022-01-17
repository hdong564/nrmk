from .event_args import EventArgs
from typing import Callable, Any, ClassVar

EventCallback: Callable[[Any, EventArgs], bool] = lambda sender, args: True

class EventManager:
    def __init__(self):
        self._event_listeners = {}
        
    def add_event_listener(self, event_arg_class: property, event_listener: EventCallback):
        if event_arg_class not in self._event_listeners.keys():
            self._event_listeners[event_arg_class] = []
        self._event_listeners[event_arg_class].append(event_listener)
    
    def remove_event_listener_on_event(self, event_arg_class: property, event_listener: EventCallback) -> bool:
        if event_arg_class not in self._event_listeners.keys():
            return False
        listeners = self._event_listeners[event_arg_class]
        for idx, listener in enumerate(listeners):
            if listener is event_listener:
                del listeners[idx]
                return True
        return False
    
    def remove_event_listener(self, event_listener: EventCallback) -> bool:
        removed = False
        for key in self._event_listeners.keys():
            if self.remove_event_listener_on_event(key, event_listener):
                removed = True
                break
        return removed
    
    def raise_event(self, sender: Any, event_args: EventArgs):
        if event_args.__class__ not in self._event_listeners.keys():
            return
        for listener in self._event_listeners[event_args.__class__]:
            if listener(sender, event_args) is False:
                break

if __name__ == "__main__":
    def test(sender, event_args: EventArgs):
        print("Event Code:", event_args.get_event_code())
        print("Event Args:", event_args.get_arguments())
        event_args.get_arguments()["TEST"] += 1

    a = EventManager()
    a.add_event_listener(EventArgs, test)
    a.add_event_listener(EventArgs, test)
    a.raise_event(None, EventArgs(1, {"TEST": 1}))
