#!/usr/bin/env python3
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
#			SCL ---------------- GPIO23
#			I/O ---------------- GPIO24
#			RST ---------------- GPIO25
#
#-----------------------------------------------------
from datetime import datetime
from ds1302 import DS1302
from sys import version_info
import time

if version_info.major == 2:
	input = raw_input

rtc = DS1302()

def setup():
	print ('')
	print ('')
	print (rtc.get_datetime())
	print ('')
	print ('')
	a = input( "Do you want to setup date and time?(y/n) ")
	if a == 'y' or a == 'Y':
		date = input("Input date:(YYYY MM DD) ")
		time = input("Input time:(HH MM SS) ")
		date = list(map(lambda x: int(x), date.split()))
		time = list(map(lambda x: int(x), time.split()))
		print ('')
		print ('')
		rtc.set_datetime(datetime(date[0], date[1], date[2], time[0], time[1], time[2]))
		dt = rtc.get_datetime()
		print ("You set the date and time to:", dt)

def loop():
	while True:
		a = rtc.get_datetime()
		print (a)
		time.sleep(0.5)

def destory():
	pass				# Release resource

if __name__ == '__main__':		# Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  	# When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destory()