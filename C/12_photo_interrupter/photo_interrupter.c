#include <wiringPi.h>
#include <stdio.h>

#define LBPin		0  // light break pin set to GPIO0
#define Gpin		1
#define Rpin		2

void LED(int color)
{
	pinMode(Gpin, OUTPUT);
	pinMode(Rpin, OUTPUT);
	if (color == 0){
		digitalWrite(Rpin, HIGH);
		digitalWrite(Gpin, LOW);
	}
	else if (color == 1){
		digitalWrite(Rpin, LOW);
		digitalWrite(Gpin, HIGH);
	}
}

void Print(int x){
	if ( x == 0 ){
		printf("Light was blocked\n");
	}
}

int main(void){

	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}

	pinMode(LBPin, INPUT);
	int temp;
	while(1){
		//Reverse the input of LBPin
		if ( digitalRead(LBPin) == 0 ){  
			temp = 1;
		}
		if ( digitalRead(LBPin) == 1 ){
			temp = 0;
		}

		LED(temp);
		Print(temp);
	}
	return 0;
}
