import sys

if __name__ == '__main__':
	if len(sys.argv) != 5:
		print('Inavlid number arguments')
		quit()
	import antigravity

	inStr = sys.argv[3] + '-' + sys.argv[4]
	antigravity.geohash(float(sys.argv[1]),float(sys.argv[2]),inStr.encode())
