#!/usr/bin/env python3
import RPi.GPIO as GPIO

IrPin  = 11
count = 0

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(IrPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def cnt(ev=None):
	global count
	count += 1
	print ('Received infrared. cnt = ', count)

def loop():
	GPIO.add_event_detect(IrPin, GPIO.FALLING, callback=cnt) # wait for falling
	while True:
		pass   # Don't do anything

def destroy():
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

