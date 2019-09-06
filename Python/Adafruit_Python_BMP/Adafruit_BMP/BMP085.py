# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import logging
import time


# BMP085 default address.
BMP085_I2CADDR           = 0x77

# Operating Modes
BMP085_ULTRALOWPOWER     = 0
BMP085_STANDARD          = 1
BMP085_HIGHRES           = 2
BMP085_ULTRAHIGHRES      = 3

# BMP085 Registers
BMP085_CAL_AC1           = 0xAA  # R   Calibration data (16 bits)
BMP085_CAL_AC2           = 0xAC  # R   Calibration data (16 bits)
BMP085_CAL_AC3           = 0xAE  # R   Calibration data (16 bits)
BMP085_CAL_AC4           = 0xB0  # R   Calibration data (16 bits)
BMP085_CAL_AC5           = 0xB2  # R   Calibration data (16 bits)
BMP085_CAL_AC6           = 0xB4  # R   Calibration data (16 bits)
BMP085_CAL_B1            = 0xB6  # R   Calibration data (16 bits)
BMP085_CAL_B2            = 0xB8  # R   Calibration data (16 bits)
BMP085_CAL_MB            = 0xBA  # R   Calibration data (16 bits)
BMP085_CAL_MC            = 0xBC  # R   Calibration data (16 bits)
BMP085_CAL_MD            = 0xBE  # R   Calibration data (16 bits)
BMP085_CONTROL           = 0xF4
BMP085_TEMPDATA          = 0xF6
BMP085_PRESSUREDATA      = 0xF6

# Commands
BMP085_READTEMPCMD       = 0x2E
BMP085_READPRESSURECMD   = 0x34


