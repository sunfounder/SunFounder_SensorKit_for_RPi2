#include <wiringPi.h>
#include <softPwm.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <lirc/lirc_client.h>
#include <time.h>

#define uchar unsigned char

#define LedPinRed    0
#define LedPinGreen  1
#define LedPinBlue   2

uchar color[3] = {0xff, 0xff, 0xff};
uchar Lv[3]    = {0xff, 0x44, 0x00};

char *keymap[21] ={
	" KEY_CHANNELDOWN ",
	" KEY_CHANNEL ",
	" KEY_CHANNELUP ",
	" KEY_PREVIOUS ",
	" KEY_NEXT ",
	" KEY_PLAYPAUSE ",
	" KEY_VOLUMEDOWN ",
	" KEY_VOLUMEUP ",
	" KEY_EQUAL ",
	" KEY_NUMERIC_0 ",
	" BTN_0 ",
	" BTN_1 ",
	" KEY_NUMERIC_1 ",
	" KEY_NUMERIC_2 ",
	" KEY_NUMERIC_3 ",
	" KEY_NUMERIC_4 ",
	" KEY_NUMERIC_5 ",
	" KEY_NUMERIC_6 ",
	" KEY_NUMERIC_7 ",
	" KEY_NUMERIC_8 ",
	" KEY_NUMERIC_9 "};

void ledInit(void)
{
	softPwmCreate(LedPinRed,  0, 100);
	softPwmCreate(LedPinGreen,0, 100);
	softPwmCreate(LedPinBlue, 0, 100);
}

void ledColorSet()
{
	softPwmWrite(LedPinRed,   color[0]);
	softPwmWrite(LedPinGreen, color[1]);
	softPwmWrite(LedPinBlue,  color[2]);
}

int key(char *code){
	int i;
	int num;
	for (i=0; i<21; i++){
		if (strstr(code, keymap[i])){
			num = i;
		}
	}
	return num + 1;
}

int RGB(int i){
	switch(i){
		case 1: color[0] = Lv[0]; printf("Red OFF\n"); break;
		case 2: color[0] = Lv[1]; printf("Light Red\n"); break;
		case 3: color[0] = Lv[2]; printf("Dark Red\n"); break;
		case 4: color[1] = Lv[0]; printf("Green OFF\n"); break;
		case 5: color[1] = Lv[1]; printf("Light Green\n"); break;
		case 6: color[1] = Lv[2]; printf("Dark Green\n"); break;
		case 7: color[2] = Lv[0]; printf("Blue OFF\n"); break;
		case 8: color[2] = Lv[1]; printf("Light Blue\n"); break;
		case 9: color[2] = Lv[2]; printf("Dark Green\n"); break;
	}
}

int main(void)
{
	struct lirc_config *config;
	int buttonTimer = millis();
	char *code;
	char *c;
	if(wiringPiSetup() == -1){
		printf("setup wiringPi failed !");
		return 1; 
	}

	if(lirc_init("lirc",1)==-1)
		exit(EXIT_FAILURE);

	ledInit();
	ledColorSet();
	
	if(lirc_readconfig(NULL,&config,NULL)==0)
	{
		while(lirc_nextcode(&code)==0)
		{
			if(code==NULL) continue;{
				if (millis() - buttonTimer  > 400){
					RGB(key(code));
					ledColorSet(color);
				}
			}
			free(code);
		}
		lirc_freeconfig(config);
	}
	lirc_deinit();
	exit(EXIT_SUCCESS);
	return 0;
}
