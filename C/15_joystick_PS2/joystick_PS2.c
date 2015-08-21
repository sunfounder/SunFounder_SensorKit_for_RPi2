#include <stdio.h>
#include <wiringPi.h>
#include <pcf8591.h>

#define PCF       120
#define uchar	unsigned char

int AIN0 = PCF + 0;
int AIN1 = PCF + 1;
int AIN2 = PCF + 2;

char *state[6] = {"home", "up", "down", "left", "right", "pressed"};

int direction(){
	int x, y, b;
	int tmp;
	x = analogRead(AIN1);
	y = analogRead(AIN0);
	b = analogRead(AIN2);
	if (y == 0)
		tmp = 1;		// up
	if (y == 255)
		tmp = 2;		// down
	
	if (x == 255)
		tmp = 3;		// left
	if (x == 0)
		tmp = 4;		// right

	if (b == 0)
		tmp = 5;		// button preesd
	if (x-125<15 && x-125>-15 && y-125<15 && y-125>-15 && b == 255)
		tmp = 0;		// home position
	
	return tmp;
}

int main (void)
{
	int tmp;
	int status = 0;
	wiringPiSetup ();
	// Setup pcf8591 on base pin 120, and address 0x48
	pcf8591Setup (PCF, 0x48);
	while(1) // loop forever
	{
		tmp = direction();
		if (tmp != status)
		{
			printf("%s\n", state[tmp]);
			status = tmp;
		}
	}
	return 0 ;
}
