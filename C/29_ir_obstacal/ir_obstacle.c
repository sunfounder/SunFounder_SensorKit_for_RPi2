#include <wiringPi.h>
#include <stdio.h>

#define ObstaclePin      0

void myISR(void)
{
	printf("Detected Barrier !\n");
}

int main(void)
{
	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !\n");
		return 1; 
	}
	
	if(wiringPiISR(ObstaclePin, INT_EDGE_FALLING, &myISR) < 0){
		printf("Unable to setup ISR !!!\n");
		return 1;
	}
	
	while(1){
		;
	}

	return 0;
}

