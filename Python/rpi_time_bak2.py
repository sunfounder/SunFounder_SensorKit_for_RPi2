#!/usr/bin/python3
from datetime import datetime
import ds1302


class DS1302:
	def __init__(self, rangechecks=True):
		self.rangechecks = rangechecks
		ds1302.init_clock()

	def get_datetime(self):
		if not self.check_sanity():
			# if clock are insane: try to reset it
			self.reset_clock()
			# if clock are still insane: return None
			if not self.check_sanity():
				return None
		year, month, date = ds1302.get_date()
		hour, minute, second = ds1302.get_time()
		'''
		if self.rangechecks:
			if year < 2000 or year > 3000:
				ds1302.set_date(2000, month, date)
				return self.get_datetime()
			if month not in range(1, 13):
				ds1302.set_date(year, 1, date)
				return self.get_datetime()
			if date not in range(1, 32):
				ds1302.set_date(year, month, 1)
				return self.get_datetime()
			if hour not in range(0, 24):
				ds1302.set_time(0, minute, second)
				return self.get_datetime()
			if minute not in range(0, 60):
				ds1302.set_time(hour, 0, second)
				return self.get_datetime()
			if second not in range(0, 60):
				ds1302.set_time(hour, minute, 0)
				return self.get_datetime()
		'''
		return datetime(year, month, date,
						hour, minute, second)


	def set_datetime(self, dt):
		if not self.check_sanity():
			# if clock are insane: try to reset it
			self.reset_clock()
			# if clock are still insane: return False
			if not self.check_sanity():
				return False
		ds1302.set_date(dt.year, dt.month, dt.day)
		ds1302.set_time(dt.hour, dt.minute, dt.second)
		return True

	def check_sanity(self):
		"check sanity of a clock. returns True if clock is sane and False otherwise"
		year, month, date = ds1302.get_date()
		hours, mins, secs = ds1302.get_time()
		if year == 2000 or month == 0 or date == 0:
			return False
		if secs == 80:
			return False
		return True

	def reset_clock(self):
		ds1302.reset_clock()

def format_time(dt):
	if dt is None:
		return ""
	fmt = "%m/%d/%Y %H:%M"
	return dt.strftime(fmt)
	
def parse_time(s):
	fmt = "%m/%d/%Y %H:%M"
	return datetime.strptime(s, fmt)






