import sys, os
from settings import *

# def extract(file):
# 	settings = {}
# 	with open(file, 'r') as f:
# 		for l in f:
# 			splitted = l[:-1].split(' = ')
# 			splitted[0].replace("\"", "")
# 			if len(splitted) == 2:
# 				settings[splitted[0].replace('"', '')] = splitted[1].replace('"', '')
# 		return settings
# 	return -1

def check_read(file):
	if os.access(file, os.R_OK):
		return 1
	return -1


def check_extention(file, ext):
	f = file.split('.')
	if  f != -1:
		if len(f) == 2 and f[1] == ext:
			return(f[0] + '.html')
	return -1


def create_html(filename, file):
	try:
		html = open(filename, 'w')
		template = open(file, 'r')
		for line in template:
			html.write(line.format(**globals()))
		template.close()
		html.close()
	except:
		print('Incorrect settings')

if __name__ == '__main__':
	if len(sys.argv) == 2:
		try:
			filename = check_extention(sys.argv[1], 'template')
			assert filename != -1
			assert check_read(sys.argv[1]) == 1
			create_html(filename, sys.argv[1])
		except Exception as e:
			print(e)
	else:
		print('python3 render.py <file.template>')
