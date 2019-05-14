import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

enable_pin = 18
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.output(enable_pin, 0)
