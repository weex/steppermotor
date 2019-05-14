import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

my_pin = int(sys.argv[1])

GPIO.setup(my_pin, GPIO.OUT)
GPIO.output(my_pin, 1)
time.sleep(5)
GPIO.output(my_pin, 0)
