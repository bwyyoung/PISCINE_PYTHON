import sys

def states():
	states = {
		"Oregon"    : "OR",
		"Alabama"   : "AL",
		"New Jersey": "NJ",
		"Colorado"  : "CO"
	}
	return states

def cities():
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	return capital_cities

def printer(city, state):
	print "%s is the capital of %s" % (city, state)

def state_from_capital(city):
	for key, value in cities().items():
		if value.lower() == city.lower():
			for state, abbr in states().items():
				if abbr.lower() == key.lower():
					return [city, state]
	return -1
	
def capital_from_state(state):
	for key, value in states().items():
		if key.lower() == state.lower():
			for abbr, capital in cities().items():
				if abbr == value:
					return [capital, state]
	return -1

def finder(array):
	for item in array:
		item = item.strip(" ")
		if item:
			c = capital_from_state(item)
			s = state_from_capital(item)
			if c != -1:
				printer(c[0], c[1])
			elif s != -1:
				printer(s[0], s[1])
			else:
				print "%s is neither a capital city nor a state" % (item)

def checker(s):
	if s.find(',,') == -1:
		array = s.split(',')
		finder(array)
	else:
		print 'Bad argv'

def starter():
	if len(sys.argv) == 2:
		checker(sys.argv[1])
	return

starter()
