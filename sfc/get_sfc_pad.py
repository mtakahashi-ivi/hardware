import RPi.GPIO as GPIO
import time

clock = 14
reset = 15
data = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(reset, GPIO.OUT)
GPIO.setup(clock, GPIO.OUT)
GPIO.setup(data,  GPIO.IN)

def get_pad_status():
	keys = ["b", "y", "select", "start", "up", "down", "left", "right", "a", "x", "l", "r"]
	status = {}
	GPIO.output(reset, True)
	GPIO.output(reset, False)

	for i in range(0, 12):
		status[keys[i]] = not GPIO.input(data)
		GPIO.output(clock, True)
		GPIO.output(clock, False)

	return status

while True:
	print get_pad_status()
	time.sleep(0.1)
