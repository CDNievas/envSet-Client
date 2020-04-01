from colorama import Fore

from handlers import handleMenu
import strmsg

def welcome():
    print(Fore.GREEN + strmsg.logo)
    print(Fore.YELLOW + strmsg.by)

def startMenu():
    print(Fore.RESET)
    print(strmsg.menu)
    while(True):
        inp = input(">> ")
        handleMenu(inp)

    