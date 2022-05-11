import os, sys
from fcntl import ioctl
from ioctl_cmds import *

fd = os.open('/dev/mydev', os.O_RDWR) #substituir pelo caminho do arquivo

def readButtons():
    ioctl(fd, RD_PBUTTONS)
    red = os.read(fd, 4); # read 4 bytes and store in red var
    print(int.from_bytes(red, 'little'))
    print(red)


while(True):
    readButtons()