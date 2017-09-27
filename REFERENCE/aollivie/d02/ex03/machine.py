import random
from beverages import HotBeverage, Coffee, Chocolate, Cappuccino, Tea

class CoffeeMachine:
	def __init__(self):
		self.drink = 0

	class EmptyCup(HotBeverage):
		price = 0.90
		name = "empty cup"
		def description(self):
			return("An empty cup?! Gimme my money back!")

	class BrokenMachineException(Exception):
		def __init__(self):
			self.raison = "This coffee machine has to be repaired."
		def __str__(self):
			return self.raison

	def repair(self):
		self.drink = 0

	def serve(self, drink):
		if self.drink == 10:
			raise self.BrokenMachineException()
		self.drink += 1
		ran = random.randrange(2)
		if ran:
			return (drink())
		return (self.EmptyCup())

if __name__ == '__main__':
	machine = CoffeeMachine()
	try:
		print(machine.serve(Coffee))
		print(machine.serve(Chocolate))
		print(machine.serve(Cappuccino))
		print(machine.serve(Coffee))
		print(machine.serve(Coffee))
		print(machine.serve(Cappuccino))
		print(machine.serve(Cappuccino))
		print(machine.serve(Chocolate))
		print(machine.serve(Chocolate))
		print(machine.serve(Coffee))
		print(machine.serve(Tea))
		print(machine.serve(Coffee))
		print(machine.serve(Coffee))
		print(machine.serve(Tea))
		print(machine.serve(Cappuccino))
		print(machine.serve(Chocolate))
	except machine.BrokenMachineException as e:
		print(e)
	machine.repair()
	try:
		print(machine.serve(Coffee))
		print(machine.serve(Chocolate))
		print(machine.serve(Cappuccino))
		print(machine.serve(Coffee))
		print(machine.serve(Coffee))
		print(machine.serve(Cappuccino))
		print(machine.serve(Cappuccino))
		print(machine.serve(Chocolate))
		print(machine.serve(Coffee))
		print(machine.serve(Cappuccino))
		print(machine.serve(Cappuccino))
		print(machine.serve(Tea))
		print(machine.serve(Chocolate))
		print(machine.serve(Coffee))
		print(machine.serve(Coffee))
		print(machine.serve(Coffee))
	except machine.BrokenMachineException as e:
		print(e)
