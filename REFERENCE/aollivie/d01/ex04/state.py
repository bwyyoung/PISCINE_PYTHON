import sys

def get_dict_states():
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	return (states)

def get_dict_capital():
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	return (capital_cities)

def get_capital_key(capital_cities_dict, capital):
	for key, value in capital_cities_dict.items():
		if value == capital:
			return key
	return

def get_state(states_dict, key_capital):
	for key, value in states_dict.items():
		if value == key_capital:
			return key
	return

if __name__ == '__main__':
	if len(sys.argv) != 2:
		quit()
	capital = sys.argv[1]
	states_dict = get_dict_states()
	capital_cities_dict = get_dict_capital()
	key_capital = get_capital_key(capital_cities_dict, capital)
	state = get_state(states_dict, key_capital)
	if state:
		print(state)
		quit()
	print('Unknown state')
