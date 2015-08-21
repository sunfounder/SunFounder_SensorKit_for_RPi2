#include <wiringPi.h>
#include <stdio.h>

#define    IR    0

int cnt = 0;

void myISR(void)
{
	printf("Received infrared. cnt = %d\n", ++cnt);	
}

int main(void)
{
	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}
	
	if(wiringPiISR(IR, INT_EDGE_FALLING, &myISR) == -1){
		printf("setup ISR failed !");
		return 1;
	}

	//pinMode(IR, INPUT);

	while(1);
	
	return 0;
}
