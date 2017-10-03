import sys


def find_state(cap,  states, capital_cities):
	for abbrev, capital in capital_cities.items():
		if cap.lower() == capital.lower():
			for state, abbreviation in states.items():
				if abbreviation.lower() == abbrev.lower():
					return [capital, state]
	return None


def find_capital_city(state, states, capital_cities):
	for state_key in states:
		if state_key.lower() == state.lower():
			if capital_cities.get(states[state_key]):
				return [capital_cities[states[state_key]], state_key]
	return None


def split_params(str):
	states = {
		"Oregon": "OR",
		"Alabama": "AL",
		"New Jersey": "NJ",
		"Colorado": "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	values = str.split(",")
	for val in values:
		stripped_val = val.strip(" ")
		if stripped_val:
			ret_state = find_state(stripped_val, states, capital_cities)
			ret_cap = find_capital_city(stripped_val, states, capital_cities)
			if ret_state:
				print("{0} is the capital of {1}".format(ret_state[0], ret_state[1]))
			elif ret_cap:
				print("{0} is the capital city of {1}".format(ret_cap[0], ret_cap[1]))
			else:
				print("{0} is neither a capital city nor a state".format(stripped_val))

if __name__ == '__main__':
	if len(sys.argv) == 2 and sys.argv[1].find(',,') == -1:
		split_params(sys.argv[1])