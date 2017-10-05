if __name__ == '__main__':
	filename = 'numbers.txt'
	with open(filename, 'r') as file:
		for line in file :
			new = line.replace('\n', '')
			print(new.replace(',', '\n'))
