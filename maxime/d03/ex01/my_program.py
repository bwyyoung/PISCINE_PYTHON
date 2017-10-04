from local_lib.path import Path

def discover_path():
	try:
		d = Path('./folder')
		d.mkdir_p()
		f = Path('folder/file')
		f.touch()
		f.open()
		f.write_text("WOLOLO\n")
		print(f.text())
	except e:
		print(e)

if __name__ == '__main__' :
	discover_path()
