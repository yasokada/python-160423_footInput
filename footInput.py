#!/usr/bin/env python

'''
v0.1  2016 Arp 23
  - add main loop
'''

import RPi.GPIO as GPIO
import time
import os

ins = range(6)
ins[0] = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ins[0], GPIO.IN, pull_up_down=GPIO.PUD_UP)

vals = range(6)

while True:
	vals[0]=GPIO.input(ins[0])
	print vals[0]

	time.sleep(1.0)
