#include <wiringPi.h>
#include <stdio.h>

typedef unsigned char uchar;
typedef unsigned int uint;

#define     ADC_CS    0
#define     ADC_CLK   1
#define     ADC_DIO   2

uchar get_ADC_Result(void)
{
	uchar i;
	uchar dat1=0, dat2=0;

	digitalWrite(ADC_CS, 0);
	digitalWrite(ADC_CLK,0);
	digitalWrite(ADC_DIO,1);	delayMicroseconds(2);
	digitalWrite(ADC_CLK,1);	delayMicroseconds(2);

	digitalWrite(ADC_CLK,0);	
	digitalWrite(ADC_DIO,1);    delayMicroseconds(2);
	digitalWrite(ADC_CLK,1);	delayMicroseconds(2);

	digitalWrite(ADC_CLK,0);	
	digitalWrite(ADC_DIO,0);	delayMicroseconds(2);
	digitalWrite(ADC_CLK,1);	
	digitalWrite(ADC_DIO,1);    delayMicroseconds(2);
	digitalWrite(ADC_CLK,0);	
	digitalWrite(ADC_DIO,1);    delayMicroseconds(2);
	
	for(i=0;i<8;i++)
	{
		digitalWrite(ADC_CLK,1);	delayMicroseconds(2);
		digitalWrite(ADC_CLK,0);    delayMicroseconds(2);

		pinMode(ADC_DIO, INPUT);
		dat1=dat1<<1 | digitalRead(ADC_DIO);
	}
	
	for(i=0;i<8;i++)
	{
		dat2 = dat2 | ((uchar)(digitalRead(ADC_DIO))<<i);
		digitalWrite(ADC_CLK,1); 	delayMicroseconds(2);
		digitalWrite(ADC_CLK,0);    delayMicroseconds(2);
	}

	digitalWrite(ADC_CS,1);
	
	return(dat1==dat2) ? dat1 : 0;
}

int main(void)
{
	uchar analogVal;
	uchar illum;

	if(wiringPiSetup() == -1){ //when initialize wiring failed,print messageto screen
		printf("setup wiringPi failed !");
		return 1; 
	}

	pinMode(ADC_CS,  OUTPUT);
	pinMode(ADC_CLK, OUTPUT);

	while(1){
		pinMode(ADC_DIO, OUTPUT);

		analogVal = get_ADC_Result();
		illum = 210 - analogVal;
		printf("Current illumination : %d\n", illum);
		delay(500);
	}

	return 0;
}
