import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time


def on_connect(client, userdata, flags, rc):
    if rc == 0: # if connection is successful
        print("Connected")
    else:
        # attempts to reconnect
        client.on_connect = on_connect
        client.username_pw_set(username="yrczhohs", password="qPSwbxPDQHEI")
        client.connect("hairdresser.cloudmqtt.com", 18973)

client = mqtt.Client()
client.username_pw_set(username="yrczhohs", password="qPSwbxPDQHEI")
client.on_connect = on_connect # creates callback for successful connection with broker
client.connect("hairdresser.cloudmqtt.com", 18973) # parameters for broker web address and port number
 

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_LIQUID = 4
GPIO.setup(GPIO_LIQUID, GPIO.IN)

while True:
    if GPIO.input(GPIO_LIQUID)==1:
        client.publish("sensors/liquid_level","5", qos =2)
        print("There's liquid!")
        start_time = time.time()
        while GPIO.input(GPIO_LIQUID)==1:
            if (time.time() - start_time) > 4:
                client.publish("sensors/liquid_level","All")
                print("There's still liquid - open all barriers!")
                time.sleep(5)
                break
            time.sleep(0.1)
    client.loop()

 
