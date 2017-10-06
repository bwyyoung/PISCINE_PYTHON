# pip3 install -r requirement.txt -t './local_lib' --upgrade
import sys, requests
from bs4 import BeautifulSoup


def request(search):
	url = 'https://en.wikipedia.org/wiki/' + search
	r = requests.get(url)
	if r.status_code == 200:
		soup = BeautifulSoup(r.text, 'html.parser')
		print(soup.title)
		div = soup.find("div", "mw-parser-output")
		paragraphs = div.find_all('p', recursive=False)
		for p in paragraphs:
			for link in p.find_all('a', recursive=False):
				print(link['title'])
				print(link['href'])

if __name__ == '__main__':
	if len(sys.argv) == 2:
		request(sys.argv[1])
	else:
		print('usage: py roads_to_philosophy.py <your search>')
