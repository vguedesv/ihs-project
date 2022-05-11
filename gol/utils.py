import os, sys
from fcntl import ioctl
from ioctl_cmds import *
import time

fd = os.open('/dev/mydev', os.O_RDWR) #substituir pelo caminho do arquivo

def readButtons():
    print('estou na readButtons')
    ioctl(fd, RD_PBUTTONS)
    button = os.read(fd, 4) # read 4 bytes and store in button var
    pressedButton  = int.from_bytes(button, 'little')

    ioctl(fd, RD_SWITCHES)
    switch = os.read(fd, 4)
    switchOldState = int.from_bytes(switch, 'little')
    switchNewState = switchOldState
    print(pressedButton)
    while(pressedButton == 15 and switchOldState == switchNewState):
        ioctl(fd, RD_PBUTTONS)
        button = os.read(fd, 4)
        pressedButton = int.from_bytes(button, 'little')
        ioctl(fd, RD_SWITCHES)
        switch = os.read(fd, 4)
        switchNewState = int.from_bytes(switch, 'little')
        time.sleep(0.2)
    
    switchOldState = switchNewState

    match pressedButton:
        case 7:
            return 'up'
        case 11:
            return 'down'
        case 13:
            return 'left'
        case 14:
            return 'right'
        case 12:
            return 'esc'
            
    
    match switchNewState:
        case 1:
            return 'space'
        case 2:
            return 'enter'
        case 3:
            return 'enter'
        case _:
            return ''


def setDisplay(num):
