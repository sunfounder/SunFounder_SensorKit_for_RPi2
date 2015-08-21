#!/usr/bin/env python
import PCF8591 as ADC
import time

def setup():
	ADC.setup(0x48)

def loop():
	while True:
		print "Current illumination: ", ADC.read(0)
		time.sleep(0.1)

def destroy():
	ADC.write(0)

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
