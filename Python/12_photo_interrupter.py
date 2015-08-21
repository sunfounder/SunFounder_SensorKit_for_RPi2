#!/usr/bin/env python
import RPi.GPIO as GPIO

PIPin  = 11
Gpin   = 12
Rpin   = 13

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(Gpin, GPIO.OUT)     # Set Green Led Pin mode to output
	GPIO.setup(Rpin, GPIO.OUT)     # Set Red Led Pin mode to output
	GPIO.setup(PIPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	GPIO.add_event_detect(PIPin, GPIO.BOTH, callback=detect, bouncetime=200)

def Led(x):
	if x == 0:
		GPIO.output(Rpin, 1)
		GPIO.output(Gpin, 0)
	if x == 1:
		GPIO.output(Rpin, 0)
		GPIO.output(Gpin, 1)

def Print(x):
	if x == 1:
		print '    *************************'
		print '    *   Light was blocked   *'
		print '    *************************'

def detect(chn):
	Led(GPIO.input(PIPin))
	Print(GPIO.input(PIPin))

def loop():
	while True:
		pass

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

