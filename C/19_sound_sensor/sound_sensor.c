#include <stdio.h>
#include <wiringPi.h>
#include <pcf8591.h>

#define PCF       120

int main (void)
{
	int value;
	int count = 0;
	wiringPiSetup ();
	// Setup pcf8591 on base pin 120, and address 0x48
	pcf8591Setup (PCF, 0x48);
	while(1) // loop forever
	{
		value = analogRead  (PCF + 0);
		printf("value: %d\n", value);
		if (value < 80){
			printf("Voice In!! \n");
		}
		delay(100);
	}
	return 0;
}
