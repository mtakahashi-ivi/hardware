import RPi.GPIO as GPIO
from RPIO import PWM
import time

servo_pin = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.output(servo_pin, False)
servo = PWM.Servo()

while True:
	servo.set_servo(servo_pin, 1500)
	time.sleep(2)
	servo.set_servo(servo_pin, 1000)
	time.sleep(2)
