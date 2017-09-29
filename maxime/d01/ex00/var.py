def my_var():
	var = [42, '42', 'quarante-deux', 42.0, True, [42], {42: 42}, (42,), set()]
	for v in var:
		print "%s est de type %s" % (v, type(v))
	return

my_var()