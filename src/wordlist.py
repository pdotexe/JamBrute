from colorama import Fore




class Wordlist:
    
    def __init__(self, wordlist_file: str = None):
        self.wordlist_file = wordlist_file or "txt/rockyou.txt"
        self.passwords: list[str] = [] #holds passwords
        

    def open_wordlist(self) -> list[str]:
        with open(self.wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    self.passwords.append(stripped_line)
        print(Fore.GREEN + f"Loaded {len(self.passwords)} passwords from {self.wordlist_file}")
        if not self.passwords: 
            print(Fore.RED + "No passwords to try. Exiting.")
            exit(1)
        return self.passwords


    
        
        
