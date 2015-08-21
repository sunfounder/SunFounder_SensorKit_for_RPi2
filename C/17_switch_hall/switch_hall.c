#include <wiringPi.h>
#include <stdio.h>

#define HallPin		0
#define Gpin		1
#define Rpin		2

void LED(char* color)
{
	pinMode(Gpin, OUTPUT);
	pinMode(Rpin, OUTPUT);
	if (color == "RED")
	{
		digitalWrite(Rpin, HIGH);
		digitalWrite(Gpin, LOW);
	}
	else if (color == "GREEN")
	{
		digitalWrite(Rpin, LOW);
		digitalWrite(Gpin, HIGH);
	}
	else
		printf("LED Error");
}

int main(void)
{
	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}

	pinMode(HallPin, INPUT);
	LED("GREEN");
	
	while(1){
		if(0 == digitalRead(HallPin)){
			delay(10);
			if(0 == digitalRead(HallPin)){
				LED("RED");	
				printf("Button is pressed\n");	
			}
		}
		else if(1 == digitalRead(HallPin)){
			delay(10);
			if(1 == digitalRead(HallPin)){
				while(!digitalRead(HallPin));
				LED("GREEN");
			}
		}
	}
	return 0;
}
