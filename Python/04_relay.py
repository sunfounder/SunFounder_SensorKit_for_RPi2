#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

RelayPin = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(RelayPin, GPIO.OUT)
	GPIO.output(RelayPin, GPIO.HIGH)

def loop():
	while True:
		#'...relayd on'
		GPIO.output(RelayPin, GPIO.LOW)
		time.sleep(0.5)
		#'relay off...'
		GPIO.output(RelayPin, GPIO.HIGH)
		time.sleep(0.5)

def destroy():
	GPIO.output(RelayPin, GPIO.HIGH)
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

