def header():
	print('<!DOCTYPE html>')
	print('<html>')
	print('<head>')
	print('<meta charset="utf-8" />')
	print('<title>Tableau periodique</title>')
	print('</head>')
	print('<body>')
	print('<table>')


def debuggline(element):
	for key, value in element:
		print(value)

def extract(line):
	d = {}
	tmp = line.split(" = ")
	d['name'] = tmp[0].strip(" ")
	tmp2 = tmp[1].split(",")
	for data in tmp2:
		tmp3 = data.split(":")
		d[tmp3[0]] = tmp3[1]
	return d

def opener(file):
	tmp = {}
	d = {}
	try:
		with open(file, 'r') as f:
			for line in f:
				tmp = extract(line[:-1])
				d[tmp['number']] = tmp
		print(d)
	except:
		print('Error: bad file')


if __name__ == '__main__' :
	opener('periodic_table.txt')
