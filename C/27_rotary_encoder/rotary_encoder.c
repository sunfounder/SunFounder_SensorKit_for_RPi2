#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <stdlib.h>
#include <wiringPi.h>

#define  RoAPin    0
#define  RoBPin    1
#define  SWPin     2

static volatile int globalCounter = 0 ;

unsigned char flag;
unsigned char Last_RoB_Status;
unsigned char Current_RoB_Status;

void btnISR(void)
{
	globalCounter = 0;
}

void rotaryDeal(void)
{
	Last_RoB_Status = digitalRead(RoBPin);

	while(!digitalRead(RoAPin)){
		Current_RoB_Status = digitalRead(RoBPin);
		flag = 1;
	}

	if(flag == 1){
		flag = 0;
		if((Last_RoB_Status == 0)&&(Current_RoB_Status == 1)){
			globalCounter ++;	
		}
		if((Last_RoB_Status == 1)&&(Current_RoB_Status == 0)){
			globalCounter --;
		}
	}
}

int main(void)
{
	if(wiringPiSetup() < 0){
		fprintf(stderr, "Unable to setup wiringPi:%s\n",strerror(errno));
		return 1;
	}

	pinMode(SWPin, INPUT);
	pinMode(RoAPin, INPUT);
	pinMode(RoBPin, INPUT);

	pullUpDnControl(SWPin, PUD_UP);

    if(wiringPiISR(SWPin, INT_EDGE_FALLING, &btnISR) < 0){
		fprintf(stderr, "Unable to init ISR\n",strerror(errno));	
		return 1;
	}
	
	int tmp = 0;

	while(1){
		rotaryDeal();
		if (tmp != globalCounter){
			printf("%d\n", globalCounter);
			tmp = globalCounter;
		}
	}

	return 0;
}
