class Elem:

	def __str__():
		pass
		# return code html de l'element

	def add_content():
		pass
		# ajoute elem a la fin du contenu

class Text(str):

	def __init__(self, arg = ''):
		self.arg = arg.replace('\n','\n<br />\n')

	def __str__(self):
		return self.arg
