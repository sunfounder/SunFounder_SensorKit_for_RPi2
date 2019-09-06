#!/usr/bin/env python3
#------------------------------------------------------
#
#		This is a program for JoystickPS2 Module.
#
#		This program depend on PCF8591 ADC chip. Follow 
#	the instruction book to connect the module and 
#	ADC0832 to your Raspberry Pi.
#
#------------------------------------------------------
import PCF8591 as ADC 
import time

def setup():
	ADC.setup(0x48)					# Setup PCF8591
	global state

def direction():	#get joystick result
	state = ['home', 'up', 'down', 'left', 'right', 'pressed']
	i = 0
	if ADC.read(0) <= 30:
		i = 1		#up
	if ADC.read(0) >= 225:
		i = 2		#down

	if ADC.read(1) >= 225:
		i = 3		#left
	if ADC.read(1) <= 30:
		i = 4		#right

	if ADC.read(2) <= 30:
		i = 5		# Button pressed

	if ADC.read(0) - 125 < 15 and ADC.read(0) - 125 > -15	and ADC.read(1) - 125 < 15 and ADC.read(1) - 125 > -15 and ADC.read(2) == 255:
		i = 0
	
	return state[i]

def loop():
	status = ''
	while True:
		tmp = direction()
		if tmp != None and tmp != status:
			print (tmp)
			status = tmp

def destroy():
	pass

if __name__ == '__main__':		# Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
