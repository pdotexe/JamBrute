<img width="554" height="300" alt="pngfind com-jam-png-1507369" src="https://github.com/user-attachments/assets/320be265-b869-4a21-9e5f-c64da92cd09d" />

JamBrute is a basic online password cracking utility for [Animal Jam Classic](classic.animaljam.com), which works by sending automated HTTP requests to the server for login attempts. This utility is written with the help of the python [requests](pypi.org/project/requests/) and [threading](docs.python.org/3/library/threading.html) modules.


### Details
* __Simple to use__: Simple command-line usage
* __Multithreading__: Supports multiple threads to simultaneously submit multiple requests
* __Proxychains__: Optional rotating proxies to maintain anonymity and bypass rate limiting


### Installation
Ensure Python
To get started, clone the repository
```
git clone https://github.com/pdotexe/JamBrute.git
```
Install dependencies
```
pip install -r requirements.txt
```
Change directory 
```
cd JamBrute 
```
Run the utility
```
python start.py -p <proxy> -w <wordlist> -u <username> -t <threads>


Manual:
-p: Path to proxies.txt file ( default provided, may be skipped
-w: Path to wordlist file ( default provided, may be skipped )
-u: Target username
-t: Number of thread workers ( required )
```


### Notes
* Server overload (HTTP 502) is a known issue with AJC servers. To combat this, lower the amount of thread workers, and preferably use proxies before running this script.
* Using no proxies is highly impracticle and will likely work against you
* This tool is a working proof of concept and not intended for malicious use
  






