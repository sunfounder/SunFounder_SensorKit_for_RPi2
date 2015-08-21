#!/usr/bin/env python

import RPi.GPIO as GPIO
import ADC0832
import time

RAIN = 15

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(RAIN, GPIO.IN)
	ADC0832.setup()

def loop():
	while True:
		rainVal = ADC0832.getResult(0)
		print GPIO.input(RAIN)
		if GPIO.input(RAIN) == 0:
			print '***************'
			print '* !!RAINING!! *'
			print '***************'
			print ''
		print rainVal
		time.sleep(0.5)

def destroy():
	GPIO.cleanup()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
