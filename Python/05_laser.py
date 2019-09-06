#!/usr/bin/env python3
#####################################################
#
#	DO NOT WATCH THE LASER DERECTELY IN THE EYE!
#
#####################################################
import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def loop():
	while True:
		#'...Laser on'
		GPIO.output(LedPin, GPIO.LOW)  # led on
		time.sleep(0.5)
		#'Laser off...'
		GPIO.output(LedPin, GPIO.HIGH) # led off
		time.sleep(0.5)

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

