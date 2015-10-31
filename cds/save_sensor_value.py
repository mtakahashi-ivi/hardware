import RPi.GPIO as GPIO
import time

sensor_pin = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)

while True:
	print GPIO.input(sensor_pin)
	time.sleep(0.1)
