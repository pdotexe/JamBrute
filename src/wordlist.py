from colorama import Fore




class Wordlist:

    def __init__(self):
        self.passwords: list[str] = [] #holds passwords
        

    def open_wordlist(self) -> list[str]:
        with open("txt/rockyou.txt", 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    self.passwords.append(stripped_line)
        print(Fore.GREEN + f"Loaded {len(self.passwords)} passwords from rockyou.txt")
        if not self.passwords: 
            print(Fore.RED + "No passwords to try. Exiting.")
            exit(1)
        return self.passwords


    
        
        
