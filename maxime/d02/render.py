import sys, os, re

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
			if len(splitted) == 2:
				settings[splitted[0]] = splitted[1]
			print(settings)


if __name__ == '__main__':
	if len(sys.argv) == 2:
		try:
			assert check_extenstion(sys.argv[1], 'template') == 1
			assert check_read('settings.py') == 1
			settings = extract('settings.py')
		except:
			print('Invalid input files')
	else:
		print('python3 render.py <file.template>')


import sys, os, re


def check_nb_argv():
	if len(sys.argv) != 2:
		raise Exception("Invalide number argument")
	return

def check_ext(file):
	find = re.search(".template$", file)
	if find is None:
		raise Exception('Bad extension file in argument')

def check_is_file(file):
	if os.access(file, os.R_OK):
		return
	raise Exception('No access to: ' + file)

def set_dict(dict, key, line):
	value = re.search(r'(?<=")(.*)(")', line)
	if value:
		dict[key] = value.group(0).replace('"', '')
	else:
		raise Exception(key + ' is require')

def extract_setting(file):
	setting = {}
	with open(file, 'r') as file:
		for line in file :
			find = re.match("^name", line)
			if find:
				set_dict(setting, 'name', line)
				continue
			find = re.match("^firstname", line)
			if find:
				set_dict(setting, 'firstname', line)
				continue
			find = re.match("^age", line)
			if find:
				set_dict(setting, 'age', line)
				continue
			find = re.match("^profession", line)
			if find:
				set_dict(setting, 'profession', line)
	if 'name' not in setting:
		raise Exception('name' + ' is require')
	if 'firstname' not in setting:
		raise Exception('firstname' + ' is require')
	if 'age' not in setting:
		raise Exception('age' + ' is require')
	if 'profession' not in setting:
		raise Exception('profession' + ' is require')
	return(setting)

def process(setting, file):
	save_stdout = sys.stdout
	fh = open('myCV.html', 'w')
	sys.stdout = fh
	with open(file, 'r') as file:
		for line in file :
			line = line.replace("{name}", setting['name'])
			line = line.replace("{firstname}", setting['firstname'])
			line = line.replace("{age}", setting['age'])
			line = line.replace("{profession}", setting['profession'])
			line = line.replace('\n', '')
			print(line)
	sys.stdout = save_stdout

if __name__ == '__main__':
	try:
		check_nb_argv()
		check_ext(sys.argv[1])
		check_is_file(sys.argv[1])
		check_is_file('settings.py')
		setting = extract_setting('settings.py')
		process(setting, sys.argv[1])
	except Exception as e:
		print(e)
