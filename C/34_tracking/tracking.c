#include <wiringPi.h>
#include <stdio.h>

#define TrackSensorPin    0
#define LedPin            1

int main(void)
{
	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}
	
	pinMode(TrackSensorPin, INPUT);
	pinMode(LedPin,  OUTPUT);

	while(1){
		if(digitalRead(TrackSensorPin) == LOW){
			printf("White line is detected\n");
			digitalWrite(LedPin, LOW);     //led on
			delay(100);
			digitalWrite(LedPin, HIGH);    //led off
		}	
		else{
			printf("...Black line is detected\n");
			delay(100);
		}
	}

	return 0;
}

