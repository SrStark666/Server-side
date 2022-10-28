from colorama import Fore, init
from time import sleep


init(convert=True)
with open("database\log.txt", "r+") as reg:
    for i in reg.readlines():
        print(f"{Fore.GREEN}{i}{Fore.RESET}")
        sleep(3)