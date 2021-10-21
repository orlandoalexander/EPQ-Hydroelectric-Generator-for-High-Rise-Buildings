import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time


def get_ultrasonic_distance():
    # Speed of sound in cm/s at temperature
    temperature = 25
    speedSound = 33100 + (0.6*temperature)

    
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    GPIO_TRIGGER = 18
    GPIO_ECHO    = 23
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    
    # Set trigger to Low
    GPIO.output(GPIO_TRIGGER, GPIO.LOW)

    # Allow module to settle
    time.sleep(0.5)

    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
    # Wait 10us
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, GPIO.LOW)
    start = time.time()

    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()

    while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()

    # Calculate pulse length
    elapsed = stop-start

    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * speedSound

    # That was the distance there and back so halve the value
    distance = distance / 2

    # Converts the distance to metres and formats the distance to two decimal places
    distance = "{0:.2f}".format(distance/100)
    if float(distance) > 5: # if the distance is less than 25 cm, the ultrasonic distance sensor will give an invalid and large result
        distance = "0"
    print("Distance : {}".format(distance))

    # Reset GPIO settings
    GPIO.cleanup()
    
    return distance

print("Ultrasonic Measurement")
for i in range (30):
    print(get_ultrasonic_distance())
