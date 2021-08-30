import RPi.GPIO as GPIO
import time


# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)

# Set trigger to Low
GPIO.output(26, GPIO.HIGH)

time.sleep(3)

GPIO.output(26, GPIO.LOW)