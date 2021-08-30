import paho.mqtt.client as mqtt

def open_barrier_get_distances(client_message):
    # function which coordinates the requests to the appropriate clients to carry out and return ultrasonic distance measurements of the water level in the pipe section below
    global ultrasonic_distances # accesses the global variable 'ultrasonic_distances'
    global ultrasonic_distance # accesses the global variable 'ultrasonic_distance'
    global barrier_open_range # accesses the global variable 'barrier_open_range'
    global active_client # accesses the global variable 'active_client'
    active_client = client_message
    ultrasonic_distances = []
    barrier_open_range = []
    if client_message == 1: # if the client which notifies the server that its pipe section is full is the client with the number '1' (first floor client), then only the ground floor client must open its barrier, so no ultrasonic distance measurements are required
        barrier_open_range.append(0) # only the ground floor barrier (client 0) must be opened
        ultrasonic_distances.append("None") # as the ground floor barrier runs directly ito the penstock pipe, there are no clients which must measure ultrasonic distances in their pipe section
        ultrasonic_distance = 0 # the distance below the ground floor barrier is set to '0' as it runs directly into the penstock pipe
        open_barrier()  # calls the function to open all the barriers and release all the water in the pipe over the turbine
    for client in range((active_client-1), 0, -1): # iterates through all the clients below the pipe section which is full of liquid
        publish_get_distance(client) # calls the function 'publish_get_distance' for each client elow the pipe section which is full of liquid

def open_barrier():
    # function which opens one barrier at a time in order to redistribute the liquid from the pipe which is full of liquid
    global barrier_open_range # accesses the global variable 'barrier_open_range'
    global ultrasonic_distance # accesses the global variable 'ultrasonic_distance'
    global ultrasonic_distances # accesses the global variable 'ultrasonic_distances'
    global barrier_status # accesses the global variable 'barrier_status'
    barrier = barrier_open_range[0] # the first element in the list 'barrier_open_range' is the next barrier to be opened
    barrier_open_range.pop(0) # the first element in the list 'barrier_open_range' is removed as this barrier has now been opened
    ultrasonic_distances.pop(0) # the first element in the list 'ultrasonic_distances' is removed as this distance has now been measured
    client.publish("actions/open_barrier", "{},{}".format(barrier, ultrasonic_distance), qos=2) # publishes the barrier which is to be opened and the water level below that barrier to the topic 'actions/open_barrier'
    barrier_status = "Open" # sets the global variable 'barrier_status' to 'Open' to signify that a barrier is currently open
    print("\nOpened barrier",barrier)
    print("Water level below barrier",barrier,"is",ultrasonic_distance,"metres")

def open_barriers():
    # function which opens all the barriers
    global open_all_barriers
    open_all_barriers = True # sets the global variable 'open_all_barriers' to True to signify that all barriers are currently open
    client.publish("actions/open_barrier", "All, None", qos=2) # publishes 'All' to the topic 'actions/open_barrier' so that all clients open their barrier

