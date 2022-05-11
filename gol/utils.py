import os, sys
from fcntl import ioctl
from ioctl_cmds import *
import time


HEX_NUMBERS = [
'C0',
'F9',
'A4',
'B0',
'99',
'92',
'82',
'F8',
'80',
'90',
'88',
'83',
'C6',
'A1',
'86',
'8E',
'89', #h
'8e' #l
]


fd = os.open('/dev/mydev', os.O_RDWR) #substituir pelo caminho do arquivo

def readButtons():
    # print('estou na readButtons')
    ioctl(fd, RD_PBUTTONS)
    button = os.read(fd, 4) # read 4 bytes and store in button var
    pressedButton  = int.from_bytes(button, 'little')

    ioctl(fd, RD_SWITCHES)
    switch = os.read(fd, 4)
    switchOldState = int.from_bytes(switch, 'little')
    switchNewState = switchOldState
    # print(pressedButton)
    while(pressedButton == 15 and switchOldState == switchNewState):

        ioctl(fd, RD_PBUTTONS)
        button = os.read(fd, 4)
        pressedButton = int.from_bytes(button, 'little')
        # print("wrote %d bytes"%retval)
        ioctl(fd, RD_SWITCHES)
        switch = os.read(fd, 4)
        switchNewState = int.from_bytes(switch, 'little')
        time.sleep(0.2)
    
    switchOldState = switchNewState

    match pressedButton:
        case 7:
            ioctl(fd, WR_GREEN_LEDS)
            temp = 192
            os.write(fd, temp.to_bytes(4, 'little'))
            time.sleep(0.5)
            temp = 0
            os.write(fd, temp.to_bytes(4, 'little'))
            return 'up'
        case 11:
            ioctl(fd, WR_GREEN_LEDS)
            temp = 48
            os.write(fd, temp.to_bytes(4, 'little'))
            time.sleep(0.5)
            temp = 0
            os.write(fd, temp.to_bytes(4, 'little'))
            return 'down'
        case 13:
            ioctl(fd, WR_GREEN_LEDS)
            temp = 12
            os.write(fd, temp.to_bytes(4, 'little'))
            time.sleep(0.5)
            temp = 0
            os.write(fd, temp.to_bytes(4, 'little'))
            return 'left'
        case 14:
            ioctl(fd, WR_GREEN_LEDS)
            temp = 3
            os.write(fd, temp.to_bytes(4, 'little'))
            time.sleep(0.3)
            temp = 0
            os.write(fd, temp.to_bytes(4, 'little'))
            return 'right'
        case 12:
            return 'esc'
            
    
    match switchNewState:
        case 1:
            return 'space'
        case 2:
            ioctl(fd, WR_RED_LEDS)
            temp = 0x3FFFF
            os.write(fd, temp.to_bytes(4, 'little'))
            time.sleep(0.5)
            temp = 0
            os.write(fd, temp.to_bytes(4, 'little'))
            return 'enter'
        case 3:
            return 'enter'
        case _:
            return ''


def setDisplay(side, num):
    algs = list(num.zfill(4))
    # print(algs)
    dataString = '0x' + HEX_NUMBERS[int(algs[0])] + HEX_NUMBERS[int(algs[1])] + HEX_NUMBERS[int(algs[2])] + HEX_NUMBERS[int(algs[3])]
    data = int(dataString, 16)
    # hex_data = hex(data)
    # print(data)
    if(side is 'left'):        
        ioctl(fd, WR_L_DISPLAY)
        retval = os.write(fd, data.to_bytes(4, 'little'))
    else:
        ioctl(fd, WR_R_DISPLAY)
        retval = os.write(fd, data.to_bytes(4, 'little'))

    
