#!/usr/bin/env python
import Adafruit_DHT as DHT
import RPi.GPIO as GPIO

Sensor = 11
humiture = 17
def setup():
	print 'Setting up, please wait...'

def loop():
	while True:
		humidity, temperature = DHT.read_retry(Sensor, humiture)

		if humidity is not None and temperature is not None:
			print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
		else:
			print 'Failed to get reading. Try again!'

def destroy():
	GPIO.cleanup()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
