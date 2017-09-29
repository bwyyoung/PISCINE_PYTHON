#!/usr/bin/python3
# coding : utf8

import sys
import requests
from bs4 import BeautifulSoup


def web_request(req):
	url = 'https://en.wikipedia.org/wiki/' + req
	r = requests.get(url)
	if r.status_code != 200:
		if r.status_code == 404:
			print('It leads to a dead end !')
		else:
			print('HTTP error ', str(r.status_code))
		exit(1)
	soup = BeautifulSoup(r.text, 'html.parser')
	content = soup.find(id="mw-content-text")
	for para in content.find_all('p'):
		for link in para.find_all('a', attrs={}):
			if not link['href'].startswith('/wiki/'):
				continue
			if str(link).find('title') > 0:
				target = link['title']
				if target:
					if not target.startswith('Help:'):
						return target
	print('It leads to a dead end !')
	exit(1)


def process_request(req):
	roads = [req]
	while (req.lower() != 'philosophy'):
		req = web_request(req)
		if req in roads:
			print('It leads to an infinite loop !')
			exit(1)
		roads.append(req)
	for road in roads:
		print(road)
	print(str(len(roads)) + " roads from " + roads[0] + " to philosophy")

def usage():
	print("Usage : python3 roads_to_philosophy.py string_search_query")

if __name__ == '__main__':
	if len(sys.argv) == 2:
		process_request(sys.argv[1])
	else:
		usage()