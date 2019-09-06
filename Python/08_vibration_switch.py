#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

VibratePin = 11
Gpin   = 13
Rpin   = 12

tmp = 0

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(Gpin, GPIO.OUT)     # Set Green Led Pin mode to output
	GPIO.setup(Rpin, GPIO.OUT)     # Set Red Led Pin mode to output
	GPIO.setup(VibratePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)

def Led(x):
	if x == 0:
		GPIO.output(Rpin, 1)
		GPIO.output(Gpin, 0)
	if x == 1:
		GPIO.output(Rpin, 0)
		GPIO.output(Gpin, 1)
	
def loop():
	state = 0
	while True:
		if GPIO.input(VibratePin)==0:
			state = state + 1
			if state > 1:
				state = 0
			Led(state)
			time.sleep(1)

def destroy():
	GPIO.output(Gpin, GPIO.HIGH)       # Green led off
	GPIO.output(Rpin, GPIO.HIGH)       # Red led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

