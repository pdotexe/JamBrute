


# About
## -----------------
FastBullet is a minimalistic credential testing utility for authentication endpoints. It is designed utilizing the python requests and threading library against the authentication endpoint of any server to automate login attempts with user provided wordlist of commonly used passwords.



# Features
## -----------------
- Proxy support
- Configurable thread-count
- Great for testing weak or newly-created auth endpoints.



# Installation
## ------------------

Clone repository and install dependencies:
```
git clone fastbullet.git
cd fastbullet
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
* It is highly impractical to not use proxies, as servers implement IP or device fingerprint based ratelimits.
* Do not use too many threads at once, as this may exhaust memory. Python's GIL is also not the best Mutex, so be mindful of thread counts.
