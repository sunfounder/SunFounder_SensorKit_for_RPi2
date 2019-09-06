from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(name 				= 'Adafruit_BMP',
	  version 			= '1.5.0',
	  author			= 'Tony DiCola',
	  author_email		= 'tdicola@adafruit.com',
	  description		= 'Library for accessing the BMP series pressure and temperature sensors like the BMP085/BMP180 on a Raspberry Pi or Beaglebone Black.',
	  license			= 'MIT',
	  url				= 'https://github.com/adafruit/Adafruit_Python_BMP/',
	  dependency_links	= ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.6.5'],
	  install_requires	= ['Adafruit-GPIO>=0.6.5'],
	  packages 			= find_packages())
