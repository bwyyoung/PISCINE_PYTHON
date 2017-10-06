# pip3 install -r requirement.txt -t './local_lib' --upgrade
import sys, requests
from bs4 import BeautifulSoup

def request(search):
	url = 'https://en.wikipedia.org/wiki/' + search
	r = requests.get(url)
	if r.status_code == 200:
		soup = BeautifulSoup(r.text, 'html.parser')
		div = soup.find("div", "mw-parser-output")
		paragraphs = div.find_all('p', recursive=False)
		for p in paragraphs:
			for link in p.find_all('a', recursive=False):
				if not link['href'].startswith('/wiki/'):
					continue
				target = link['title']
				if target and target.startswith('Help:') == False:
					return(link['title'])
	else:
		print('It leads to a dead end !')
		exit(1)


def loop_request(search):
	roads = [search]
	while (search.lower() != 'philosophy'):
		print(search)
		search = request(search)
		if search in roads:
			print('It leads to an infinite loop !')
			exit(1)
		roads.append(search)
	print("{} roads from {} to philosophy !".format(len(roads), roads[0]))


if __name__ == '__main__':
	if len(sys.argv) == 2:
		loop_request(sys.argv[1])
	else:
		print('usage: py roads_to_philosophy.py <your search>')
