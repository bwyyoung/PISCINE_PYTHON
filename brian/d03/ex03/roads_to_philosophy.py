#!/usr/bin/python3
# coding : utf8

import sys
import requests
from bs4 import BeautifulSoup


def valid_page_name(page):
	"""
	Checks for valid mainspace Wikipedia page name
	"""
	return (page.find('File:') == -1
			and page.find('File talk') == -1
			and page.find('Wikipedia:') == -1
			and page.find('Wikipedia talk:') == -1
			and page.find('Project:') == -1
			and page.find('Project talk:') == -1
			and page.find('Portal:') == -1
			and page.find('Portal talk:') == -1
			and page.find('Special:') == -1
			and page.find('Help:') == -1
			and page.find('Help talk:') == -1
			and page.find('Template:') == -1
			and page.find('Template talk:') == -1
			and page.find('Talk:') == -1
			and page.find('Category:') == -1
			and page.find('Category talk:') == -1)


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
						if valid_page_name(target):
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