
def show_type(val):
	print("{0} est de type {1}".format(val, type(val)))

def my_var():
	show_type(42)
	show_type("42")
	show_type("quarante-deux")
	show_type(42.0)
	show_type([42])
	show_type({42 :42})
	show_type((42,))
	show_type(set())
	
if __name__ == '__main__' :
    my_var()
