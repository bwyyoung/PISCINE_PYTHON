import random
from beverages import HotBeverage, Coffee, Chocolate, Cappuccino, Tea

class CoffeeMachine:
	def __init__(self):
		self.count = 0

	class EmptyCup(HotBeverage):
		name = "empty cup"
		price = 0.9
		def description(self):
			return("An empty cup?! Gimme my money back!")
