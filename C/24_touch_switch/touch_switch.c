#include <wiringPi.h>
#include <stdio.h>

#define TouchPin	0
#define Gpin		1
#define Rpin		2

int tmp = 0;

void LED(int color)
{
	pinMode(Gpin, OUTPUT);
	pinMode(Rpin, OUTPUT);
	if (color == 0)
	{
		digitalWrite(Rpin, HIGH);
		digitalWrite(Gpin, LOW);
	}
	else if (color == 1)
	{
		digitalWrite(Rpin, LOW);
		digitalWrite(Gpin, HIGH);
	}
	else
		printf("LED Error");
}

void Print(int x){
	if (x != tmp){
		if (x == 0)
			printf("...ON\n");
		if (x == 1)
			printf("OFF..\n");
		tmp = x;
	}
}

int main(void)
{
	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}

	pinMode(TouchPin, INPUT);
	
	while(1){
		LED(digitalRead(TouchPin));	
		Print(digitalRead(TouchPin));	
	}
	return 0;
}
