#!/usr/bin/env python3
import PCF8591 as ADC
import time

def setup():
	ADC.setup(0x48)

def loop():
	status = 1
	while True:
		print ('Value:', ADC.read(0))
		Value = ADC.read(0)
		outvalue = map(Value,0,255,120,255)
		ADC.write(outvalue)
		time.sleep(0.2)
def destroy():
	ADC.write(0)

def map(x, in_min, in_max, out_min, out_max):
        '''To map the value from arange to another'''
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt: 
		destroy()
