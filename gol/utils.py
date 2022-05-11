import os, sys
from fcntl import ioctl
from ioctl_cmds import *

fd = os.open('/dev/mydev', os.O_RDWR) #substituir pelo caminho do arquivo

def readButtons():
    print('estou na readButtons')
    ioctl(fd, RD_PBUTTONS)
    red = os.read(fd, 4); # read 4 bytes and store in red var
    pressedButton  = int.from_bytes(red, 'little')
    while(pressedButton == 15):
        pressedButton = int.from_bytes(red, 'little')
    match pressedButton:
        case 7:
            return 'up'
        case 11:
            return 'down'
        case 13:
            return 'left'
        case 14:
            return 'right'
        case _:
            return ''


