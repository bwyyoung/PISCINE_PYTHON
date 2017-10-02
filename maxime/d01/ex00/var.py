def my_var():
	var = [42, '42', 'quarante-deux', 42.0, True, [42], {42: 42}, (42,), set()]
	for v in var:
		print("{0} est de type {1}".format(v, type(v)))
	return

if __name__ == '__main__':
	my_var()
