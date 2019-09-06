#!/usr/bin/env python3
import RPi.GPIO as GPIO

TrackPin = 11
LedPin   = 12

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
	GPIO.setup(TrackPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to off led

def loop():
	while True:
		if GPIO.input(TrackPin) == GPIO.LOW:
			print ('White line is detected')
			GPIO.output(LedPin, GPIO.LOW)  # led on
		else:
			print ('...Black line is detected')
			GPIO.output(LedPin, GPIO.HIGH) # led off

def destroy():
	GPIO.output(LedPin, GPIO.HIGH)     # led off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

