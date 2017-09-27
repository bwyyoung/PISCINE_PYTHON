
def my_var():
	number = int(42)
	str = '42'
	str_long = 'quarante-deux'
	float = 42.0
	bool = True
	list = [42]
	dict = {42: 42}
	tuple = (42,)
	set_s = set()
	print(number, 'est de type', type(number))
	print(str, 'est de type', type(str))
	print(str_long, 'est de type', type(str_long))
	print(float, 'est de type', type(float))
	print(bool, 'est de type', type(bool))
	print(list, 'est de type', type(list))
	print(dict, 'est de type', type(dict))
	print(tuple, 'est de type', type(tuple))
	print(set_s, 'est de type', type(set_s))

if __name__ == '__main__':
	my_var()
