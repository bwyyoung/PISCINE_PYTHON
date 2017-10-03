import sys, os

def check_read(file):
	if os.access(file, os.R_OK):
		return 1
	return -1


def check_extenstion(file, ext):
	f = file.split('.')
	if  f != -1:
		if len(f) == 2 and f[1] == ext:
			return 1
	return -1


def extract(file):
	settings = {}
	with open(file, 'r') as f:
		for l in f:
			splitted = l[:-1].split(' = ')
			splitted[0].replace("\"", "")
			if len(splitted) == 2:
				settings[splitted[0].replace('"', '')] = splitted[1].replace('"', '')
		return settings
	return -1

def create_html(settings, file):
	html = open('myCV.html', 'w')
	with open(file, 'r') as template:
		for line in template :
			line = line.replace("{lastname}", settings['lastname'])
			line = line.replace("{firstname}", settings['firstname'])
			line = line.replace("{age}", settings['age'])
			line = line.replace("{work}", settings['work'])
			line = line.replace('\n', '')
			html.write(line + '\n');
	html.close()

if __name__ == '__main__':
	if len(sys.argv) == 2:
		try:
			assert check_extenstion(sys.argv[1], 'template') == 1
			assert check_read('settings.py') == 1
			settings = extract('settings.py')
			create_html(settings, sys.argv[1])
		except Exception as e:
			print(e)
	else:
		print('python3 render.py <file.template>')
