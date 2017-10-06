# pip3 install -r requirement.txt -t './' --upgrade
# https://stackoverflow.com/questions/24257803/distutilsoptionerror-must-supply-either-home-or-prefix-exec-prefix-not-both

import sys, json
from local_lib import requests, dewiki

def writer(search, result):
	filename = search.replace(" ", "_") + ".wiki"
	with open(filename, "w") as f:
		f.write(result)


def reader(json, search):
	if json.get('query'):
		query = json['query']
		if query.get('pages'):
			pages = query['pages']
			result = ""
			for pageid in pages:
				page = pages[pageid]
				if page.get('revisions'):
					revisions = page['revisions']
					if revisions[0].get('*'):
						result += revisions[0]['*'] + "\n"
					result = dewiki.from_string(result)
					writer(search, result)
				else:
					print('Bad search')


def request(search):
	source = 'https://en.wikipedia.org/w/api.php'
	p = {'action': 'query', 'titles': search, 'prop': 'revisions','rvprop': 'content', 'format': 'json'}
	r = requests.get(source, p)
	# print(r.headers)
	if r.status_code == 200:
		try:
			json = r.json()
			reader(json, search)
		except ValueError as e:
			print(e)
	else:
		print('Http error: {}'.format(r.status_code))


if __name__ == '__main__':
	if len(sys.argv) == 2:
		request(sys.argv[1])
	else:
		print("usage: python3 request_wikipedia.py <string_search_query>")
