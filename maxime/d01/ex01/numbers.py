def splitter(line):
	l = line.split(',')
	for c in l:
		print(c.strip('\n'))

def opener():
	try:
		with open('numbers.txt', 'r') as f:
			for line in f:
				splitter(line)
	except:
		print('Error: check numbers.txt file')

if __name__ == '__main__' :
	opener()
