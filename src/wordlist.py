from colorama import Fore
import gzip
import shutil
import os


project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
source_file = os.path.join(project_root, "txt", "rockyou.txt.gz")
destination_file = os.path.join(project_root, "txt", "rockyou.txt")



try:
    print(Fore.YELLOW + f"Unzipping {source_file} to {destination_file}...")
    with gzip.open(source_file, 'rb') as file_in:
        with open(destination_file, 'wb') as file_out:
            shutil.copyfileobj(file_in, file_out)
except FileNotFoundError:
    print(Fore.RED + f"Error: {source_file} not found.")
    exit(1)
except Exception as e:
    print(Fore.RED + f"Error: {e}")
    exit(1)

class Wordlist:

    def __init__(self):
        self.passwords: list[str] = [] #holds passwords
        

    def open_wordlist(self) -> list[str]:
        with open(destination_file, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    self.passwords.append(stripped_line)
        print(Fore.GREEN + f"Loaded {len(self.passwords)} passwords from rockyou.txt")
        if not self.passwords: 
            print(Fore.RED + "No passwords to try. Exiting.")
            exit(1)
        return self.passwords


    
        
        
