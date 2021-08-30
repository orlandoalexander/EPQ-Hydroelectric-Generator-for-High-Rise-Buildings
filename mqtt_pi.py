import paho.mqtt.client as mqtt
import time

def publish_message_distance(client_sensor):
    # function to publish data about the water level height in the pipe section to the topic 'sensors/ultrasonic_distance'
    client.publish("sensors/ultrasonic_distance", ("{},2.3").format(client_sensor)) # publishes the client name (floor number) and the distance to the water level in the pipe to the topic 'sensors/ultrasonic_distance'

def publish_message_next_distance(client_sensor):
    # function to publish data about the water level height in the pipe section to the topic 'sensors/next_ultrasonic_distance'
    client.publish("sensors/next_ultrasonic_distance", ("{},2.3").format(client_sensor)) # publishes the client name (floor number) and the distance to the water level in the pipe to the topic 'sensors/ultrasonic_distance'

def publish_message_barrier_status(status):
    # function to notifies the server that the barrier is now closed by publishing this 'Closed' status to the topic 'status/barrier_status'
    client.publish("status/barrier_status", status) # publishes 'Closed' the topic 'status/barrier_status'

def on_message_get_distance(client, userdata, msg):
    # callback function which is called when the server publishes to the topic 'sensors/ultrasonic_distance'
    msg = msg.payload.decode() # converts msg from bytearray to string
    if msg == clientNum: # if the server is asking for data from client 4 (the ID of the Raspberry Pi running this file), then the function 'publish_message_distance()' is called
        publish_message_distance(clientNum) # calls the function 'publish_message_distance()'

def on_message_get_next_distance(client, userdata, msg):
    # callback function which is called when the server publishes to the topic 'sensors/next_ultrasonic_distance'
    msg = msg.payload.decode() # converts msg from bytearray to string
    if msg == clientNum: # if the server is asking for data from client 4 (the ID of the Raspberry Pi running this file), then the function 'publish_message_next_distance()' is called
        publish_message_next_distance(clientNum)

def on_message_open_barrier(client, userdata, msg):
    # callback function which is called when the server publishes to the topic 'actions/open_barrier'
    msg = msg.payload.decode() # converts msg from bytearray to string
    barrier = msg.split(",")[0] # the msg string contains both info about the barrier to be opened and the distance to the water level below. These data items are seperated by a ',' so the split function is used to seperate the two data items; the first item is assigned to the variable 'barrier'
    ultrasonic_distance = msg.split(",")[1] # the msg string contains both info about the barrier to be opened and the distance to the water level below. These data items are seperated by a ',' so the split function is used to seperate the two data items; the second item is assigned to the variable 'ultrasonic_distance'
    if barrier == "All": # if all barriers are to be opened
        print("All barriers are open")
        # open barrier
        time.sleep(20)
        print("All barriers are closed")
        # closes all barriers
    elif barrier == clientNum: # if the barrier to be opened is this Raspberry Pi's barrier (barrier 4)
        print("Barrier 4 is open")
        # open barrier
        # if distance == None
        # call ultrasonic sensor to loop until (2.97 - ultrasound result - 0.2) == ultrasonic_distance
        # close barrier
        time.sleep(5)
        print("Barrier 4 is closed")
        publish_message_barrier_status("Closed") # calls function to notify server that barrier is closed

def on_connect(client, userdata, flags, rc):
    if rc == 0: # if connection is successful
        client.subscribe("actions/get_distance") # subscribes to topic 'actions/get_distance'
        client.subscribe("actions/open_barrier") # subscribes to topic 'actions/open_barrier'
        client.subscribe("actions/on_message_get_next_distance") # subscribes to topic 'actions/get_next_distance'
        client.message_callback_add("actions/get_distance", on_message_get_distance) # creates callback for topic 'actions/get_distance'
        client.message_callback_add("actions/open_barrier", on_message_open_barrier) # creates callback for topic 'actions/open_barrier'
        client.message_callback_add("actions/on_message_get_next_distance", on_message_get_next_distance) # creates callback for topic 'actions/get_next_distance'

    else:
        # attempts to reconnect
        client.on_connect = on_connect
        client.username_pw_set(username="yrczhohs", password="qPSwbxPDQHEI")
        client.connect("hairdresser.cloudmqtt.com", 18973)

clientNum = "4"
client = mqtt.Client()
client.username_pw_set(username="yrczhohs", password="qPSwbxPDQHEI")
client.on_connect = on_connect # creates callback for successful connection with broker
client.connect("hairdresser.cloudmqtt.com", 18973) # parameters for broker web address and port number

client.loop_forever()
