#include <wiringPi.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>
#include <stdio.h>
#include <pcf8591.h>

#define     LedRed		0
#define     LedGreen	1
#define     LedBlue		2

#define     PCF			120

#define		Beep		3 

#define		BUFSIZE		128

typedef unsigned char uchar;
typedef unsigned int  uint;

static int sys_state = 1; 

static int AIN0 = PCF + 0;
static int AIN1 = PCF + 1;
static int AIN2 = PCF + 2;

void beepInit(void)
{
	pinMode(Beep, OUTPUT);	
}

void beep_on(void)
{
	digitalWrite(Beep, LOW);	
}

void beep_off(void)
{	
	digitalWrite(Beep, HIGH);	
}

void beepCtrl(int t)
{
	beep_on();
	delay(t);
	beep_off();
	delay(t);
}

float tempRead(void)
{
	float temp;
	int i, j;
    int fd;
	int ret;

	char buf[BUFSIZE];
	char tempBuf[5];
	
	fd = open("/sys/bus/w1/devices/28-031467805fff/w1_slave", O_RDONLY);

	if(-1 == fd){
		perror("open device file error");
		return 1;
	}

	while(1){
		ret = read(fd, buf, BUFSIZE);
		if(0 == ret){
			break;	
		}
		if(-1 == ret){
			if(errno == EINTR){
				continue;	
			}
			perror("read()");
			close(fd);
			return 1;
		}
	}

	for(i=0;i<sizeof(buf);i++){
		if(buf[i] == 't'){
			for(j=0;j<sizeof(tempBuf);j++){
				tempBuf[j] = buf[i+2+j]; 	
			}
		}	
	}

	temp = (float)atoi(tempBuf) / 1000;

	close(fd);

	return temp;
}

void ledInit(void)
{
	pinMode(LedRed,   OUTPUT);	
	pinMode(LedGreen, OUTPUT);	
	pinMode(LedBlue,  OUTPUT);	
}

/* */
void ledCtrl(int n, int state)
{
	digitalWrite(n, state);
}

void joystickquit(void)
{
	sys_state = 0;
	printf("interrupt occur !\n");
}

uchar get_joyStick_state(void)
{
	uchar tmp = 0;
	uchar xVal = 0, yVal = 0, zVal = 0;
	
	xVal = analogRead(AIN1);
	if(xVal >= 250){
		tmp = 1;
	}
	if(xVal <= 5){
		tmp = 2;
	}

	yVal = analogRead(AIN0);
	if(yVal >= 250){
		tmp = 4;
	}
	if(yVal <= 5){
		tmp = 3;
	}
	
	zVal = analogRead(AIN2);
	if(zVal <= 5){
		tmp = 5;
	}

	if(xVal-127<30 && xVal-127>-30 && yVal-127<30 && yVal-127>-30 && zVal>127){
		tmp = 0;
	}
// Uncomment this line to see the value of joystick.
//	printf("x = %d, y = %d, z = %d",xVal,yVal,zVal);
	return tmp;
}

int main(void)
{
	int i;
	uchar joyStick = 0;
	float temp;
	uchar low = 26, high = 30;

	if(wiringPiSetup() == -1){
		printf("setup wiringPi failed !");
		return 1; 
	}
	
	pcf8591Setup(PCF, 0x48);
	ledInit();
	beepInit();
	
	printf("System is running...\n");

	while(1){
		flag:
		joyStick = get_joyStick_state();

		switch(joyStick){
			case 1 : --low;  break; 
			case 2 : ++low;  break;
			case 3 : ++high; break;
			case 4 : --high; break;
			case 5 : joystickquit(); break;
			default: break;
		}
		
		if(low >= high){
			printf("Error, lower limit should be less than upper limit\n");
			goto flag;
		}

		printf("The lower limit of temperature : %d\n", low);
		printf("The upper limit of temperature : %d\n", high);
		
		temp = tempRead();
		
		printf("Current temperature : %0.3f\n", temp);
		
		if(temp < low){
			ledCtrl(LedBlue,  LOW);
			ledCtrl(LedRed,   HIGH);
			ledCtrl(LedGreen, LOW);
			for(i = 0;i < 3; i++){
				beepCtrl(400);
			}
		}
		if(temp >= low && temp < high){
			ledCtrl(LedBlue,  HIGH);
			ledCtrl(LedRed,   HIGH);
			ledCtrl(LedGreen, LOW);
		}
		if(temp >= high){
			ledCtrl(LedBlue,  HIGH);
			ledCtrl(LedRed,   LOW);
			ledCtrl(LedGreen, HIGH);
			for(i = 0;i < 3; i++){
				beepCtrl(80);
			}
		}

		if(sys_state == 0){
			ledCtrl(LedRed, LOW);
			ledCtrl(LedGreen, LOW);
			ledCtrl(LedBlue, LOW);
			beep_off();
			printf("SyStem will be off...\n");
			break;
		}
	}
	return 0;
}
