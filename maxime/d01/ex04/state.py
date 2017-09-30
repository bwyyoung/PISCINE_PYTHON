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

def find_name(abbr):
	for key, value in states().items():
		if value == abbr:
			print key
			return

def finder(city):
	for key, value in cities().items():
		if value == city:
			find_name(key)
			return
	print("Unknown capital city")

def starter():
	if len(sys.argv) == 2:
		finder(sys.argv[1])
	return

starter()
