from colorama import Fore
import requests


from Exceptions import ConnectionException
from VarSetter import VarSetter
import strmsg

class Connection():

    url = None
    __instance = None
    token = None

    @staticmethod
    def getInstance(_url=None):
        if Connection.__instance == None:
            Connection(_url)
        return Connection.__instance


    def testConn(self):
        try:
            requests.get(self.url + "/api/ping/")
        
        except requests.exceptions.RequestException as e:
            raise ConnectionException(e)


    def login(self, user, passwd):
        
        try:
            payload = {"user":user, "pass":passwd}
            r = requests.get(self.url + "/api/auth/",payload)
            r = r.json()
            if(r["success"]):
                print(Fore.GREEN + r["msg"] + Fore.RESET)
                self.token = r["token"]
            else:
                print(Fore.RED + r["msg"] + Fore.RESET)
        
        except requests.exceptions.RequestException as e:
            raise ConnectionException(e)
    

    def register(self, user, passwd):

        try:
            payload = {"user":user, "pass":passwd}
            r = requests.post(self.url + "/api/auth/",payload)
            r = r.json()
            if(r["success"]):
                print(Fore.GREEN + r["msg"] + Fore.RESET)
                self.token = r["token"]
            else:
                print(Fore.RED + r["msg"] + Fore.RESET)
        except requests.exceptions.RequestException as e:
            raise ConnectionException(e)


    def logout(self):
        if(self.token == None):
            print(Fore.RED + strmsg.noSession + Fore.RESET)
        else:
            self.token = None
            print(Fore.GREEN + strmsg.logoutOk + Fore.RESET)


    def envset(self,envName,envValue,envDesc):
        if(self.token == None):
            print(Fore.RED + strmsg.noSession + Fore.RESET)
        else:
            
            try:

                headers = {"Authorization": self.token}
                payload = {"name":envName, "desc":envDesc, "value":envValue}
                r = requests.post(self.url + "/api/envs/",payload,headers=headers)
                r = r.json()

                if(r["success"]):
                    print(Fore.GREEN + r["msg"] + Fore.RESET)
                else:
                    print(Fore.RED + r["msg"] + Fore.RESET)

            except requests.exceptions.RequestException as e:
                raise ConnectionException(e)
    

    def envlist(self):
        if(self.token == None):
            print(Fore.RED + strmsg.noSession + Fore.RESET)
        else:
            try:

                headers = {"Authorization": self.token}
                r = requests.get(self.url + "/api/envs/",headers=headers)
                r = r.json()

                if(r["success"]):
                    envs = r["envs"]
                    if(len(envs) == 0):
                        print(Fore.YELLOW + strmsg.noEnvVars + Fore.RESET)
                    else:
                        for env in envs:
                            print(env["name"] + ": " + env["desc"])

                else:
                    print(Fore.RED + r["msg"] + Fore.RESET)

            except requests.exceptions.RequestException as e:
                raise ConnectionException(e)


    def envget(self, envName):
        if(self.token == None):
            print(Fore.RED + strmsg.noSession + Fore.RESET)
        else:
            try:
                headers = {"Authorization": self.token}
                r = requests.get(self.url + "/api/envs/" + envName,headers=headers)
                r = r.json()

                if(r["success"]):
                    
                    VarSetter.getInstance().setVar(envName,r["value"],r["desc"])
                    
                else:
                    print(Fore.RED + r["msg"] + Fore.RESET)

            except requests.exceptions.RequestException as e:
                raise ConnectionException(e)


    def __init__(self, _url=None):
        if Connection.__instance != None:
            raise Exception("Singleton class")
        else:
            Connection.url = _url
            self.testConn()
            Connection.__instance = self
