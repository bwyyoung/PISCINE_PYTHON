# pip3 install -r requirement.txt -t './local_lib' --upgrade
import sys, requests
from bs4 import BeautifulSoup

def request(search):
	url = 'https://fr.wikipedia.org/wiki/' + search
	r = requests.get(url)
	if r.status_code == 200:
		soup = BeautifulSoup(r.text, 'html.parser')
		print(soup.prettify())

if __name__ == '__main__':
	if len(sys.argv) == 2:
		request(sys.argv[1])
	else:
		usage()
