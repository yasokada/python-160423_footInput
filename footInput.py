#!/usr/bin/env python

'''
v0.3 2016 Apr 23
  - add UDP_recvData()
  - add UDP_setup()
  - add GPIO_setup()
v0.2 2016 Apr 23
  - define main()
  - change interval to 10 msec base for UDP comm
v0.1 2016 Apr 23
  - can check 5 GPIO input
'''

import RPi.GPIO as GPIO
import socket
import time
import os

ins = [40, 38, 36, 32, 26]

def GPIO_setup():
    GPIO.setmode(GPIO.BOARD)
    for idx in range(5):
        GPIO.setup(ins[idx], GPIO.IN, pull_up_down=GPIO.PUD_UP)

def UDP_setup():
    # incoming data string port
    datip="" # INADDR_ANY
    datport = 7002
    datsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    datsock.bind((datip, datport))
    datsock.setblocking(0)
    return datsock

def UDP_recvData(datsock, rcvdat):
	try:
		data,address = datsock.recvfrom(100)
	except socket.error:
			pass
	else:
		rcvdat = rcvdat + data
		return rcvdat, True
	return rcvdat, False

def main():
    GPIO_setup()
    datsock = UDP_setup()
    
    vals = range(5)
    cnt=0
    rcvdat = ""

    while True:
        cnt=cnt+1
        rcvdat,rcvd = UDP_recvData(datsock, rcvdat)
        time.sleep(0.01)

        if cnt < 30: # 300msec
            continue
        cnt=0

        for idx in range(5):
            vals[idx]=GPIO.input(ins[idx])
            print vals[idx],
        print

if __name__ == '__main__':
    main()
