#!/usr/local/bin/python3

import sys

def	func(arg) :
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
    if arg in capital_cities.values() :
        for key, value in capital_cities.items():
            if arg == value :
                for key2, value2 in states.items():
                    if key == value2 :
                        print(key2)
    else:
        print("Unknown capital city")

if __name__ == '__main__' :
    if len(sys.argv) == 2 :
        func(sys.argv[1])
