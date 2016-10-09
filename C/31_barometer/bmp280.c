/**********************************************************************
* Filename    : bmp280.c
* Description : Simple use for bmp280 through i2c bus
* Author      : Cavon
* Brand       : SunFounder
* E-mail      : support@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Cavon    2016-10-09    New release
**********************************************************************/

#include <stdio.h>
#include <wiringPiI2C.h>
#include <math.h>

#define QNH             1020

// Power mode
//#define POWER_MODE    0   // sleep mode
//#define POWER_MODE    1   // forced mode
//#define POWER_MODE    2   // forced mode
#define POWER_MODE      3   // normal mode

// Temperature resolution
//#define OSRS_T    0    // skipped
//#define OSRS_T    1    // 16 Bit
//#define OSRS_T    2    // 17 Bit
//#define OSRS_T    3    // 18 Bit
//#define OSRS_T    4    // 19 Bit
#define OSRS_T      5    // 20 Bit

// Pressure resolution
//#define OSRS_P    0   // pressure measurement skipped
//#define OSRS_P    1   // 16 Bit ultra low power
//#define OSRS_P    2   // 17 Bit low power
//#define OSRS_P    3   // 18 Bit standard resolution
//#define OSRS_P    4   // 19 Bit high resolution
#define OSRS_P      5   // 20 Bit ultra high resolution

// Filter settings
//#define FILTER    0   //
//#define FILTER    1   //
//#define FILTER    2   //
//#define FILTER    3   //
#define FILTER      4   //
//#define FILTER    5   //
//#define FILTER    6   //
//#define FILTER    7   //

// Standby settings
//#define T_SB      0     // 000 0,5ms
//#define T_SB      1     // 001 62.5 ms
//#define T_SB      2     // 010 125 ms
//#define T_SB      3     // 011 250ms
#define T_SB        4     // 100 500ms
//#define T_SB      5     // 101 1000ms
//#define T_SB      6     // 110 2000ms
//#define T_SB      7     // 111 4000ms

#define BMP280_REGISTER_DIG_T1				0x88
#define BMP280_REGISTER_DIG_T2				0x8A
#define BMP280_REGISTER_DIG_T3				0x8C
#define BMP280_REGISTER_DIG_P1				0x8E
#define BMP280_REGISTER_DIG_P2				0x90
#define BMP280_REGISTER_DIG_P3				0x92
#define BMP280_REGISTER_DIG_P4				0x94
#define BMP280_REGISTER_DIG_P5				0x96
#define BMP280_REGISTER_DIG_P6				0x98
#define BMP280_REGISTER_DIG_P7				0x9A
#define BMP280_REGISTER_DIG_P8				0x9C
#define BMP280_REGISTER_DIG_P9				0x9E
#define BMP280_REGISTER_CHIPID				0xD0
#define BMP280_REGISTER_VERSION				0xD1
#define BMP280_REGISTER_SOFTRESET			0xE0
#define BMP280_REGISTER_CONTROL				0xF4
#define BMP280_REGISTER_CONFIG				0xF5
#define BMP280_REGISTER_STATUS				0xF3
#define BMP280_REGISTER_TEMPDATA_MSB		0xFA
#define BMP280_REGISTER_TEMPDATA_LSB		0xFB
#define BMP280_REGISTER_TEMPDATA_XLSB		0xFC
#define BMP280_REGISTER_PRESSDATA_MSB		0xF7
#define BMP280_REGISTER_PRESSDATA_LSB		0xF8
#define BMP280_REGISTER_PRESSDATA_XLSB		0xF9

int CONFIG = (T_SB <<5) + (FILTER <<2); // combine bits for config
int CTRL_MEAS = (OSRS_T <<5) + (OSRS_P <<2) + POWER_MODE; // combine bits for ctrl_meas

int bmp280 = 0;
struct {
	int chip_id;
	int chip_version;
	double temperature;
	double pressure;
	double altitude;
} bmp;

int dig_T1 = 0;
int dig_T2 = 0;
int dig_T3 = 0;
int dig_P1 = 0;
int dig_P2 = 0;
int dig_P3 = 0;
int dig_P4 = 0;
int dig_P5 = 0;
int dig_P6 = 0;
int dig_P7 = 0;
int dig_P8 = 0;
int dig_P9 = 0;

void write_byte_data(int reg, int value){
	wiringPiI2CWriteReg8(bmp280, reg, value);
}

int read_byte_data(int reg){
	int result;
	result = wiringPiI2CReadReg8(bmp280, reg);
	return result;
}

int read_word_data_unsigned(int reg){
	int result;
	result = wiringPiI2CReadReg16(bmp280, reg);
	return result;
}

int read_word_data_signed(int reg){
	int result;
	result = read_word_data_unsigned(reg);
	if (result > 32767){
		result -= 65536;
	}
	return result;
}

void read_id(self){
	int REG_ID     = 0xD0;
	int result;
	result = read_word_data_unsigned(REG_ID);
	bmp.chip_id = result & 0x00FF;
	bmp.chip_version = result >> 8;
}

