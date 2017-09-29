def read_file(file):
	with open(file) as f:
		for line in f:
			words = line.split(",")
			for w in words:
				print(w.strip('\n'))

if __name__ == '__main__' :
	read_file("numbers.txt")
