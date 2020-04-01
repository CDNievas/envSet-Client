from colorama import init, Fore

from menus import welcome, startMenu
from Connection import Connection, ConnectionException
import strmsg

# Init colorama to print colors on all platforms
init()

# Welcome message
welcome()

# Check connection
try:
    Connection.getInstance("http://localhost:8080")
    print(Fore.GREEN + strmsg.connOk + Fore.RESET)
except ConnectionException as e:
    print(Fore.RED + strmsg.connError + "\n" + str(e) + Fore.RESET)
    exit()

# Start menu
startMenu()