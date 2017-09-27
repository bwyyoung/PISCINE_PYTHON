import sys
import requests
from bs4 import BeautifulSoup

def func(arg):
	result = requests.get("https://en.wikipedia.org/wiki/" + arg)
	c = result.content
	soup = BeautifulSoup(c, "html.parser")
	title = soup.title
	print(title)
	p = soup.find(id="mw-content-text")
	p = p.find_all('p', recursive=False)
	for item in range(len(p)):
		print(p[item])

if __name__ == '__main__':
	try:
		if len(sys.argv) != 2:
			raise Exception ("Usage: ./roads_to_philosophy.py <research>")
		func(sys.argv[1])
	except Exception as e:
		print (e)
