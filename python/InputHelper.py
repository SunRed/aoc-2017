import os, sys

class InputHelper:
	def __init__(self, dayNr):
		self.dayNr = dayNr

	def readlines(self):
		lines = []

		if not sys.stdin.isatty:
			lines = sys.stdin.readlines()
		else:
			os.chdir('..')
			f = open('day' + str(self.dayNr) + '.input', 'r')
			lines = f.readlines()
			f.close()

		return lines

	def read(self):
		lines = ""

		if not sys.stdin.isatty:
			lines = sys.stdin.read()
		else:
			os.chdir('..')
			f = open('day' + str(self.dayNr) + '.input', 'r')
			lines = f.read()
			f.close()

		return lines
