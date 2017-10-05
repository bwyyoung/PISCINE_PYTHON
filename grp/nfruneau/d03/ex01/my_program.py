#!/usr/local/bin/python3

from local_lib.path import path

libpath = "local_lib/"
dirname = "newdir"
filename = "newfile"

def func():
	tmp = path(libpath)
	if tmp.dirs(dirname) == []:
		newdir = tmp / dirname
		newdir.mkdir()
	else:
		newdir = path(libpath + dirname + "/")
	newfile = newdir / filename
	newfile.touch()
	newfile.write_text("HELLO I'M A TEXT IN A FILE INSIDE A DIR")
	print(newfile.text())


if __name__ == '__main__':
	func()
