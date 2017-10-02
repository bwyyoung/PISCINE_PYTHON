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

def finder(state):
	abbr = states().get(state)
	if not abbr:
		print("Unknown state")
		return 
	capital = cities().get(abbr)
	print(capital)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		finder(sys.argv[1])
