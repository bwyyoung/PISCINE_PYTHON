from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, Ul,Ol, Li, H1, H2, P, Div, Span, Hr, Br
from elem import Text


class Page:
	def __init__(self, elem):
		self.i =0
		self.elem = elem
		self.valid_elem = [Html, Head, Body, Title, Meta, Img, Table, Th,
		Tr, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text]
		self.__valid_instance_body_div__ = [H1, H2, Div, Table, Ul, Ol, Span, Text]

	def __str__(self):
		s = ''
		if isinstance(self.elem, Html):
			s = '<!DOCTYPE html>\n'
		return s + str(self.elem)

	def __v_instance__(self, node, instance):
		return isinstance(node, instance)

	def __v_html__(self, node):
		if len(node.content) != 2:
			return False
		if not isinstance(node.content[0], Head):
			return False
		if not isinstance(node.content[1], Body):
			return False
		return True

	def __v_head__(self, node):
		if len(node.content) != 1:
			return False
		return isinstance(node.content[0], Title)

	def __v_body_div__(self, node):
		if len(node.content) == 0:
			return True
		check = True
		for elem in node.content:
			if check == False:
				return False
			for instance in self.__valid_instance_body_div__:
				if self.__v_instance__(elem, instance):
					check = True
					break;
				check = False
		return check


	def __v_Tr__(self, node):
		if len(node.content) < 1:
			return False
		if isinstance(node.content[0], Th):
			for elem in node.content:
				if not isinstance(elem, Th):
					return False
			return True
		if isinstance(node.content[0], Td):
			for elem in node.content:
				if not isinstance(elem, Td):
					return False
			return True
		return False

	def __v_table__(self, node):
		if len(node.content) == 0:
			return True
		for elem in node.content:
			if not isinstance(elem, Tr):
				return False
		return True

	def __v_p__(self, node):
		if len(node.content) == 0:
			return True
		for elem in node.content:
			if not isinstance(elem, Text):
				return False
		return True

	def __v_span__(self, node):
		if len(node.content) == 0:
			return True
		for elem in node.content:
			if not isinstance(elem, Text):
				if not isinstance(elem, P):
					return False
		return True

	def __v_node_with_text(self, node):
		if len(node.content) == 0:
			return True
		if len(node.content) > 1:
			return False
		return isinstance(node.content[0], Text)


	def __v_list__(self, node):
		if len(node.content) < 1:
			return False
		for elem in node.content:
			if not isinstance(elem, Li):
				return False
		return True


	def __v_node__(self, node):
		for instance in self.valid_elem:
			if self.__v_instance__(node, instance):
				if isinstance(node, Html):
					return self.__v_html__(node)
				if isinstance(node, Head):
					return self.__v_head__(node)
				if isinstance(node, Body):
					return self.__v_body_div__(node)
				if isinstance(node, Div):
					return self.__v_body_div__(node)
				if (isinstance(node, Title) or isinstance(node, H1) or isinstance(node, H2)
					or isinstance(node, Li) or isinstance(node, Th) or isinstance(node, Td)):
					return self.__v_node_with_text(node)
				if isinstance(node, P):
					return self.__v_p__(node)
				if isinstance(node, Span):
					return self.__v_span__(node)
				if isinstance(node, Ul) or isinstance(node, Ol):
					return self.__v_list__(node)
				if isinstance(node, Tr):
					return self.__v_Tr__(node)
				if isinstance(node, Table):
					return self.__v_table__(node)
				if isinstance(node, Text):
					return True
		return False

	def __loop_tree__(self, elem):
		if isinstance(elem, Text):
			return True
		if self.__v_node__(elem) is False:
			return False
		for node in elem.content:
			if self.__loop_tree__(node) is False:
				return False
		return True

	def isvalid(self):
		return self.__loop_tree__(self.elem)

	def write_to_file(self, filename):
		fd = open(filename, 'w')
		fd.write(self.__str__())
		fd.close()

