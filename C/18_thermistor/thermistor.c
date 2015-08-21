#include <stdio.h>
#include <wiringPi.h>
#include <pcf8591.h>
#include <math.h>

#define		PCF     120
#define		DOpin	0

void Print(int x)
{
	switch(x)
	{
		case 0:
			printf("\n************\n"  );
			printf(  "* Too Hot! *\n"  );
			printf(  "************\n\n");
		break;
		case 1:
			printf("\n***********\n"  );
			printf(  "* Better~ *\n"  );
			printf(  "***********\n\n");
		break;
		default:
			printf("\n**********************\n"  );
			printf(  "* Print value error. *\n"  );
			printf(  "**********************\n\n");
		break;
	}
}

int main()
{
	unsigned char analogVal;
	double Vr, Rt, temp;
	int tmp, status;
	
	if(wiringPiSetup() == -1){
		printf("setup wiringPi failed !");
		return 1;
	}
	// Setup pcf8591 on base pin 120, and address 0x48
	pcf8591Setup(PCF, 0x48);

	pinMode(DOpin, INPUT);

	status = 0;
	while(1) // loop forever
	{
		printf("loop");
		analogVal = analogRead(PCF + 0);
		Vr = 5 * (double)(analogVal) / 255;
		Rt = 10000 * (double)(Vr) / (5 - (double)(Vr));
		temp = 1 / (((log(Rt/10000)) / 3950)+(1 / (273.15 + 25)));
		temp = temp - 273.15;
		printf("Current temperature : %lf\n", temp);
		
		// For a threshold, uncomment one of the code for
		// which module you use. DONOT UNCOMMENT BOTH!
		//---------------------------------------------
		// 1. For Analog Temperature module(with DO)
		tmp = digitalRead(DOpin);

        // 2. For Thermister module(with sig pin)
        // if (temp > 33) tmp = 0;
        // else if (temp < 31) tmp = 1;
		//---------------------------------------------

		if (tmp != status)
		{
			Print(tmp);
			status = tmp;
		}

		delay (200);
	}
	return 0;
}
