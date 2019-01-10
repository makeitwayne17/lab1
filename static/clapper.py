#!/usr/bin/python

import matplotlib.pyplot as plt
import random
import time
import RPi.GPIO as GPIO

timespan = range(1, 50)

import sys
sys.path.append('..')

import SmartSound
sound = SmartSound.SmartSound()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.OUT)

while True:
    print(str(sound.get_gate()))

    if sound.get_gate() == 1023:
        GPIO.output(13, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(13, GPIO.LOW)
