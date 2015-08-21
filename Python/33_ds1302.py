#!/usr/bin/env python
#-----------------------------------------------------
#
#		This is a program for DS1302 RTC Module.
#	It provide precision timmer.
#
#		This program depend on rpi_time.py. 
#
#		ds1302 Module 			   Pi
#			VCC ------------------ 5 V (Must be 5v)
#			GND ------------------ GND
#			SCL ---------------- Pin 16
#			SDA ---------------- Pin 18
#			RST ---------------- Pin 22
#
#-----------------------------------------------------
from datetime import datetime
import ds1302
import rpi_time
import time

rtc = rpi_time.DS1302()

def setup():
	print ''
	print ''
	print rtc.get_datetime()
	print ''
	print ''
	a = raw_input( "Do you want to setup date and time?(y/n) ")
	if a == 'y' or a == 'Y':
		date = raw_input("Input date:(YYYY MM DD) ")
		time = raw_input("Input time:(HH MM SS) ")
		date = date.split()
		time = time.split()
		print ''
		print ''
		ds1302.set_date(int(date[0]), int(date[1]), int(date[2]))
		ds1302.set_time(int(time[0]), int(time[1]), int(time[2]))
		dt = rtc.get_datetime()
		print "You set the date and time to:", dt

def loop():
	while True:
		a = rtc.get_datetime()
		print a
		time.sleep(0.5)

def destory():
	GPIO.cleanup()				# Release resource

if __name__ == '__main__':		# Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destory()