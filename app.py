from colorama import init, Fore

from menus import welcome, startMenu
from Connection import Connection, ConnectionException
from VarSetter import VarSetter, SoNoDetectedException
import strmsg

# Init colorama to print colors on all platforms
init()

# Welcome message
welcome()

# Check connection
try:
    VarSetter.getInstance()
    print(Fore.GREEN + strmsg.soDetected + Fore.RESET)
    Connection.getInstance("http://cdnapp.ddns.net:800")
    print(Fore.GREEN + strmsg.connOk + Fore.RESET)

except SoNoDetectedException:
    print(Fore.RED + strmsg.soNoDetected + Fore.RESET)
    exit()

except ConnectionException as e:
    print(Fore.RED + strmsg.connError + "\n" + str(e) + Fore.RESET)
    exit()

# Start menu
startMenu()
