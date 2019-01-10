#!/usr/bin/python

import matplotlib.pyplot as plt
import random
import time

timespan = range(1, 5)

import sys
sys.path.append('..')

import SmartSound

sound = SmartSound.SmartSound()

data = {}
data['audio'] = []
data['envelope'] = []
data['gate'] = []

for i in timespan:
    data['audio'].append(sound.get_audio())
    data['envelope'].append(sound.get_envelope())
    data['gate'].append(sound.get_gate())
    time.sleep(2)

plt.title("Collected Data from Lab 2")

plt.subplot(3, 1, 1)
plt.plot(timespan, data['audio'], 'o-')
plt.ylabel('audio')

plt.subplot(3, 1, 2)
plt.plot(timespan, data['envelope'], '.-')
plt.ylabel('envelope')

plt.subplot(3, 1, 3)
plt.plot(timespan, data['gate'], '.-')
plt.ylabel('gate')

plt.xlabel('time (in minutes)')
plt.show()
