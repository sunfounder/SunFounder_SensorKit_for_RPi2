#!/usr/bin/env python3
import PCF8591 as ADC

def setup():
	ADC.setup(0x48)

def loop():
	while True:
		print (ADC.read(0))
		ADC.write(ADC.read(0))

def destroy():
	ADC.write(0)

if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
