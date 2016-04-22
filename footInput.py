#!/usr/bin/env python

'''
v0.1  2016 Arp 23
  - can check 5 GPIO input
'''

import RPi.GPIO as GPIO
import time
import os

ins = [40, 38, 36, 32, 26]
GPIO.setmode(GPIO.BOARD)
for idx in range(5):
    GPIO.setup(ins[idx], GPIO.IN, pull_up_down=GPIO.PUD_UP)

vals = range(5)

while True:
    for idx in range(5):
        vals[idx]=GPIO.input(ins[idx])
        print vals[idx],
    print

    time.sleep(1.0)
