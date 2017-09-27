import sys

def start_html():
	s = '<!doctype html>\n<html>\n\t<head>\n\t\t<meta charset="utf-8" />\n'
	s += '\t\t<title>Tableau periodique des elements</title>\n'
	s += '\t\t<style>\n'
	s += '\t\t\ttable {\n'
	s += '\t\t\t\t\tborder-collapse: collapse;\n\t\t\t}\n'
	s += '\t\t\ttd {\n\t\t\t\tborder: solid;\n\t\t\t}\n'
	s += '\t\t\th4, li {\n\t\t\t\tfont-size:10px;\n\t\t\t}\n'
	s += '\t\t\t.no-elem {\n\t\t\t\tborder: 0px;\n\t\t\t}\n'
	s += '\t\t</style>\n\t</head>\n\t<body>\n'
	s += '\t\t<table>\n'
	return (s)

def s_tr_s():
	return('\t\t\t<tr>\n')
def s_tr_e():
	return('\t\t\t</tr>\n')

def s_td_s():
	return('\t\t\t\t<td>\n')

def s_td_e():
	return('\t\t\t\t</td>\n')

def s_td_no():
	return('\t\t\t\t<td class="no-elem"></td>\n')

def s_h_s():
	return ('\t\t\t\t\t<h4>')

def s_h_e():
	return ('</h4>\n')

def s_ul_s():
	return ('\t\t\t\t\t<ul>\n')

def s_ul_e():
	return ('\t\t\t\t\t</ul>\n')
def s_li_s():
	return ('\t\t\t\t\t<li>')

def s_li_e():
	return ('</li>\n')

def s_table_end():
	return ('\t\t</table>\n')

def s_body_end():
	return ('\t</body>\n')

def s_html_end():
	return ('</html>')

def to_dict(str):
	new = {}
	s = str.split(',')
	name_postion = s[0].split('=')
	new['name'] = name_postion[0]
	position = name_postion[1].split(':')
	new['position'] = int(position[1])
	number = s[1].split(':')
	new['number'] = number[1]
	small = s[2].split(':')
	new['small'] = small[1]
	molar = s[3].split(':')
	new['molar'] = molar[1]
	return (new)

def extract():
	list = []
	filename = 'periodic_table.txt'
	with open(filename, 'r') as file:
		for line in file :
			list.append(to_dict(line))
	return(list)


def write(s, l, last_pos):
	i = l['position']

	if i == 0:
		s += s_tr_s()

	while last_pos < i - 1:
		s += s_td_no()
		last_pos += 1

	s += s_td_s()

	s += s_h_s()

	s += l['name']

	s += s_h_e()

	s += s_ul_s()
	s += s_li_s()
	s += l['number']
	s += s_li_e()
	s += s_li_s()
	s += l['small']
	s += s_li_e()
	s += s_li_s()
	s += l['molar']
	s += s_li_e()
	s += s_ul_e()
	s += s_td_e()

	if i == 17:
		s += s_tr_e()
	return (s)

def process(list, s):
	last_pos = 0
	for l in list:
		s = write(s, l, last_pos)
		last_pos = l['position']
	return (s)


if __name__ == '__main__':
	save_stdout = sys.stdout
	fh = open('periodic_table.html', 'w')
	sys.stdout = fh

	list = extract()

	s = start_html()

	s = process(list, s)
	s += s_table_end()
	s += s_body_end()
	s += s_html_end()
	print(s)

	sys.stdout = save_stdout
