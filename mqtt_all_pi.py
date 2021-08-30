import paho.mqtt.client as mqtt
import random
import decimal
import time

def publish_message_distance(client_sensor):
    randomNum = decimal.Decimal(random.randrange(0, 297))/100
    client.publish("sensors/ultrasonic_distance", ("{},{}").format(client_sensor, randomNum), qos=2)

def publish_message_next_distance(client_sensor):
    randomNum = decimal.Decimal(random.randrange(0, 297)) / 100
    client.publish("sensors/next_ultrasonic_distance", ("{},{}").format(client_sensor, randomNum), qos=2)

def publish_message_barrier_status(status):
    client.publish("status/barrier_status", status, qos=2)

def on_message_get_distance(client, userdata, msg):
    msg = msg.payload.decode()
    if int(msg) != 4:
        publish_message_distance(msg)

def on_message_get_next_distance(client, userdata, msg):
    msg = msg.payload.decode()
    if int(msg) != 4:
        publish_message_next_distance(msg)

def on_message_open_barrier(client, userdata, msg):
    msg = msg.payload.decode()
    barrier = msg.split(",")[0]
    ultrasonic_distance = msg.split(",")[1]
    if barrier == "All":
        print("All barriers are open")
        # open all barriers
        time.sleep(20)
        print("All barriers are closed")
        # closes all barriers
        publish_message_barrier_status("All closed")
    elif barrier != "4":
        print("Barrier", barrier, "is open")
        # open barrier
        # call ultrasonic sensor to loop until (2.97 - ultrasound result - 0.2) == ultrasonic_distance
        # close barrier
        time.sleep(5)
        print("Barrier", barrier, "is closed")
        publish_message_barrier_status("Closed")


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("actions/get_distance")
        client.subscribe("actions/open_barrier")
        client.subscribe("actions/on_message_get_next_distance")
        client.message_callback_add("actions/get_distance", on_message_get_distance)
        client.message_callback_add("actions/open_barrier", on_message_open_barrier)
        client.message_callback_add("actions/on_message_get_next_distance", on_message_get_next_distance)
    else:
        # attempts to connect again
        client.on_connect = on_connect
        client.username_pw_set(username="yrczhohs", password="qPSwbxPDQHEI")
        client.connect("hairdresser.cloudmqtt.com", 18973)




client = mqtt.Client()
client.username_pw_set(username="yrczhohs", password="qPSwbxPDQHEI")
client.on_connect = on_connect
client.connect("hairdresser.cloudmqtt.com", 18973)

client.loop_forever()





