import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)

try:
    GPIO.output(27, GPIO.HIGH)
    sleep(10)

finally:
    GPIO.output(27, GPIO.LOW)