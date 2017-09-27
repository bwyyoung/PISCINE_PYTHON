import sys
import requests
import json
from dewiki.parser import Parser

def func(arg, count):
	r = requests.get("https://fr.wikipedia.org/w/api.php?action=query&titles="+arg+"&prop=revisions&redirects=&rvprop=content&format=json&formatversion=2&utf8=")
	if r.status_code != 200:
		raise Exception ("status code error: " + str(r.status_code))
	dic = json.loads(r.text)
	try:
		if 'missing' in dic['query']['pages'][0]:
			count += 1
			if count == 1:
				func(arg.capitalize(), count)
			elif count == 2:
				func(arg.title(), count)
			else:
				raise Exception ("L'article « " + arg + " » n'existe pas sur ce wiki !")
			return
		res = dic['query']['pages'][0]['revisions'][0]['content']
		name = dic['query']['pages'][0]['title']
		with open("_".join(name.split()) + ".wiki", 'w') as f:
			f.write(Parser().parse_string(res) + "\n")
	except Exception as e:
		print (e)

if __name__ == '__main__':
	try:
		if len(sys.argv) != 2:
			raise Exception ("Usage: ./request_wikipedia.py <request>")
		func(sys.argv[1], 0)
	except Exception as e:
		print(e)
