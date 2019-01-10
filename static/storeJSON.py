import random
import time
import json

import sys
sys.path.append('..')

timespan = range(1, 61)

import SmartDHT22
import SmartMCP3008
import SmartSound

dht = SmartDHT22.SmartDHT22(4)
mcp = SmartMCP3008.SmartMCP3008()
sound = SmartSound.SmartSound()

data = {}

data['humidity'] = []
data['temp_f'] = []
data['temp_c'] = []
data['audio'] = []
data['envelope'] = []
data['gate'] = []

for i in timespan:
   # data['humidity'].append(dht.get_humidity())
   # data['temp_f'].append(dht.get_temp_fahrenheit())
   # data['temp_c'].append(dht.get_temp_celsius())
    data['audio'].append(sound.get_audio())
    data['envelope'].append(sound.get_envelope())
    data['gate'].append(sound.get_gate())
    print(i)
    time.sleep(5)


with open('data.json', 'w') as jsonfile:
    json.dump(data, jsonfile)

