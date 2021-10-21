import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time


def get_ultrasonic_distance():
    # Speed of sound in cm/s at temperature
#     temperature = 25
#     speedSound = 33100 + (0.6*temperature)

#     print("Ultrasonic Measurement")
#     print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")
    
#     # Use BCM GPIO references
#     # instead of physical pin numbers
#     GPIO.setmode(GPIO.BCM)

#     GPIO_TRIGGER = 18
#     GPIO_ECHO    = 23
#     GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
#     GPIO.setup(GPIO_ECHO, GPIO.IN)
    
#     # Set trigger to Low
#     GPIO.output(GPIO_TRIGGER, GPIO.LOW)

#     # Allow module to settle
#     time.sleep(0.5)

#     # Send 10us pulse to trigger
#     GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
#     # Wait 10us
#     time.sleep(0.00001)
#     GPIO.output(GPIO_TRIGGER, GPIO.LOW)
#     start = time.time()

#     while GPIO.input(GPIO_ECHO)==0:
#         start = time.time()

#     while GPIO.input(GPIO_ECHO)==1:
#         stop = time.time()

#     # Calculate pulse length
#     elapsed = stop-start

#     # Distance pulse travelled in that time is time
#     # multiplied by the speed of sound (cm/s)
#     distance = elapsed * speedSound

#     # That was the distance there and back so halve the value
#     distance = distance / 2

#     # Converts the distance to metres and formats the distance to two decimal places
#     distance = "{0:.2f}".format(distance/100)
#     if float(distance) > 5: # if the distance is less than 25 cm, the ultrasonic distance sensor will give an invalid and large result
#         distance = "0"
#     print("Distance : {}".format(distance))

#     # Reset GPIO settings
#     GPIO.cleanup()
    
    return 0.12

def publish_message_distance(client_sensor):
    # function to publish data about the water level height in the pipe section to the topic 'sensors/ultrasonic_distance'
    distance = get_ultrasonic_distance() # gets the distance to the water level below the barrier of this client (which is client 4) 
    print("Get distance below barrier 4")
    client.publish("sensors/ultrasonic_distance", ("{},{}").format(client_sensor, distance), qos=2) # publishes the client name (floor number) and the distance to the water level in the pipe to the topic 'sensors/ultrasonic_distance'

def publish_message_next_distance(client_sensor):
    # function to publish data about the water level height in the pipe section to the topic 'sensors/next_ultrasonic_distance'
    distance = get_ultrasonic_distance() # gets the distance to the water level below the barrier of this client (which is client 4) 
    print("Get (next) distance below barrier 4")
    client.publish("sensors/next_ultrasonic_distance", ("{},{}").format(client_sensor, distance), qos=2) # publishes the client name (floor number) and the distance to the water level in the pipe to the topic 'sensors/ultrasonic_distance'

def publish_message_barrier_status(status):
    # function to notifies the server that the barrier is now closed by publishing this 'Closed' status to the topic 'status/barrier_status'
    client.publish("status/barrier_status", status, qos=2) # publishes 'Closed' the topic 'status/barrier_status'

def on_message_get_distance(client, userdata, msg):
    # callback function which is called when the server publishes to the topic 'sensors/ultrasonic_distance'
    msg = msg.payload.decode() # converts msg from bytearray to string
    if msg == clientNum: # if the server is asking for data from client 4 (the ID of the Raspberry Pi running this file), then the function 'publish_message_distance()' is called
#         print("Get distance!")
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
    distance = msg.split(",")[1] # the msg string contains both info about the barrier to be opened and the distance to the water level below. These data items are seperated by a ',' so the split function is used to seperate the two data items; the second item is assigned to the variable 'ultrasonic_distance'
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)
    GPIO_ELECTROMAGNET = 21
    GPIO_SOLENOID = 26
    GPIO.setup(GPIO_ELECTROMAGNET, GPIO.OUT)
    GPIO.setup(GPIO_SOLENOID, GPIO.OUT)
    GPIO.output(GPIO_ELECTROMAGNET, GPIO.LOW)
    GPIO.output(GPIO_SOLENOID, GPIO.LOW)
    
    if barrier == "All": # if all barriers are to be opened
        print("All barriers are open")
        # open barrier
        GPIO.output(GPIO_ELECTROMAGNET, GPIO.HIGH)
        GPIO.output(GPIO_SOLENOID, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(GPIO_ELECTROMAGNET, GPIO.LOW)
        GPIO.output(GPIO_SOLENOID, GPIO.LOW)
        time.sleep(5)
        GPIO.output(GPIO_SOLENOID, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(GPIO_SOLENOID, GPIO.LOW)
        print("All barriers are closed")
        # closes all barriers
    elif barrier == clientNum: # if the barrier to be opened is this Raspberry Pi's barrier (barrier 4)
        print("Barrier 4 is open")
        # open barrier
        GPIO.output(GPIO_ELECTROMAGNET, GPIO.HIGH)
        GPIO.output(GPIO_SOLENOID, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(GPIO_ELECTROMAGNET, GPIO.LOW)
        GPIO.output(GPIO_SOLENOID, GPIO.LOW)
        if distance != "None": 
            while float(distance) > 0.3:
                distance = get_ultrasonic_distance()
        else:
            time.sleep(5) # replace with time to empty bottom section of pipe
        # close barrier
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_SOLENOID, GPIO.OUT)
        GPIO.output(GPIO_SOLENOID, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(GPIO_SOLENOID, GPIO.LOW)
        print("Barrier 4 is closed")
        publish_message_barrier_status("Closed") # calls function to notify server that barrier is closed

def on_connect(client, userdata, flags, rc):
    if rc == 0: # if connection is successful
        print("Connected")
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