class BMP085(object):
	def __init__(self, mode=BMP085_STANDARD, address=BMP085_I2CADDR, i2c=None, **kwargs):
		self._logger = logging.getLogger('Adafruit_BMP.BMP085')
		# Check that mode is valid.
		if mode not in [BMP085_ULTRALOWPOWER, BMP085_STANDARD, BMP085_HIGHRES, BMP085_ULTRAHIGHRES]:
			raise ValueError('Unexpected mode value {0}.  Set mode to one of BMP085_ULTRALOWPOWER, BMP085_STANDARD, BMP085_HIGHRES, or BMP085_ULTRAHIGHRES'.format(mode))
		self._mode = mode
		# Create I2C device.
		if i2c is None:
			import Adafruit_GPIO.I2C as I2C
			i2c = I2C
		self._device = i2c.get_i2c_device(address, **kwargs)
		# Load calibration values.
		self._load_calibration()

	def _load_calibration(self):
		self.cal_AC1 = self._device.readS16BE(BMP085_CAL_AC1)   # INT16
		self.cal_AC2 = self._device.readS16BE(BMP085_CAL_AC2)   # INT16
		self.cal_AC3 = self._device.readS16BE(BMP085_CAL_AC3)   # INT16
		self.cal_AC4 = self._device.readU16BE(BMP085_CAL_AC4)   # UINT16
		self.cal_AC5 = self._device.readU16BE(BMP085_CAL_AC5)   # UINT16
		self.cal_AC6 = self._device.readU16BE(BMP085_CAL_AC6)   # UINT16
		self.cal_B1 = self._device.readS16BE(BMP085_CAL_B1)     # INT16
		self.cal_B2 = self._device.readS16BE(BMP085_CAL_B2)     # INT16
		self.cal_MB = self._device.readS16BE(BMP085_CAL_MB)     # INT16
		self.cal_MC = self._device.readS16BE(BMP085_CAL_MC)     # INT16
		self.cal_MD = self._device.readS16BE(BMP085_CAL_MD)     # INT16
		self._logger.debug('AC1 = {0:6d}'.format(self.cal_AC1))
		self._logger.debug('AC2 = {0:6d}'.format(self.cal_AC2))
		self._logger.debug('AC3 = {0:6d}'.format(self.cal_AC3))
		self._logger.debug('AC4 = {0:6d}'.format(self.cal_AC4))
		self._logger.debug('AC5 = {0:6d}'.format(self.cal_AC5))
		self._logger.debug('AC6 = {0:6d}'.format(self.cal_AC6))
		self._logger.debug('B1 = {0:6d}'.format(self.cal_B1))
		self._logger.debug('B2 = {0:6d}'.format(self.cal_B2))
		self._logger.debug('MB = {0:6d}'.format(self.cal_MB))
		self._logger.debug('MC = {0:6d}'.format(self.cal_MC))
		self._logger.debug('MD = {0:6d}'.format(self.cal_MD))

	def _load_datasheet_calibration(self):
		# Set calibration from values in the datasheet example.  Useful for debugging the
		# temp and pressure calculation accuracy.
		self.cal_AC1 = 408
		self.cal_AC2 = -72
		self.cal_AC3 = -14383
		self.cal_AC4 = 32741
		self.cal_AC5 = 32757
		self.cal_AC6 = 23153
		self.cal_B1 = 6190
		self.cal_B2 = 4
		self.cal_MB = -32767
		self.cal_MC = -8711
		self.cal_MD = 2868

	def read_raw_temp(self):
		"""Reads the raw (uncompensated) temperature from the sensor."""
		self._device.write8(BMP085_CONTROL, BMP085_READTEMPCMD)
		time.sleep(0.005)  # Wait 5ms
		raw = self._device.readU16BE(BMP085_TEMPDATA)
		self._logger.debug('Raw temp 0x{0:X} ({1})'.format(raw & 0xFFFF, raw))
		return raw

	def read_raw_pressure(self):
		"""Reads the raw (uncompensated) pressure level from the sensor."""
		self._device.write8(BMP085_CONTROL, BMP085_READPRESSURECMD + (self._mode << 6))
		if self._mode == BMP085_ULTRALOWPOWER:
			time.sleep(0.005)
		elif self._mode == BMP085_HIGHRES:
			time.sleep(0.014)
		elif self._mode == BMP085_ULTRAHIGHRES:
			time.sleep(0.026)
		else:
			time.sleep(0.008)
		msb = self._device.readU8(BMP085_PRESSUREDATA)
		lsb = self._device.readU8(BMP085_PRESSUREDATA+1)
		xlsb = self._device.readU8(BMP085_PRESSUREDATA+2)
		raw = ((msb << 16) + (lsb << 8) + xlsb) >> (8 - self._mode)
		self._logger.debug('Raw pressure 0x{0:04X} ({1})'.format(raw & 0xFFFF, raw))
		return raw

	def read_temperature(self):
		"""Gets the compensated temperature in degrees celsius."""
		UT = self.read_raw_temp()
		# Datasheet value for debugging:
		#UT = 27898
		# Calculations below are taken straight from section 3.5 of the datasheet.
		X1 = ((UT - self.cal_AC6) * self.cal_AC5) >> 15
		X2 = (self.cal_MC << 11) / (X1 + self.cal_MD)
		B5 = X1 + X2
		temp = ((B5 + 8) >> 4) / 10.0
		self._logger.debug('Calibrated temperature {0} C'.format(temp))
		return temp

	def read_pressure(self):
		"""Gets the compensated pressure in Pascals."""
		UT = self.read_raw_temp()
		UP = self.read_raw_pressure()
		# Datasheet values for debugging:
		#UT = 27898
		#UP = 23843
		# Calculations below are taken straight from section 3.5 of the datasheet.
		# Calculate true temperature coefficient B5.
		X1 = ((UT - self.cal_AC6) * self.cal_AC5) >> 15
		X2 = (self.cal_MC << 11) / (X1 + self.cal_MD)
		B5 = X1 + X2
		self._logger.debug('B5 = {0}'.format(B5))
		# Pressure Calculations
		B6 = B5 - 4000
		self._logger.debug('B6 = {0}'.format(B6))
		X1 = (self.cal_B2 * (B6 * B6) >> 12) >> 11
		X2 = (self.cal_AC2 * B6) >> 11
		X3 = X1 + X2
		B3 = (((self.cal_AC1 * 4 + X3) << self._mode) + 2) / 4
		self._logger.debug('B3 = {0}'.format(B3))
		X1 = (self.cal_AC3 * B6) >> 13
		X2 = (self.cal_B1 * ((B6 * B6) >> 12)) >> 16
		X3 = ((X1 + X2) + 2) >> 2
		B4 = (self.cal_AC4 * (X3 + 32768)) >> 15
		self._logger.debug('B4 = {0}'.format(B4))
		B7 = (UP - B3) * (50000 >> self._mode)
		self._logger.debug('B7 = {0}'.format(B7))
		if B7 < 0x80000000:
			p = (B7 * 2) / B4
		else:
			p = (B7 / B4) * 2
		X1 = (p >> 8) * (p >> 8)
		X1 = (X1 * 3038) >> 16
		X2 = (-7357 * p) >> 16
		p = p + ((X1 + X2 + 3791) >> 4)
		self._logger.debug('Pressure {0} Pa'.format(p))
		return p

	def read_altitude(self, sealevel_pa=101325.0):
		"""Calculates the altitude in meters."""
		# Calculation taken straight from section 3.6 of the datasheet.
		pressure = float(self.read_pressure())
		altitude = 44330.0 * (1.0 - pow(pressure / sealevel_pa, (1.0/5.255)))
		self._logger.debug('Altitude {0} m'.format(altitude))
		return altitude

	def read_sealevel_pressure(self, altitude_m=0.0):
		"""Calculates the pressure at sealevel when given a known altitude in
		meters. Returns a value in Pascals."""
		pressure = float(self.read_pressure())
		p0 = pressure / pow(1.0 - altitude_m/44330.0, 5.255)
		self._logger.debug('Sealevel pressure {0} Pa'.format(p0))
		return p0
