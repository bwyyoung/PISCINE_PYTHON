#!/usr/local/bin/python3

import sys
import settings

def istemplate(file):
	if file.endswith(".template") == False:
		raise Exception("Wrong file format: Usage: python3 render.py <file.template>")

def func(s):
	with open("file.html", 'w') as f:
		f.write("")
	with open("file.html", 'a') as f:
		with open(s, 'r') as f2:
			for line in f2:
				f.write(line.format(title = settings.title, firstname = settings.firstname, lastname = settings.lastname, age = settings.age, job = settings.job))

if __name__ == '__main__':
	try:
		if len(sys.argv) != 2:
			raise Exception("Usage: python3 render.py <file.template>")
		istemplate(sys.argv[1])
		func(sys.argv[1])
	except Exception as e:
		print (e)
