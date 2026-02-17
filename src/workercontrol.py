import threading
import time
from colorama import Fore
class Threading:
    def __init__(self):
        self.print_lock = threading.Lock() # keeps workers from printing at the same time
        self.pause_event = threading.Event() # the event occurring for pausing all workers in the threads
        self.repeated_lock = threading.Lock() # the lock occurring for repeated 502 responses'
        self.repeated_502 = 0
    def pause_workers(self) -> None:
        with self.repeated_lock:
            if self.repeated_502 < 3:
                return
            self.repeated_502 = 0
        with self.print_lock:
            print(Fore.YELLOW + f"All workers paused for a few seconds...")
        self.pause_event.set()
        time.sleep(6.7) #xd
        self.pause_event.clear()