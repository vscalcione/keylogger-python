from pynput import keyboard
import sys
from datetime import datetime

class Time(object):
	def Years(self):
		self.now = datetime.now()
		self.years = ' ' + str(self.now.day) + '/' + str(self.now.month) + '/' + str(self.now.year)
		return self.years

	def Hours(self):
		self.now = datetime.now()
		self.hour = ' ' + str(self.now.hour) + ':' + str(self.now.minute) + ':' + str(self.now.second)
		return self.hour


def on_press(key):
	if str(key) == 'Key.esc':
		sys.exit()
	else:
		print(Time().Years() + '|' + Time().Hours() + f': {key}')
if __name__ == "__main__":
	with keyboard.Listener(on_press = on_press) as listener:
		listener.join()