def barrier_coordination():
    # function which coordinates the opening and closing of the barriers
    global barrier_open_range # accesses the global variable 'barrier_open_range'
    global ultrasonic_distances # accesses the global variable 'ultrasonic_distances'
    global ultrasonic_distance # accesses the global variable 'ultrasonic_distance'
    global active_client # accesses the global variable 'active_client'
    counter = 0
    print("\nActive client:", active_client)
    for i in ultrasonic_distances: # iterates through all the measurements of water level below clients
        barrier = int(i.split(",")[0]) # each element in the list 'ultrasonic_distances' stores the barrier number and the water level below it. The value before the ',' is the barrier number and is assigned to the variable 'barrier'
        ultrasonic_distance = (i.split(",")[1]) # each element in the list 'ultrasonic_distances' stores the barrier number and the water level below it. The value after the ',' is the barrier number and is assigned to the variable 'ultrasonic_distance'
        if counter == 2:  # if the iteration through two measurements of water level has not found any pipe sections which are sufficiently empty, then all barriers are opened and all the water in the pipe is released across the turbine
            print("\nOpened all barriers - checked 2 pipe sections below pipe section",active_client,"and both are too full")
            ultrasonic_distance = ""
            open_barriers()  # calls the function to open all the barriers
            break
        elif float(ultrasonic_distance) < 1: # if the height above the water level in the pipe section is less than 1 metre, then it is deemed to be an isufficient amount of space to store the excess liquid on its own, so the iteration continues
            if len(ultrasonic_distances) == 1: # if the active client is client 2, then there will only be one available measurement of ultrasonic distance (below client 1), as client 0 is on the ground floor and leads directly into the penstock pipe
                barrier_open_range = [0,1] # only the ground floor barrier (client 0) and first floor barrier (client 1) must be opened
                ultrasonic_distances = ["0", ultrasonic_distances[0]] # the distance below the ground floor barrier (client 0) is 0 metres as it runs directly into the penstock pipe
                ultrasonic_distance = 0
                open_barrier()  # calls the function to open all the barriers and release all the water in the pipe over the turbine
                print("Barriers to be opened:", (", ".join(str(barriers) for barriers in barrier_open_range)))
                break
            else:
                counter+=1 # the value of counter is incremented by a value of '1' to indicate that the height of the water in another pipe section has been measured and has been deemed to have an isufficient amount of space to store the excess liquid on its own
        else:
            barrier_open_range = [item for item in range(barrier, active_client)] # creates a list which stores all the barriers which need to be opened, starting with the barrier furthest down the pipe
            ultrasonic_distances = (ultrasonic_distances[:len(barrier_open_range)]) # creates a list of all the client numbers and the water height in their pipe section below (i.e. their ultrasonic distances) required to coordinate the opening and closing of the barriers in 'barrier_open_range'
            ultrasonic_distances.reverse() # reverses the list ultrasonic_distances as the barriers are opened from the barrier furthest down the pipe upwards
            print("Barriers to be opened:", (", ".join(str(barriers) for barriers in barrier_open_range)))
            open_barrier() # calls the function 'open_barrier()' to open the first barrier which is to be opened
            break

def publish_get_distance(client_action):
    # function which publishes to the topic 'actions/get_distance' with the client numbers from which the server is request water level measurements
    client.publish("actions/get_distance", client_action, qos=2)

def publish_get_next_distance(client_action):
    # function which publishes to the topic 'actions/on_message_get_next_distance' with the client numbers from which the server is request water level measurements
    client.publish("actions/on_message_get_next_distance", client_action, qos=2)

def on_message_barrier_status(client, userdata, msg):
    # callback function which is called when a client publishes to the topic 'status/barrier_status'
    global ultrasonic_distances  # accesses the global variable 'ultrasonic_distances'
    global ultrasonic_distance  # accesses the global variable 'ultrasonic_distance'
    global barrier_status  # accesses the global variable 'barrier_status'
    global open_all_barriers  # accesses the global variable 'open_all_barriers'
    global client_queue  # accesses the global variable 'client_queue'
    global busy  # accesses the global variable 'busy'
    msg = msg.payload.decode() # converts msg from bytearray to string
    busy = False # the global variable 'busy' is set to False as a client has indicated that the barrier(s) which were open is/are now closed, so the pipe system and the server is no longer busy coordinating the opening and closing of pipes
    if msg == "Closed" and open_all_barriers == False and len(barrier_open_range)>0: # if the barrier that was open has has now been closed, but there are still more barriers to be opened to redistribute the water that is in the pipe section which is full (as indicated by the fact that there are still elements in the list 'barrier_open_range)
        print("\nFinding water level in next pipe section")
        busy = True # the global variable 'busy' is set to True as the pipe system and server are now busy again
        next_distance = int(ultrasonic_distances[0].split(",")[0]) # the first element in the list 'ultrasonic_distances' is the next client whose distance to the water level in its pipe section must be measured
        publish_get_next_distance(next_distance) # calls the function 'publish_get_next_distance()'
    elif msg == "Closed" and open_all_barriers == False and len(barrier_open_range)==0: # if the barrier that was open has has now been closed and there are no more barriers to be opened (as indicated by the fact that there are no more elements in the list 'barrier_open_range)
        barrier_status = "Closed" # the global variable 'barrier_status' is set to 'Closed' as all the barriers are now closed
        print("\nAll barriers are closed")
        print("Barrier status is now:", barrier_status)
        if len(client_queue) == 1: # if there is a client which is full of liquid and is waiting for the water in its pipe section to be released/redistributed
            print("\nNew barrier(s) to be opened from queue")
            busy = True # the global variable 'busy' is set to True as the pipe system and server are now busy again
            client_message = client_queue.pop(0) # the first element in the list 'client_queue' is the client which has been waiting for the water in its pipe section to be released/redistributed
            open_barrier_get_distances(int(client_message)) # calls the function 'open_barrier_get_distances()'
        elif len(client_queue) > 1: # if there is more than one client which is full of liquid and is waiting for the water in its pipe section to be released/redistributed, all barriers are to be opened to avoid any issues
            print("\nOpened all barriers - more than 1 client in queue")
            ultrasonic_distance = ""
            open_barriers() # calls the function 'open_barriers()'
    elif msg == "All closed": # if all the barriers were open and all the barriers have now been closed
        open_all_barriers = False # the global variable 'open_all_barriers' is set to False as all the barriers are no longer opened
        barrier_status = "Closed" # the global variable 'barrier_status' is set to 'Closed' as all the barriers are now closed
        print("\nAll barriers are closed")
        print("Barrier status is now:", barrier_status)


