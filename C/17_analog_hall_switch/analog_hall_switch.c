#include <stdio.h>
#include <wiringPi.h>
#include <pcf8591.h>

#define PCF       120

int main (void)
{
	int res, tmp, status;
	wiringPiSetup ();
	// Setup pcf8591 on base pin 120, and address 0x48
	pcf8591Setup (PCF, 0x48);
	status = 0;
	while(1) // loop forever
	{
		res = analogRead(PCF + 0);
		printf("Current intensity of magnetic field : %d\n", res);
		if (res - 133 < 5 || res - 133 > -5) 
			tmp = 0;
		if (res < 128) tmp = -1;
		if (res > 138) tmp =  1;
		if (tmp != status)
		{
			switch(tmp)
			{
				case 0:
					printf("\n*****************\n"  );
					printf(  "* Magnet: None. *\n"  );
					printf(  "*****************\n\n");
					break;
				case -1:
					printf("\n******************\n"  );
					printf(  "* Magnet: North. *\n"  );
					printf(  "******************\n\n");
					break;
				case 1:
					printf("\n******************\n"  );
					printf(  "* Magnet: South. *\n"  );
					printf(  "******************\n\n");
					break;
			}
			status = tmp;
		}
		delay (200);
	}
	return 0 ;
}
