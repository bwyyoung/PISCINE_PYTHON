#!/usr/bin/python3


class Text(str):
	def __str__(self):
		data = super().__str__()
		data = data.replace('<', '&lt;')
		data = data.replace('>', '&gt;')
		data = data.replace('"', '&quot;')
		data = data.replace('\n', '\n<br />\n')
		return data


class Elem:
	class ValidationError(Exception):
		def __init__(self):
			self.message = "This content is not a Text or an Elem."

		def __str__(self):
			return self.message

	def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
		self.tag = tag
		self.attr = attr
		self.content = []

		if content:
			self.add_content(content)
		elif content != None:
			if not isinstance(content, Text):
				raise Elem.ValidationError
		self.tag_type = tag_type

	def __str__(self):
		attr = self.__make_attr()
		if self.tag_type == 'double':
			result = "<" + self.tag + attr + ">"
			result += self.__make_content()
			result += "</" + self.tag + ">"
		elif self.tag_type == 'simple':
			result = "<" + self.tag + attr + ">"
		return result

	def __make_attr(self):
		result = ''
		for pair in sorted(self.attr.items()):
			result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
		return result

	def __make_content(self):
		if len(self.content) == 0:
			return ''
		result = '\n'
		for elem in self.content:
			result += "  " + str(elem).replace('\n', '\n  ') + "\n"
		return result

	def add_content(self, content):
		if not Elem.check_type(content):
			raise Elem.ValidationError
		if type(content) == list:
			self.content += [elem for elem in content if elem != Text('')]
		elif content != Text(''):
			self.content.append(content)

	@staticmethod
	def check_type(content):
		return (isinstance(content, Elem) or type(content) == Text or
				(type(content) == list and all([type(elem) == Text or
												isinstance(elem, Elem)
												for elem in content])))

if __name__ == '__main__':
	e = Elem(tag='html',
				content=[Elem(tag='head', content=Elem(tag='title',
				content=Text('"Hello Ground!"'))),Elem(tag='body',
				content=[Elem(tag='h1', content=Text('"Oh no, not again!"')),
				Elem(tag='img', tag_type='simple', attr={'src': 'http://i.imgur.com/pfp3T.jpg'})])])
	print(e)
