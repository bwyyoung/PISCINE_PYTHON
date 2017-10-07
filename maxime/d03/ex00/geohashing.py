# https://stackoverflow.com/questions/7585307/typeerror-unicode-objects-must-be-encoded-before-hashing
import sys
import antigravity

def hashgeo(lat, lon, date):
	try:
		antigravity.geohash(lat, lon, date)
	except e:
		print('usage: py geohashing.py 37.421542 -122.085589 2005-05-26-10458.68')

if __name__ == '__main__':
	if len(sys.argv) == 4:
		lat = float(sys.argv[1])
		lon = float(sys.argv[2])
		date = sys.argv[3].encode('utf-8')
		hashgeo(lat, lon, date)
	else:
		print('usage: py geohashing.py 37.421542 -122.085589 2005-05-26-10458.68')
