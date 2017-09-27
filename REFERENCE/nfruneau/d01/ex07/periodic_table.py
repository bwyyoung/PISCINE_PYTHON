#!/usr/local/bin/python3

def func(count, line, f):
	name = line.split('=')
	tab = name[1].split(',')
	dic = dict()
	for item in range(len(tab)):
		obj = tab[item].split(':')
		dic[obj[0].strip()] = obj[1].strip("\n ")
	if count + 1 < int(dic['position']):
		for var in range(int(dic['position']) - count - 1):
			f.write("""
				<td></td>""")
	f.write("""
				<td style="border: 1px solid black; padding:10px">
					<h4>"""+name[0]+"""</h4>
					<ul>
						<li>No """+dic['number']+"""</li>
						<li>"""+dic['small']+"""</li>
						<li>"""+dic['molar']+"""</li>
						<li>"""+dic['electron']+""" electron</li>
					</ul>
				</td>""")
	if int(dic['position']) > 16 and int(dic['number']) < 118:
		f.write("""
			</tr>
			<tr>""")
	return int(dic['position'])

if __name__ == '__main__':
	count = 0
	with open("periodic_table.html", 'w') as fd:
		fd.write("")
	with open("periodic_table.html", 'a') as fd1:
		fd1.write("""<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Periodic table</title>
		<style type="text/css">
		table {
			border-collapse: collapse;
		}
		ul {
			list-style: none;
		}
		</style>
	</head>
	<body>
		<table>
			<tr>""")
		with open("periodic_table.txt", 'r') as fd2:
			for line in fd2:
				count = func(count, line, fd1)
		fd1.write("""
			</tr>
		</table>
	</body>
</html>
""")
