#include <wiringPi.h>
#include <stdio.h>

#define LaserPin    0

int main(void)
{
	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}
	//printf("linker LedPin : GPIO %d(wiringPi pin)\n",LedPin); //when initialize wiring successfully,print message to screen

	pinMode(LaserPin, OUTPUT);

	while(1){
		digitalWrite(LaserPin, HIGH);
		delay(500);
		digitalWrite(LaserPin, LOW);
		delay(500);
	}

	return 0;
}