void reg_check(self){
	write_byte_data(BMP280_REGISTER_SOFTRESET, 0xB6);
	delay(200);
	write_byte_data(BMP280_REGISTER_CONTROL, CTRL_MEAS);
	delay(200);
	write_byte_data(BMP280_REGISTER_CONFIG, CONFIG);
	delay(200);

	dig_T1 = read_word_data_unsigned(BMP280_REGISTER_DIG_T1); // read correction settings
	dig_T2 = read_word_data_signed(BMP280_REGISTER_DIG_T2);
	dig_T3 = read_word_data_signed(BMP280_REGISTER_DIG_T3);
	dig_P1 = read_word_data_unsigned(BMP280_REGISTER_DIG_P1);
	dig_P2 = read_word_data_signed(BMP280_REGISTER_DIG_P2);
	dig_P3 = read_word_data_signed(BMP280_REGISTER_DIG_P3);
	dig_P4 = read_word_data_signed(BMP280_REGISTER_DIG_P4);
	dig_P5 = read_word_data_signed(BMP280_REGISTER_DIG_P5);
	dig_P6 = read_word_data_signed(BMP280_REGISTER_DIG_P6);
	dig_P7 = read_word_data_signed(BMP280_REGISTER_DIG_P7);
	dig_P8 = read_word_data_signed(BMP280_REGISTER_DIG_P8);
	dig_P9 = read_word_data_signed(BMP280_REGISTER_DIG_P9);
}

void read(){
	int raw_temperature_msb, raw_temperature_lsb, raw_temperature_xlsb;
	int raw_pressure_msb, raw_pressure_lsb, raw_pressure_xlsb;
	int raw_temperature;
	int raw_pressure;
	double var1, var2, temperature, t_fine, pressure, altitude;

	raw_temperature_msb = read_byte_data(BMP280_REGISTER_TEMPDATA_MSB); // read raw temperature msb
	raw_temperature_lsb = read_byte_data(BMP280_REGISTER_TEMPDATA_LSB); // read raw temperature lsb
	raw_temperature_xlsb = read_byte_data(BMP280_REGISTER_TEMPDATA_XLSB); // read raw temperature xlsb
	raw_pressure_msb = read_byte_data(BMP280_REGISTER_PRESSDATA_MSB); // read raw pressure msb
	raw_pressure_lsb = read_byte_data(BMP280_REGISTER_PRESSDATA_LSB); // read raw pressure lsb
	raw_pressure_xlsb = read_byte_data(BMP280_REGISTER_PRESSDATA_XLSB); // read raw pressure xlsb

	raw_temperature=(raw_temperature_msb <<12)+(raw_temperature_lsb<<4)+(raw_temperature_xlsb>>4); // combine 3 bytes  msb 12 bits left, lsb 4 bits left, xlsb 4 bits right
	raw_pressure=(raw_pressure_msb <<12)+(raw_pressure_lsb <<4)+(raw_pressure_xlsb >>4); // combine 3 bytes  msb 12 bits left, lsb 4 bits left, xlsb 4 bits right

	var1=(raw_temperature/16384.0-dig_T1/1024.0)*dig_T2; // formula for temperature from datasheet
	var2=(raw_temperature/131072.0-dig_T1/8192.0)*(raw_temperature/131072.0-dig_T1/8192.0)*dig_T3; // formula for temperature from datasheet
	temperature=(var1+var2)/5120.0; // formula for temperature from datasheet
	t_fine=(var1+var2); // need for pressure calculation

	var1=t_fine/2.0-64000.0; // formula for pressure from datasheet
	var2=var1*var1*dig_P6/32768.0; // formula for pressure from datasheet
	var2=var2+var1*dig_P5*2; // formula for pressure from datasheet
	var2=var2/4.0+dig_P4*65536.0; // formula for pressure from datasheet
	var1=(dig_P3*var1*var1/524288.0+dig_P2*var1)/524288.0; // formula for pressure from datasheet
	var1=(1.0+var1/32768.0)*dig_P1; // formula for pressure from datasheet
	pressure=1048576.0-raw_pressure; // formula for pressure from datasheet
	pressure=(pressure-var2/4096.0)*6250.0/var1; // formula for pressure from datasheet
	var1=dig_P9*pressure*pressure/2147483648.0; // formula for pressure from datasheet
	var2=pressure*dig_P8/32768.0; // formula for pressure from datasheet
	pressure=pressure+(var1+var2+dig_P7)/16.0; // formula for pressure from datasheet

	//altitude= 44330.0 * (1.0 - pow(pressure / (QNH*100), (1.0/5.255))); // formula for altitude from airpressure

	bmp.temperature = temperature;
	bmp.pressure = pressure / 100.0;
}

void main(){
	int address = 0x77;
	bmp280 = wiringPiI2CSetup(address);
	while (1){
		read_id();

		if(bmp.chip_id == 88){
			reg_check();
			read();
			printf("Temperature : %2.2f `C\n", bmp.temperature);
			printf("Pressure    : %5.4f mbar\n\n", bmp.pressure);
		}
		else{
			printf("Error\n");
			// Chip ID should be 88
			printf("Chip ID     : %d\n", bmp.chip_id);
			printf("Version     : %d\n", bmp.chip_version);
			delay(1000);
		}
	}
}
