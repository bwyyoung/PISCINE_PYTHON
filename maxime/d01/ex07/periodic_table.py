import sys

def opener(file):
	try:
		with open(file, 'r') as f:
			for line in f:
				reader(line)
	except:
		print('Error: bad file')


if __name__ == '__main__' :
	if len(sys.argv) == 2
		opener(sys.argv[1])