def on_message_liquid_level(client, userdata, msg):
    # callback function which is called when a client publishes to the topic 'sensors/liquid_level'
    global ultrasonic_distances # accesses the global variable 'ultrasonic_distances'
    global ultrasonic_distance # accesses the global variable 'ultrasonic_distance'
    global barrier_status # accesses the global variable 'barrier_status'
    global open_all_barriers # accesses the global variable 'open_all_barriers'
    global client_queue # accesses the global variable 'client_queue'
    global busy # accesses the global variable 'busy'
    global barrier_open_range # accesses the global variable 'barrier_open_range'
    client_message = msg.payload.decode() # converts msg from bytearray to string and assigns the data from the message (which is the client who sent the message) to the variable 'client_message'
    print("\nPipe section",client_message,"is full")
    if client_message == "All": # if the client which was too full of liquid has been waiting for too long for the water in its pipe section to be released/redistributed, then all barriers are opened to avoid any issues
        print("Opened all barriers - waiting too long to open individual barriers")
        client_queue = [] # clears all the clients from the queue as all the barriers have now been opened
        open_barriers() # calls the function 'open_barriers()'
    elif open_all_barriers == True: # if the global variable 'open_all_barriers' is set to True, then all barriers are already open so nothing needs to be done
        print ("All barriers already open")
        pass
    elif len(client_queue) == 1: # if there is already a client in the queue waiting for the water in its pipe section to be released/redistributed
        if busy == True: # if the pipe system and server is still busy opening barriers to redistribute water from another client whose pipe section is full of liquid        if len(barrier_open_range) > 0: #
            print("Opened all barriers - server is busy and one client already in the queue")
            client_queue = [] # clears all the clients from the queue as all the barriers have now been opened
            open_barriers() # calls the function 'open_barriers()'
        else:
            print("Added pipe section", client_message, "to queue")
            print("New barrier(s) to be opened (from queue)")
            client_queue.append((client_message)) # the client which is too full of liquid is added to the queue of clients waiting for the water in its pipe section to be released/redistributed
            client_message = client_queue.pop(0) # the first element in the list 'client_queue' is the client which has been water in its pipe section to be released/redistributed
            open_barrier_get_distances(int(client_message)) # calls the function 'open_barrier_get_distances'
    elif len(client_queue) > 1: # if there is more than one client in the queue waiting for the water in its pipe section to be released/redistributed - note: this situation should never arise!
        print("Opened all barriers - more than 1 client in queue")
        client_queue = [] # clears all the clients from the queue as all the barriers have now been opened
        open_barriers() # calls the function 'open_barriers()'
    elif busy == True and len(client_queue) == 0: # if the pipe system and server is busy but there are no clients in the queue waiting for the water in its pipe section to be released/redistributed
        print("Added pipe section",client_message,"to queue")
        client_queue.append(client_message) # adds the client whose pipe section is too full of liquid to the queue of clients waiting for the water in their pipe section to be released/redistributed
    else:
        print("New barrier(s) to be opened")
        busy = True  # the global variable 'busy' is set to True as the pipe system and server are now busy again
        open_barrier_get_distances(int(client_message)) # calls the function 'open_barrier_get_distances()'

