import requests
from requests.exceptions import Timeout, RequestException
from colorama import Fore



class ProxyLoader:

    
    def __init__(self):
        self.proxy_list: list[str] = []
        self.test = "http://httpbin.org/status/200" # proxy test endpoint
    
    def load_proxies(self) -> list[str]:
        try:   
            with open("txt/proxies.txt", 'r') as p: 
                for l in p:
                    proxy = l.strip() # strip whitespace
                    if proxy:
                        try:
                            if not proxy.startswith("socks5://") and not proxy.startswith("http://") and not proxy.startswith("https://"):
                                proxy = f"socks5://{proxy}"
                            else:
                                print(Fore.RED + f'Proxy {proxy} is not a valid proxy protocol, skipping.')
                                continue
                            proxyresponse = requests.head(self.test, proxies={"http": proxy, "https": proxy}, timeout=2.5)
                            if proxyresponse.status_code in [200, 301, 302, 304, 405]: #http status check
                                self.proxy_list.append(proxy)
                                print(Fore.GREEN + f'Proxy {proxy} working with HTTP/{proxyresponse.status_code})')
                            else:
                                print(Fore.RED + f'Proxy {proxy} failed status check with code {proxyresponse.status_code}), skipping.')
                        except (Timeout, RequestException):
                            print(Fore.RED + f'Proxy {proxy} is timed out, skipping.')
            print(f"Loaded {len(self.proxy_list)} working proxies")
            return self.proxy_list
        except FileNotFoundError:
            print(Fore.YELLOW + f"Warning: proxies file not found. Proceeding without proxies.")
            return self.proxy_list
        except Exception as e:
            print(Fore.RED + f"Error loading proxies file: {e}")
            return self.proxy_list

        