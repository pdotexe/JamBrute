import argparse
import json


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--proxy", type=str, help="Path to proxy file", default="txt/proxies.txt", required=False)
    parser.add_argument("-w", "--wordlist", type=str, help="Path to wordlist file", default="txt/rockyou.txt", required=False)
    parser.add_argument("-u", "--username", type=str, help="Target player username", required=True)
    parser.add_argument("-t", "--threads", type=int, help="Number of concurrent threads", default=4, required=False)
    parser.add_argument("-e", "--endpoint", type=str, help="Target endpoint", required=True)
    parser.add_argument("-H", "--headers", type=json.loads,help="request headers (e.g \'{"User-Agent": "Bot"}\')", required=True)
    return parser.parse_args()