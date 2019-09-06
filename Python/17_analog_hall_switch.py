#/usr/bin/env python3
import RPi.GPIO as GPIO
import PCF8591 as ADC
import time

def setup():
	ADC.setup(0x48)

def Print(x):
	if x == 0:
		print ('')
		print ('*************')
		print ('* No Magnet *')
		print ('*************')
		print ('')
	if x == 1:
		print ('')
		print ('****************')
		print ('* Magnet North *')
		print ('****************')
		print ('')
	if x == -1:
		print ('')
		print ('****************')
		print ('* Magnet South *')
		print ('****************')
		print ('')

def loop():
	status = 0
	while True:
		res = ADC.read(0)
		print ('Current intensity of magnetic field : ', res)
		if res - 133 < 5 and res - 133 > -5:
			tmp = 0
		if res < 128:
			tmp = -1
		if res > 138:
			tmp = 1
		if tmp != status:
			Print(tmp)
			status = tmp
		time.sleep(0.2)

if __name__ == '__main__':
	setup()
	loop()

