#---------------------------------------------------------
#
#		This is a program for Barometer Pressure Sensor
#	Module. It could measure the pressure and temperature.
#
#		This program depend on BMP085.py writted by 
#	Adafruit. 
#
#	   Barometer Module			   Pi
#			VCC ----------------- 3.3V
#			GND ------------------ GND
#			SCL ----------------- SCL1
#			SDA ----------------- SDA1
#
#---------------------------------------------------------
#!/usr/bin/env python3

import Adafruit_BMP.BMP085 as BMP085
import time

def setup():
	print ('\n Barometer begins...')

def loop():
	while True:
		sensor = BMP085.BMP085()
		temp = sensor.read_temperature()	# Read temperature to veriable temp
		pressure = sensor.read_pressure()	# Read pressure to veriable pressure

		print ('')
		print ('      Temperature = {0:0.2f} C'.format(temp))		# Print temperature
		print ('      Pressure = {0:0.2f} Pa'.format(pressure))	# Print pressure
		time.sleep(1)			
		print ('')

def destroy():
	pass

if __name__ == '__main__':		# Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()