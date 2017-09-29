#!/usr/bin/python3
# coding : utf8

from local_lib.path import Path

if __name__ == '__main__':
	d = Path('/tmp/pathfinder')
	d.mkdir_p()
	f = Path('/tmp/pathfinder/test.txt')
	f.touch()
	f.open()
	f.write_text("Path Successfully Installed\n", append=True)
	print(f.text())
