#!/usr/local/bin/python3

import beverages
import random

class CoffeeMachine:

	def __init__(self):
		self.count = 0

	class EmptyCup(beverages.HotBeverage):
		Name = "empty cup"
		Price = 0.90
		des = "An empty cup?! Gimme my money back!"

	class BrokenMachineException(Exception):
		def __init__(self):
			self.msg = "This coffee machine has to be repaired."

	def repair(self):
		self.count = 0

	def serve(self, arg):
		try:
			if isinstance(arg, beverages.HotBeverage) == False:
				raise Exception ("Type Error")
		except Exception as e:
			print (e)
			arg = self.EmptyCup()
		self.count += 1
		if self.count > 10:
			raise self.BrokenMachineException()
		return random.choice([arg, self.EmptyCup()])

if __name__ == '__main__':
	var = CoffeeMachine()
	try:
		for i in range(20):
			bev = var.serve(arg = random.choice([beverages.Coffee(), beverages.Tea(), beverages.Chocolate(), beverages.Capuccino()]))
			print(bev.des)
	except Exception as e:
		print(e.msg)
	var.repair()
	try:
		for i in range(20):
			bev = var.serve(beverages.Coffee())
			print(bev.des)
	except Exception as e:
		print(e.msg)
