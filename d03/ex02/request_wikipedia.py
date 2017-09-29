#!/usr/bin/python3
# coding : utf8

import sys
import requests
import json
import dewiki


def write_in_file(req, txt):
	filename = req.replace(" ", "_") + ".wiki"
	f = open(filename, "w")
	f.write(txt)
	f.close()


def process_request(req):
	url = 'https://en.wikipedia.org/w/api.php'
	payload = {'action': 'query', 'titles': req, 'prop': 'revisions','rvprop': 'content', 'format': 'json'}
	r = requests.get(url, params=payload)
	if r.status_code != 200:
		print("Erreur HTTP, code ", str(r.status_code))
		exit(1)
	res = r.json()
	if res.get('query'):
		query = res['query']
		if query.get('pages'):
			pages = query['pages']
			txt = ""
			for pageid in pages:
				page = pages[pageid]
				if page.get('revisions'):
					revisions = page['revisions']
					if revisions[0].get('*'):
						txt += revisions[0]['*'] + "\n"
					txt = dewiki.from_string(txt)
			write_in_file(req, txt)


def usage():
	print("Arguments: python3 request_wikipedia.py string_search_query")

if __name__ == '__main__':
	if len(sys.argv) == 2:
		process_request(sys.argv[1])
	else:
		usage()
