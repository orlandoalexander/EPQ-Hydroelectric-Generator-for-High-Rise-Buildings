import RPi.GPIO as GPIO
import time


# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
time.sleep(3)

GPIO.output(26, GPIO.HIGH)

time.sleep(2)

GPIO.output(26, GPIO.LOW)

GPIO.output(21, GPIO.HIGH)

time.sleep(1)

GPIO.output(21, GPIO.LOW)
