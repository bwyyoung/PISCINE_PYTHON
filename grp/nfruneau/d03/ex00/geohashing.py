#!/usr/local/bin/python3

import sys
import antigravity

def func(argv):
	try:
		if len(argv) != 5:
			raise Exception ("Usage: ./geohashing.py <lat> <long> <AAAA-MM-DD> <dow>")
		seq = (argv[3], argv[4])
		s = "-".join(seq)
		antigravity.geohash(float(argv[1]), float(argv[2]), bytes(s, 'utf-8'))
	except Exception as e:
		print(e)


if __name__ == '__main__':
	func(sys.argv)
