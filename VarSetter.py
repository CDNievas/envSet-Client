
import platform
from colorama import Fore
from pathlib import Path

import strmsg
from Exceptions import SoNoDetectedException

class VarSetter():

    __instance = None
    aPlatform = None

    @staticmethod
    def getInstance():
        if VarSetter.__instance == None:
            VarSetter()
        return VarSetter.__instance

    def __init__(self):
        if VarSetter.__instance != None:
            raise Exception("Singleton class")
        else:

            strPlatform = platform.system()

            if(strPlatform == "Linux"):
                self.aPlatform = LinuxSetter()
            elif(strPlatform == "Windows"):
                self.aPlatform = WindowsSetter()
            elif(strPlatform == "Mac"):
                self.aPlatform == MacSetter()
            else:
                raise SoNoDetectedException
            VarSetter.__instance = self

    def setVar(self,envName, envValue,envDesc):
        self.aPlatform.setVar(envName,envValue,envDesc)

class WindowsSetter():

    def parseVar(self, envName, envValue):
        print("Windows")

class LinuxSetter():

    def setVar(self,envName, envValue, envDesc):
        path = str(Path.home()) + "/.profile"
        f = open(path, "r")
        textArr = f.readlines()
        f.close()

        try:
            posStart = textArr.index("# envSet - DONT TOUCH BELOW\n") + 1
            posEnd = textArr.index("# envSet - DONT TOUCH UP\n")
        except ValueError:
            textArr.append("# envSet - DONT TOUCH BELOW\n")
            posStart = len(textArr) + 1
            textArr.append("# envSet - DONT TOUCH UP\n")
            posEnd = len(textArr)

        varArr = textArr[posStart:posEnd]
        
        inserted = False
        for x in range(0, len(varArr)):
            var = varArr[x].split("=",2)
            varName = var[0]

            if(varName == envName):
                inserted=True
                textArr[x + posStart] = envName + "=" + envValue + " #" + envDesc + "\n"
                break
            
        if(not(inserted)):
            textArr.insert(posEnd, envName + "=" + envValue + " #" + envDesc + "\n")

        text = "".join(textArr)
        f = open(path, "w")
        f.write(text)
        f.close()

        print(Fore.YELLOW + strmsg.linuxLogout + Fore.RESET)

class MacSetter():

    def parseVar(self, envName, envValue):
        print("Mac")
