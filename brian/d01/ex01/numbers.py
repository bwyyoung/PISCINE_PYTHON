def read_file(file):
	try:
		with open(file) as f:
			for line in f:
				words = line.split(",")
				for w in words:
					print(w.strip('\n'))
	except FileNotFoundError as e:
		print("File {0} not found".format(e.filename))
		exit(1)

if __name__ == '__main__' :
	read_file("numbers.txt")
