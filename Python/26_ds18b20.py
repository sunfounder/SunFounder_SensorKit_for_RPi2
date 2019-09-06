#!/usr/bin/env python3
#----------------------------------------------------------------
#	Note:
#		ds18b20's data pin must be connected to pin7.
#		replace the 28-XXXXXXXXX as yours.
#----------------------------------------------------------------
import os

ds18b20 = ''

def setup():
	global ds18b20
	for i in os.listdir('/sys/bus/w1/devices'):
		if i != 'w1_bus_master1':
			ds18b20 = '28-031590bf4aff'

def read():
#	global ds18b20
	location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
	tfile = open(location)
	text = tfile.read()
	tfile.close()
	secondline = text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
	temperature = temperature / 1000
	return temperature
	
def loop():
	while True:
		if read() != None:
			print ("Current temperature : %0.3f C" % read())

def destroy():
	pass

if __name__ == '__main__':
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()

