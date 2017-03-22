#include  <wiringPiI2C.h>
#include  <stdio.h>
#include  <math.h>

int fd;
int acclX, acclY, acclZ;
int gyroX, gyroY, gyroZ;
double acclX_scaled, acclY_scaled, acclZ_scaled;
double gyroX_scaled, gyroY_scaled, gyroZ_scaled;

int read_word_2c(int addr)
{
  int val;
  val = wiringPiI2CReadReg8(fd, addr);
  val = val << 8;
  val += wiringPiI2CReadReg8(fd, addr+1);
  if (val >= 0x8000)
    val = -(65536 - val);

  return val;
}

int main()
{
  fd = wiringPiI2CSetup (0x68);
  wiringPiI2CWriteReg8 (fd,0x6B,0x00);//disable sleep mode 
  printf("set 0x6B=%X\n",wiringPiI2CReadReg8 (fd,0x6B));
  
  while(1) {

    gyroX = read_word_2c(0x43);
    gyroY = read_word_2c(0x45);
    gyroZ = read_word_2c(0x47);

    gyroX_scaled = gyroX / 131.0;
    gyroY_scaled = gyroY / 131.0;
    gyroZ_scaled = gyroZ / 131.0;
    
    printf("My gyroX_scaled: %f\n", gyroX_scaled);
    printf("My gyroY_scaled: %f\n", gyroY_scaled);
    printf("My gyroZ_scaled: %f\n", gyroZ_scaled);

    
    delay(100);
  }
  return 0;
}