if __name__ == '__main__':
	print("----------------- Creating Fail Case -------------------")
	elem_test_fail = Html([Head(Title(Text('"Hello World"'))),
				Body([H1(Text('"This is a test"')),
				Span(Text('This is span')),
				Div(
					[Ul([Li(Text('This is a li in a ul'))])]),
				H2(Text('h2 element')),
				P(Text('a p section\nla suite')),
				Table([Tr(Th(Text('This is a th in a table'))), Tr(Td(Text('this is a td')))]),
				Ol([Li(Text('<')), Li(Text('>')), Li(Text('"')) ])
				])])
	print("----------------- Creating Success Case ----------------")
	elem_test = Html([Head(Title(Text('"Hello World"'))),
				Body([H1(Text('"This is a test"')),
				Span(Text('This is span')),
				Div(
					[Ul([Li(Text('This is a li in a ul'))])]),
				H2(Text('h2 element')),
				Table([Tr(Th(Text('This is a th in a table'))), Tr(Td(Text('this is a td')))]),
				Ol([Li(Text('<')), Li(Text('>')), Li(Text('"')) ])
				])])

	elem = Html([Head(Title(Text('title'))), Body(Div(Span(Text('span'))))])
	p = Page(Html([Head(Title(Text('title'))), Body(Div(Span(Text('span'))))]))
	print("----------------- Print Simple Page --------------------")
	print(p)
	print("----------------- End Print Simple Page ----------------")
	print('body simple', p.isvalid())
	p = Page(elem_test)
	p.write_to_file('test.html')
	print('page written to file:', p.isvalid())
	p = Page(elem_test_fail)
	print('body with fail case:', p.isvalid())
	print("----------------------Test html-------------------------")
	ph = Page(Html())
	print ('plain html:', ph.isvalid())
	phhb = Page(Html([Head(), Body()]))
	print('html [head, body]:', phhb.isvalid())
	phhb = Page(Html([Body(), Head()]))
	print('html [body, head]:', phhb.isvalid())
	print('test head')
	ph = Page(Head())
	print('head:', ph.isvalid())
	ph = Page(Head(Title()))
	print('head(Title):', ph.isvalid())
	ph = Page(Head([Title(), Div()]))
	print('head([Title, Div]):', ph.isvalid())
	print('test body')
	pb = Page(Body())
	print('body', pb.isvalid())
	pb = Page(Body(Div()))
	print('body(div):', pb.isvalid())
	pb = Page(Body([Div(), Div()]))
	print('body([div, div]):', pb.isvalid())
	pb = Page(Body([Div(),Title(), Div()]))
	print('body([div,title div]):', pb.isvalid())
	print('title, h1')
	pt = Page(Title(Text('ok')))
	print('title(Text(ok)):', pt.isvalid())
	pt = Page(Title([Text('uo'), Text('text_obj')]))
	print('title([Text(uo), Text(text_obj)]):', pt.isvalid())
	pt = Page(Title(Text('ok')))
	print('title(Text(ok)):', pt.isvalid())
	pt = Page(H1([Text('uo'), Text('text_obj')]))
	print('h1([Text(uo), Text(text_obj)]):', pt.isvalid())
	pt = Page(H1(Text('ok')))
	print('h1(Text(ok)):', pt.isvalid())
	pt = Page(H1([Text('uo'), Text('text_obj')]))
	print('h1([Text(uo), Text(text_obj)]):', pt.isvalid())
	print('p')
	p = Page(P(Text('text_obj')))
	print('p(text(text_obj)):', p.isvalid())
	p = Page(P([Text('text_obj'), Text('text_obj')]))
	print('p([text(text_obj), text(text_obj)]):', p.isvalid())
	p = Page(P([Text('text_obj'), Div(), Text('text_obj')]))
	print('p([text(text_obj), div(), text(text_obj)]):', p.isvalid())
	print('span')
	p = Page(Span(Text('ok')))
	print('span(text(text_obj):', p.isvalid())
	p = Page(Span([Text('ok'), P(Text('paragraph_text'))]))
	print('span(text(text_obj), p(paragraph_text)):', p.isvalid())
	p = Page(Span([Text('ok'), Div(), P(Text('paragraph_text'))]))
	print('span(text(text_obj),div, p(paragraph_text)):', p.isvalid())
	print('ul ol')
	p = Page(Ul())
	print('Page(Ul()):', p.isvalid())
	p = Page(Ul(Li()))
	print('Page(Ul(Li())):', p.isvalid())
	p = Page(Ol(Li()))
	print('Page(Ol(Li())):', p.isvalid())
	p = Page(Ol([Li(), Li()]))
	print('Page(Ol(Li(), Li())):', p.isvalid())
	p = Page(Ol([Li(),Div(),  Li()]))
	print('Page(Ol(Li(),Div(), Li())):', p.isvalid())
	p = Page(Tr())
	print('p = Page(Tr()):', p.isvalid())
	p = Page(Tr(Td()))
	print('p = Page(Tr(Td)):', p.isvalid())
	p = Page(Tr([Td(), Th()]))
	print('p = Page(Tr(Td, Th)):', p.isvalid())
	p = Page(Table(Td()))
	print('p = Page(Table(Td)):', p.isvalid())
	p = Page(Table([Tr(), Tr()]))
	print('p = Page(Table(Tr, Tr)):', p.isvalid())
