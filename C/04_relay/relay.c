#include <wiringPi.h>
#include <stdio.h>

#define RelayPin      0

int main(void)
{
	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}
//	printf("linker LedPin : GPIO %d(wiringPi pin)\n",VoicePin); //when initialize wiring successfully,print message to screen
	
	pinMode(RelayPin, OUTPUT);

	while(1){
			digitalWrite(RelayPin, LOW);			
			delay(1000);
			digitalWrite(RelayPin, HIGH);
			delay(1000);
	}

	return 0;
}

