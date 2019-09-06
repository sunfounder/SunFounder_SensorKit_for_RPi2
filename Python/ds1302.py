# RTC_DS1302 - Python Hardware Programming Education Project For Raspberry Pi
# Copyright (C) 2015 Jason Birch
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

'''
RTC_DS1302                                                              
'''
'''
------------------------------------------------------------------------
'''
'''
V1.00 - 2015-08-26 - Jason Birch                                        
'''
'''
------------------------------------------------------------------------
'''
'''
Class to handle controlling a Real Time Clock IC DS1302.                
'''

import time
import RPi.GPIO
from datetime import datetime


class DS1302:

    CLK_PERIOD = 0.00001

    DOW = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" ]


    def __init__(self, scl=23, rst=25, io=24):
        self.scl = scl
        self.rst = rst
        self.io = io
        # Turn off GPIO warnings.
        RPi.GPIO.setwarnings(False)
        # Configure Raspberry Pi GPIO interfaces.
        RPi.GPIO.setmode(RPi.GPIO.BCM)
        # Initiate DS1302 communication.
        self.init_ds1302()
        # Make sure write protect is turned off.
        self.write_byte(int("10001110", 2))
        self.write_byte(int("00000000", 2))
        # Make sure trickle charge mode is turned off.
        self.write_byte(int("10010000", 2))
        self.write_byte(int("00000000", 2))
        # End DS1302 communication.
        self.end_ds1302()
        self.datetime = {}

    def CloseGPIO(self):
        '''
        Close Raspberry Pi GPIO use before finishing.
        '''
        RPi.GPIO.cleanup()


    def init_ds1302(self):
        '''
        Start a transaction with the DS1302 RTC.
        '''
        RPi.GPIO.setup(self.scl, RPi.GPIO.OUT, initial=0)
        RPi.GPIO.setup(self.rst, RPi.GPIO.OUT, initial=0)
        RPi.GPIO.setup(self.io, RPi.GPIO.OUT, initial=0)
        RPi.GPIO.output(self.scl, 0)
        RPi.GPIO.output(self.io, 0)
        time.sleep(self.CLK_PERIOD)
        RPi.GPIO.output(self.rst, 1)


    def end_ds1302(self):
        '''
        Complete a transaction with the DS1302 RTC.
        '''
        RPi.GPIO.setup(self.scl, RPi.GPIO.OUT, initial=0)
        RPi.GPIO.setup(self.rst, RPi.GPIO.OUT, initial=0)
        RPi.GPIO.setup(self.io, RPi.GPIO.OUT, initial=0)
        RPi.GPIO.output(self.scl, 0)
        RPi.GPIO.output(self.io, 0)
        time.sleep(self.CLK_PERIOD)
        RPi.GPIO.output(self.rst, 0)


    def write_byte(self, Byte):
        '''
        Write a byte of data to the DS1302 RTC.
        '''
        for Count in range(8):
            time.sleep(self.CLK_PERIOD)
            RPi.GPIO.output(self.scl, 0)

            Bit = Byte % 2
            Byte = int(Byte / 2)
            time.sleep(self.CLK_PERIOD)
            RPi.GPIO.output(self.io, Bit)

            time.sleep(self.CLK_PERIOD)
            RPi.GPIO.output(self.scl, 1)
        
    def read_byte(self):
        '''
        Read a byte of data to the DS1302 RTC.
        '''
        RPi.GPIO.setup(self.io, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_DOWN)

        Byte = 0
        for Count in range(8):
            time.sleep(self.CLK_PERIOD)
            RPi.GPIO.output(self.scl, 1)

            time.sleep(self.CLK_PERIOD)
            RPi.GPIO.output(self.scl, 0)
            
            time.sleep(self.CLK_PERIOD)
            Bit = RPi.GPIO.input(self.io)
            Byte |= ((2 ** Count) * Bit)

        return Byte


    def write_ram(self, Data):
        '''
        Write a message to the RTC RAM.
        '''
        # Initiate DS1302 communication.
        self.init_ds1302()
        # Write address byte.
        self.write_byte(int("11111110", 2))
        # Write data bytes.
        for Count in range(len(Data)):
            self.write_byte(ord(Data[Count:Count + 1]))
        for Count in range(31 - len(Data)):
            self.write_byte(ord(" "))
        # End DS1302 communication.
        self.end_ds1302()

    def read_ram(self):
        '''
        Read message from the RTC RAM.
        '''
        # Initiate DS1302 communication.
        self.init_ds1302()
        # Write address byte.
        self.write_byte(int("11111111", 2))
        # Read data bytes.
        Data = ""
        for Count in range(31):
            Byte = self.read_byte()
            Data += chr(Byte)
        # End DS1302 communication.
        self.end_ds1302()
        return Data


    def set_datetime(self, dt):
        '''
        Write date and time to the RTC.
        '''
        if not self.check_sanity():
            return False
        # Initiate DS1302 communication.
        self.init_ds1302()
        # Write address byte.
        self.write_byte(int("10111110", 2))
        # Write seconds data.
        self.write_byte((dt.second % 10) | int(dt.second / 10) * 16)
        # Write minute data.
        self.write_byte((dt.minute % 10) | int(dt.minute / 10) * 16)
        # Write hour data.
        self.write_byte((dt.hour % 10) | int(dt.hour / 10) * 16)
        # Write day data.
        self.write_byte((dt.day % 10) | int(dt.day / 10) * 16)
        # Write month data.
        self.write_byte((dt.month % 10) | int(dt.month / 10) * 16)
        # Write day of week data.
        self.write_byte((dt.isoweekday() % 10) | int(dt.isoweekday() / 10) * 16)
        # Write year data.
        self.write_byte((dt.year % 100 % 10) | int(dt.year % 100 / 10) * 16)
        # Make sure write protect is turned off.
        self.write_byte(int("00000000", 2))
        # Make sure trickle charge mode is turned off.
        self.write_byte(int("00000000", 2))
        # End DS1302 communication.
        self.end_ds1302()


    def get_datetime(self):
        '''
        Read date and time from the RTC.
        '''
        # Initiate DS1302 communication.
        self.init_ds1302()
        # Write address byte.
        self.write_byte(int("10111111", 2))
        # Read date and time data.
        Data = ""

        Byte = self.read_byte()
        second = (Byte % 16) + int(Byte / 16) * 10
        Byte = self.read_byte()
        minute = (Byte % 16) + int(Byte / 16) * 10
        Byte = self.read_byte()
        hour = (Byte % 16) + int(Byte / 16) * 10
        Byte = self.read_byte()
        day = (Byte % 16) + int(Byte / 16) * 10
        Byte = self.read_byte()
        month = (Byte % 16) + int(Byte / 16) * 10
        Byte = self.read_byte()
        day_of_week = ((Byte % 16) + int(Byte / 16) * 10) - 1
        Byte = self.read_byte()
        year = (Byte % 16) + int(Byte / 16) * 10 + 2000

        # End DS1302 communication.
        self.end_ds1302()
        return datetime(year, month, day, hour, minute, second)

    def check_sanity(self):
        "check sanity of a clock. returns True if clock is sane and False otherwise"
        dt = self.get_datetime()
        if dt.year == 2000 or dt.month == 0 or dt.day == 0:
            return False
        if dt.second == 80:
            return False
        return True

def format_time(dt):
    if dt is None:
        return ""
    fmt = "%m/%d/%Y %H:%M"
    return dt.strftime(fmt)
    
def parse_time(s):
    fmt = "%m/%d/%Y %H:%M"
    return datetime.strptime(s, fmt)

