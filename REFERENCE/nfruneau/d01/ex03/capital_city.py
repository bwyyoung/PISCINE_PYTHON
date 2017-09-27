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
    if arg in states :
       print(capital_cities[states[arg]])
    else:
        print("Unknown state")


if __name__ == '__main__' :
    if len(sys.argv) == 2 :
        func(sys.argv[1])
