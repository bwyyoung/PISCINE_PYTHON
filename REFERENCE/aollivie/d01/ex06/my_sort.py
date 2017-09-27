def get_dict():
	d = {
		'Hendrix' : '1942',
		'Allman' : '1946',
		'King' : '1925',
		'Clapton' : '1945',
		'Johnson' : '1911',
		'Berry' : '1926',
		'Vaughan' : '1954',
		'Cooder' : '1947',
		'Page' : '1944',
		'Richards' : '1943',
		'Hammett' : '1962',
		'Cobain' : '1967',
		'Garcia' : '1942',
		'Beck' : '1944',
		'Santana' : '1947',
		'Ramone' : '1948',
		'White' : '1975',
		'Frusciante': '1970',
		'Thompson' : '1949',
		'Burton' : '1939',
	}
	return (d)

def reverse_dict(dict):
	new = {}
	for key, value in dict.items():
		if value not in new:
			new[value] = key
		else:
			new[value] += ' ' + key
	return (new)

def index_to_append(list, target):
	index = 0
	for i, v in enumerate(list):
		index = i
		if target < v[0]:
			return (index)
	return (index)

def dick_to_list(dict):
	list = []
	for key, value in dict.items():
		index = index_to_append(list, key)
		list.insert(index, [key, value])
	return list

def print_list(list):
	for value in list:
		new_value = value[1].split(' ')
		new_value.sort()
		for v in new_value:
			print(v)
	return

if __name__ == '__main__':
	dict = get_dict()
	new_dict = reverse_dict(dict)
	list = dick_to_list(new_dict)
	print_list(list)
