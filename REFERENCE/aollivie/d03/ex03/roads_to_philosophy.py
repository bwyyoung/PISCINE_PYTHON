import requests
from bs4 import BeautifulSoup
import sys


def hack_wiki(query):
	url = 'https://en.wikipedia.org/wiki/'
	url_target = url + query
	r = requests.get(url_target)
	if not r:
		print('It leads to a dead end !')
		return
	html_doc = r.text
	soup = BeautifulSoup(html_doc, 'html.parser')
	title = str(soup.title.string)
	title = title.replace(' - Wikipedia', '')


	content = soup.find(id="mw-content-text")
	p = content.p
	if not p:
		pass
		print('It leads to a dead end !')
		return
	b = p.b
	if not b:
		print('It leads to a dead end !', b.string)
		return
	a = p.find_all('a')
	if not a:
		print('It leads to a dead end !')
		return

	for v in a:
		if str(v).find('title') > 0:
			target = v['title']
			if not target:
				continue
			if not target.startswith('Help:'):
				return target

def ispresent(list, value):
	for v in list:
		if v == value:
			return True
	return False

def process(query):
	road = []
	road.append(query)
	while (query != 'Philosophy'):
		query = hack_wiki(query)
		if not query:
			return
		if ispresent(road, query):
			print('It leads to an infinite loop !')
			return
		road.append(query)
	for v in road:
		print(v)


if __name__ == '__main__':
	if len(sys.argv) != 2:
		('Invalide number of argument')
		quit()
	process(sys.argv[1])
