#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

colors = [0xFF00, 0x00FF, 0x0FF0, 0xF00F]
pins = {'pin_R':11, 'pin_G':12}  # pins is a dict

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for i in pins:
	GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
	GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led

p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
p_G = GPIO.PWM(pins['pin_G'], 2000)

p_R.start(0)      # Initial duty Cycle = 0(leds off)
p_G.start(0)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col):   # For example : col = 0x112233
	R_val = (col & 0x1100) >> 8
	G_val = (col & 0x0011) >> 0
	
	R_val = map(R_val, 0, 255, 0, 100)
	G_val = map(G_val, 0, 255, 0, 100)
	
	p_R.ChangeDutyCycle(R_val)     # Change duty cycle
	p_G.ChangeDutyCycle(G_val)

def loop():
	while True:
		for col in colors:
			setColor(col)
			time.sleep(0.5)

def destroy():
	p_R.stop()
	p_G.stop()
	for i in pins:
		GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
