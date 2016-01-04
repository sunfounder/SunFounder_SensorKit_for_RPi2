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
		case 1:
			printf("\n*********\n"  );
			printf(  "* Saft~ *\n"  );
			printf(  "*********\n\n");
		break;
		case 0:
			printf("\n*********\n"  );
			printf(  "* Fire! *\n"  );
			printf(  "*********\n\n");
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
	int analogVal;
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
		analogVal = analogRead(PCF + 0);
		printf("%d\n", analogVal);

		tmp = digitalRead(DOpin);

		if (tmp != status)
		{
			Print(tmp);
			status = tmp;
		}

		delay (200);
	}
	return 0;
}
