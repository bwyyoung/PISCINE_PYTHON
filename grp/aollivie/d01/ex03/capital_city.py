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

def get_capital(states_dict, capital_cities_dict, state):
	if state in states_dict:
		value_state = states_dict[state]
		if value_state in capital_cities_dict:
			value_capital = capital_cities_dict[value_state]
			return (value_capital)
	return
if __name__ == '__main__':
	if len(sys.argv) != 2:
		quit()
	state = sys.argv[1]
	states_dict = get_dict_states()
	capital_cities_dict = get_dict_capital()
	capital = get_capital(states_dict, capital_cities_dict, state)
	if capital:
		print(capital)
		quit()
	print('Unknown state')
