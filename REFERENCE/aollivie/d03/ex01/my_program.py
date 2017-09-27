from local_lib.path import Path

if __name__ == '__main__':
	tmp = Path('.')
	new = tmp / 'test'
	if not new.isdir():
		new.mkdir()
	new = new / 'test.txt'
	if not new.isfile():
		new.touch()
	fd = new.open('w')
	if fd:
		fd.write('hello')
		fd.close()
	if fd:
		fd = new.open('r')
		print(fd.read())
