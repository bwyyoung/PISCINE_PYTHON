#!/usr/local/bin/python3

import sys

def	func(name) :
    arg = " ".join(name.title().split())
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }
    if arg in states :
       print(capital_cities[states[arg]], "is the capital of", arg)
    elif arg in capital_cities.values() :
        for key, value in capital_cities.items():
            if arg == value :
                for key2, value2 in states.items():
                    if key == value2 :
                        print(arg, "is the capital of", key2)
    else:
        print(name, "is neither a capital city nor a state")

if __name__ == '__main__' :
    if len(sys.argv) == 2 :
        tab = sys.argv[1].split(',')
        for var in range(len(tab)):
            if len(tab[var].strip()) > 0:
                func(tab[var].strip())
