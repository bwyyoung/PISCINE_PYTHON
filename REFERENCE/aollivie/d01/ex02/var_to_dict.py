def get_list():
	d = [
		('Hendrix' , '1942'),
		('Allman' , '1946'),
		('King' , '1925'),
		('Clapton' , '1945'),
		('Johnson' , '1911'),
		('Berry' , '1926'),
		('Vaughan' , '1954'),
		('Cooder' , '1947'),
		('Page' , '1944'),
		('Richards' , '1943'),
		('Hammett' , '1962'),
		('Cobain' , '1967'),
		('Garcia' , '1942'),
		('Beck' , '1944'),
		('Santana' , '1947'),
		('Ramone' , '1948'),
		('White' , '1975'),
		('Frusciante', '1970'),
		('Thompson' , '1949'),
		('Burton' , '1939')
	]
	return (d)

def do_dict_from_list(list):
	new_dict = {}
	for indice, value in enumerate(list):
		if value[1] in new_dict:
			new_dict[value[1]].append(value[0])
		else:
			new_dict[value[1]] = []
			new_dict[value[1]].append(value[0])
	return new_dict

def format_print_list(arg):
	new = ''
	for v in arg:
		new += ' ' + v
	return (new)

def print_dict(dict):
	for key, value in dict.items():
		str_value = format_print_list(value)
		print(key, ':', str_value)

if __name__ == '__main__':
	list = get_list()
	dict = do_dict_from_list(list)
	print_dict(dict)