def on_message_ultrasonic_distance(client, userdata, msg):
    # callback function which is called when a client publishes to the topic 'sensors/ultrasonic_distance'
    global ultrasonic_distances # access the global variable 'ultrasonic_distances'
    global barrier_open_range # access the global variable 'barrier_open_range'
    global active_client # access the global variable 'active_client'
    msg = msg.payload.decode() # converts msg from bytearray to string
    ultrasonic_distances.append(msg) # appends the msg data which includes the client number (which is a Raspberry Pi) and the water level below this client
    if len(ultrasonic_distances) == active_client-1: # if all the required clients have returned their values for the distance to the water level in their pipe section
        ultrasonic_distances.sort(key=lambda tup: int(tup[:tup.index(",")]), reverse=True)  # sorts the list 'ultrasonic_distances' by the first element in each tuple (which is the Raspberry Pi client number) so that the values of the distances to the water level are in descending order, starting with the client number below the clien which is too full of liquid
        barrier_coordination() # calls the function 'barrier_coordination()'
    else: # if not all the required clients have returned their values for the distance to the water level in their pipe section yet
        pass

def on_message_next_ultrasonic_distance(client, userdata, msg):
    # callback function which is called when a client publishes to the topic 'sensors/next_ultrasonic_distance'
    global ultrasonic_distance # access the global variable 'ultrasonic_distance'
    print("Next distance: ",msg.payload.decode())
    ultrasonic_distance = msg.payload.decode().split(",")[1] # converts msg from bytearray to string
    open_barrier() # calls the function 'open_barrier'

def on_connect(client, userdata, flags, rc):
    # callback function which is called when the server successfully connects to the MQTT broker
    if rc == 0:
        # placing subscription command in the connection callback ensures that subscription to a topic occurs after a successful connection to the broker
        client.subscribe("sensors/liquid_level") # subscribes to topic 'sensors/liquid_level'
        client.subscribe("sensors/ultrasonic_distance") # subscribes to topic 'sensors/ultrasonic_distance'
        client.subscribe("sensors/next_ultrasonic_distance")  # subscribes to topic 'sensors/next_ultrasonic_distance'
        client.subscribe("status/barrier_status") # subscribes to topic 'sensors/barrier_status'
        client.message_callback_add("sensors/liquid_level", on_message_liquid_level) # creates callback for topic 'sensors/liquid_level'
        client.message_callback_add("sensors/ultrasonic_distance", on_message_ultrasonic_distance) # creates callback for topic 'sensors/ultrasonic_distance'
        client.message_callback_add("sensors/next_ultrasonic_distance",on_message_next_ultrasonic_distance)  # creates callback for topic 'sensors/next_ultrasonic_distance'
        client.message_callback_add("status/barrier_status", on_message_barrier_status) # creates callback for topic 'sensors/barrier_status'
    else:
        # attempts to connect again
        client.on_connect = on_connect
        client.username_pw_set(username="raspberrypi", password="RaspberryP1")
        client.connect("node02.myqtthub.com", 1883)

ultrasonic_distances = []
barrier_open_range = []
client_queue = []
ultrasonic_distance = ""
barrier_status = ""
active_client = 0
busy = False
open_all_barriers = False

client = mqtt.Client()
client.username_pw_set(username="yrczhohs", password="qPSwbxPDQHEI")
client.on_connect = on_connect # creates callback for successful connection with the MQTT broker
client.connect("hairdresser.cloudmqtt.com", 18973) # parameters for the MQTT broker web address and port number

client.loop_forever() # program loops indefinitely

