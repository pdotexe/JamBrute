


# About
## -----------------
JamBrute is a Proof-of-Concept (PoC) bruteforce utility built for Animal Jam Classic. It is designed utilizing the python requests and threading library against the authentication endpoint of the server to automate login attempts with wordlist of commonly used passwords.



# Features
## -----------------
- Proxy support
- Configurable thread-count
- Large default wordlist



# Installation
## ------------------

Clone repository and install dependencies:
```
git clone jambrute.git
cd jambrute
pip install -r requirements.txt

```

Run application:

```
python start.py -p <proxy file> -w <wordlist file> -u <username> -t <thread count>
```
* -p is not required, but highly recommended.
* use /txt/<wordlist_name>.txt format for -w flag 


# Notes
## ------------------

* This utility is not intended for malicious use. 
* It is highly impractical to not use proxies, as the server implements rate-limits per IP address and may return a HTTP 502 server error.
* Do not use too many threads at once, as this may exhaust memory.