import argparse


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--proxy", type=str, help="Path to proxy file", default="txt/proxies.txt", required=False)
    parser.add_argument("-w", "--wordlist", type=str, help="Path to wordlist file", default="txt/rockyou.txt", required=False)
    parser.add_argument("-u", "--username", type=str, help="Target player username", required=True)
    parser.add_argument("-t", "--threads", type=int, help="Number of concurrent threads", default=4, required=False)
    return parser.parse_args()