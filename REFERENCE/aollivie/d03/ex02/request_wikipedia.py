import sys, requests, json
from dewiki import parser

def hack_wiki():
	adr = "https://fr.wikipedia.org/w/api.php?action=query&titles="\
			+ sys.argv[1]\
			+"&prop=revisions&redirects=&rvprop=content&format=json&formatversion=2&utf8="

	r = requests.get(adr)
	if not r:
		print('Please check your internet conection')
		return

	if r.status_code != 200:
		print('Not found')
		return

	if not r.text:
		print('Not found')
		return

	s_json = json.loads(r.text)
	if not s_json:
		print('Internal error')

	if 'missing' in s_json['query']['pages'][0] and s_json['query']['pages'][0]['missing'] == True:
		print('Not found')
		return
	content = s_json['query']['pages'][0]['revisions'][0]['content']

	p = parser.Parser()
	new_file = sys.argv[1] + '.wiki'
	fd = open(new_file, 'w')
	if not fd:
		print('Not acess to', new_file)
	fd.write(p.parse_string(content))
	fd.close()
	# print(p.parse_string(content))


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Ivalide number of arguments')
		quit()
	hack_wiki()

	# except Exception as e:
	# 	print('Not found')
