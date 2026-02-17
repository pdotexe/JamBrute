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
from src.cli import parse_arguments


def start() -> None:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    colorama.init(autoreset = True)
    
    args = parse_arguments()
    
    # ascii banner
    text = "JamBrute"
    ascii_art = pyfiglet.figlet_format(text, font="standard", width = 150)
    print(colored(ascii_art, 'red'))

    
    # store objects in variables
    login = LoginRequests()
    wordlist = Wordlist(wordlist_file=args.wordlist)
    proxy_list = ProxyLoader(proxy_file=args.proxy)
    proxy_list.load_proxies() 
    wordlist.open_wordlist()
    
    # execute threads
    
    with ThreadPoolExecutor(max_workers = args.threads) as worker:
        for password in wordlist.passwords: #iterate through the wordlist array of passwords
            proxy = random.choice(proxy_list.proxy_list) if proxy_list.proxy_list else None # random selection from list
            worker.submit(login.send_login, password, proxy) # submit the threads to executor with login method and password +proxy parameters
    



if __name__ == "__main__":
    start() # start call
    