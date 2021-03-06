#!/usr/bin/python

import matplotlib.pyplot as plt
import random
import time

timespan = range(1, 8)

import sys
sys.path.append('..')

import SmartDHT22

dht = SmartDHT22.SmartDHT22(4)

data = {}
data['humidity'] = []
data['temp_f'] = []
data['temp_c'] = []

for i in timespan:
    data['humidity'].append(dht.get_humidity())
    data['temp_f'].append(dht.get_temp_fahrenheit())
    data['temp_c'].append(dht.get_temp_celsius())
    time.sleep(1)

plt.title("Collected Data from Lab 2")

plt.subplot(3, 1, 1)
plt.plot(timespan, data['humidity'], 'o-')
plt.ylabel('humidity')

plt.subplot(3, 1, 2)
plt.plot(timespan, data['temp_f'], '.-')
plt.ylabel('temperature (in Fahrenheit)')

plt.subplot(3, 1, 3)
plt.plot(timespan, data['temp_c'], '.-')
plt.ylabel('temperature (in Celsius)')

plt.xlabel('time (in minutes)')
plt.show()
