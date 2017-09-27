# objects:

# class Myclass:
#	counter = 0
#	def __init__(self, name='toto'):
#		self.name = name
#		self.increment_counter()
#	def __del__(self):
#		print("%s just died" % self.name)
#
#	class Test:
#		s = "test"
#		def method(self):
#			print("lolo")
#
#	@classmethod
#	def increment_counter(clss)
#		clss.counter += 1
#
#	if __name__ == '__main__':
#		print(Myclass.Test.s)
#		ins = Myclass.Test()
#		ins.method()


# decorators:

# take a function in parameter and complete it:
# def decorator(f):
# 	def func(s)
# 		return ("blabla" + f(s))
# 	return func

# Two different way to assign a decorator:

# def dec_func_assign(s)
# 	return s
#
# def dec_func_assign(s) = decorator(dec_func_assign)

# @decorator
# def dec_function_def(s)
# 	return s


# inheritence:

# class Daddy:
#	des = "the dad"
#
#	def __init__(self):
#		print("I'm a human")
#
# class Kiddo(Daddy):
#	des = "the kid"
#
#	def __init__(self): (facultative, just to show that you can call parents method with super())
#		super().__init__()
#		print("I'm a human too")

# exceptions:

# throw exception but show error on stdout if not catched:
# def func():
#	if ...
#		raise Exception("toto")

# to catch it use:
# try:
#	func()
# except Exception as e:
# 	print(e)

# * fct isinstance(var, Instance) <- to check if var match Class type
