#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

RoAPin = 11    # CLK Pin
RoBPin = 12    # DT Pin
BtnPin = 13    # Button Pin

globalCounter = 0

flag = 0
Last_RoB_Status = 0
Current_RoB_Status = 0

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(RoAPin, GPIO.IN)    # input mode
	GPIO.setup(RoBPin, GPIO.IN)
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def rotaryDeal():
	global flag
	global Last_RoB_Status
	global Current_RoB_Status
	global globalCounter
	Last_RoB_Status = GPIO.input(RoBPin)
	while(not GPIO.input(RoAPin)):
		Current_RoB_Status = GPIO.input(RoBPin)
		flag = 1
	if flag == 1:
		flag = 0
		if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
			globalCounter = globalCounter + 1
		if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
			globalCounter = globalCounter - 1

def btnISR(channel):
	global globalCounter
	globalCounter = 0

def loop():
	global globalCounter
	tmp = 0	# Rotary Temperary

	GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=btnISR)
	while True:
		rotaryDeal()
		if tmp != globalCounter:
			print ('globalCounter = %d' % globalCounter)
			tmp = globalCounter

def destroy():
	GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

