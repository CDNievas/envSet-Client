from colorama import init, Fore
import strmsg
from getpass import getpass

from Connection import Connection, ConnectionException

def handleMenu(inp):
    inp = inp.split(" ")
    comm = inp[0]

    if(comm == "login"):
        login(inp)
    elif (comm == "register"):
        register(inp)
    elif (comm == "envpush"):
        envpush(inp)
    elif (comm == "envdel"):
        envdel(inp)
    elif (comm == "envlist"):
        envlist()
    elif (comm == "envset"):
        envset(inp)
    elif (comm == "envprint"):
        envprint(inp)
    elif (comm == "logout"):
        logout()
    elif (comm == "help"):
        help()
    elif (comm == "exit"):
        exit()

def login(inp):

    if(len(inp) != 2):
        print(Fore.RED + strmsg.argsError + Fore.RESET)
    else:
        user = inp[1]
        passwd = getpass(">> Password: ")
        try:
            Connection.getInstance().login(user,passwd)
        except ConnectionException:
            print(Fore.RED + strmsg.connError + Fore.RESET)

def register(inp):

    if(len(inp) != 2):
        print(Fore.RED + strmsg.argsError + Fore.RESET)
    else:
        user = inp[1]
        passwd = getpass(">> Password: ")
        passwd2 = getpass(">> Re-Passsword: ")

        if(passwd != passwd2):
            print(Fore.RED + strmsg.passError + Fore.RESET)
        else:
            try:
                Connection.getInstance().register(user,passwd)
            except ConnectionException:
                print(Fore.RED + strmsg.connError + Fore.RESET)

def logout():
    Connection.getInstance().logout()

def envpush(inp):
    if(len(inp) < 3):
        print(Fore.RED + strmsg.argsError + Fore.RESET)
    else:
        envName = inp[1]
        envDesc = " ".join(inp[2:])
        envValue = getpass(">> Env var value: ")
        
        try:
            Connection.getInstance().envpush(envName,envValue,envDesc)
        except ConnectionException:
            print(Fore.RED + strmsg.connError + Fore.RESET)

def envdel(inp):
    if(len(inp) != 2):
        print(Fore.RED + strmsg.argsError + Fore.RESET)
    else:
        envName = inp[1]     
        try:
            Connection.getInstance().envdel(envName)
        except ConnectionException:
            print(Fore.RED + strmsg.connError + Fore.RESET)

def envlist():
    Connection.getInstance().envlist()

def envset(inp):
    if(len(inp) != 2):
        print(Fore.RED + strmsg.argsError + Fore.RESET)
    else:
        envName = inp[1]
        
        try:
            Connection.getInstance().envset(envName)
        except ConnectionException:
            print(Fore.RED + strmsg.connError + Fore.RESET)

def envprint(inp):
    if(len(inp) != 2):
        print(Fore.RED + strmsg.argsError + Fore.RESET)
    else:
        envName = inp[1]
        
        try:
            Connection.getInstance().envprint(envName)
        except ConnectionException:
            print(Fore.RED + strmsg.connError + Fore.RESET)

def help():
    print(strmsg.menu)