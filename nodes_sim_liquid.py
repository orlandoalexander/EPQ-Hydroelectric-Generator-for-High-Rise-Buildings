import paho.mqtt.client as mqtt
import random
import time

clientNums = [1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26] # the first client (Raspberry Pi) which has sensors is on the first floor, as the ground floor barrier mechanism is just a barrier mechanism on its own with no sensors. The last client is number 26 and only has an ultrasonic distance sensor and liquid level sensor, as there is no water above it

client = mqtt.Client()
client.username_pw_set(username="yrczhohs", password="qPSwbxPDQHEI")
client.connect("hairdresser.cloudmqtt.com", 18973)

while True:
    randomNum = random.choice(clientNums)
    client.publish("sensors/liquid_level", ("{}").format(randomNum))
    randomTime = random.randint(7,20)
    time.sleep(randomTime)
