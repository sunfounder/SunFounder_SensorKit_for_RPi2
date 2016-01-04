#!/usr/bin/env python
import PCF8591 as ADC
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

def setup():
	ADC.setup(0x48)

def loop():
	status = 1
	while True:
		print 'Value:', ADC.read(0)
		
		time.sleep(0.2)

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		pass	
