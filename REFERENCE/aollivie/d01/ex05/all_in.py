import sys

def print_capital_state(capital, state):
	print(capital, 'is the capital of', state)

def print_not_found(name):
	print(name, 'is neither a capital city nor a state')

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

def get_state_value(key, states_dict):
	if key in states_dict:
		return states_dict[key]
	return

def get_capital_value(key, capital_cities_dict):
	if key in capital_cities_dict:
		return capital_cities_dict[key]


def get_capital_key(capital, capital_cities_dict):
	for key, value in capital_cities_dict.items():
		if value == capital:
			return key
	return

def get_state_key(key_capital, states_dict):
	for key, value in states_dict.items():
		if value == key_capital:
			return key
	return

def process(target, states_dict, capital_cities_dict, notFound):
	result = get_state_value(target, states_dict)
	if result:
		print_capital_state(
		get_capital_value(result, capital_cities_dict), target)
		return
	result = get_capital_key(target, capital_cities_dict)
	if result:
		print_capital_state(target, get_state_key(result, states_dict))
		return
	print_not_found(notFound)
	return

if __name__ == '__main__':
	if len(sys.argv) != 2:
		quit()
	str_city = sys.argv[1].replace('"', '')
	list_city = str_city.split(',')
	states_dict = get_dict_states()
	capital_cities_dict = get_dict_capital()
	for city in list_city:
		new = city.strip()
		if len(new):
			new_lower = new.lower()
			new_title = new.title()
			process(new_title, states_dict, capital_cities_dict, new)
