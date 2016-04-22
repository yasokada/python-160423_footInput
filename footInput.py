#!/usr/bin/env python

'''
v0.1  2016 Arp 23
  - add main loop
'''

import RPi.GPIO as GPIO
import time
import os

swio=40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(swio, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	chk3=GPIO.input(swio)
	print chk3

	time.sleep(1.0)
