import lirc
import time
import RPi.GPIO as GPIO

# client = lirc.Client()
# print(client.version())

''' RGB config'''
Rpin = 17
Gpin = 18
Bpin = 27

Lv = [0, 20, 90] # Light Level
color = [0, 0, 0]

p_R = None
p_G = None
p_B = None


def setColor(color):
	# global p_R, p_G, p_B
	p_R.ChangeDutyCycle(100 - color[0])     # Change duty cycle
	p_G.ChangeDutyCycle(100 - color[1])
	p_B.ChangeDutyCycle(100 - color[2])

def x():
    setColor(color)

def setup():
	global p_R, p_G, p_B
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Rpin, GPIO.OUT)
	GPIO.setup(Gpin, GPIO.OUT)
	GPIO.setup(Bpin, GPIO.OUT)

	p_R = GPIO.PWM(Rpin, 2000) # Set Frequece to 2KHz
	p_G = GPIO.PWM(Gpin, 2000)
	p_B = GPIO.PWM(Bpin, 2000)

	p_R.start(100)
	p_G.start(100)
	p_B.start(100)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def key_handler(key:str):
    global color

    if key == 'KEY_CHANNELDOWN':
        color[0] = Lv[0]
        print ('Red OFF')

    elif key == 'KEY_CHANNEL':
        color[0] = Lv[1]
        print ('Dark Red')

    elif key == 'KEY_CHANNELUP':
        color[0] = Lv[2]
        print ('Bright Red')

    elif key == 'KEY_PREVIOUS':
        color[1] = Lv[0]
        print ('Green OFF')

    elif key == 'KEY_NEXT':
        color[1] = Lv[1]
        print ('Dark Green')

    elif key == 'KEY_PLAYPAUSE':
        color[1] = Lv[2]
        print ('Bright Green')

    elif key == 'KEY_VOLUMEDOWN':
        color[2] = Lv[0]
        print ('Blue OFF')

    elif key == 'KEY_VOLUMEUP':
        color[2] = Lv[1]
        print ('Dark Blue')

    elif key == 'KEY_EQUAL':
        color[2] = Lv[2]
        print ('Bright BLUE')

    setColor(color)

    
def loop():
    with lirc.LircdConnection(timeout=5.0) as conn:
        conn.connect()
        while True:
            try: 
                # print(conn.readline()) # 0000000000000001 00 KEY_CHANNELDOWN ./lircd.conf
                key = conn.readline().split(' ')[2] #KEY_CHANNELDOWN
                # print(key)
                key_handler(key)
            except TimeoutError:
                # print('Timeout')
                pass 

def destroy():
	p_R.stop()
	p_G.stop()
	p_B.stop()
	GPIO.output(Rpin, GPIO.HIGH)    # Turn off all leds
	GPIO.output(Gpin, GPIO.HIGH)
	GPIO.output(Bpin, GPIO.HIGH)
	GPIO.cleanup()


if __name__ == "__main__":
	try:
		setup()
		loop()
	except KeyboardInterrupt:
		destroy()
        

