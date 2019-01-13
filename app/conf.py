import os
import time

def PrScrn():#调用 dll示例
    time.sleep(0.5)
    os.popen('rundll32 .\\script\\截图\\PrScrn.dll PrScrn')

def Open360Wifi():#打开应用程序示例
    os.popen('"C:\\Program Files (x86)\\360\\360AP\\360AP.exe" /menufree')

def OpenRegedit():#调用 命令示例
    os.popen('regedit')

def Ifconfig():
    os.system('''ipconfig & pause''')

menuItems=[
    {"text":"截图","icon":"./icons/cut.png","event":PrScrn,"hot":"Alt+P"},
    {"text":"360Wifi","icon":"./icons/wifi.png","event":Open360Wifi,"hot":"Alt+W"},
    {"text":"注册表","icon":"./icons/regedit.png","event":OpenRegedit,"hot":"Alt+R"},
    {"text":"ifconfig","icon":"./icons/ip.png","event":Ifconfig,"hot":"Alt+R"}
] 