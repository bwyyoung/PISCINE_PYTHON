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

	class BrokenMachineException(Exception):
		def __init__(self, msg= "This coffee machine has to be repaired."):
			super().__init__(self, msg)

	def repair(self):
		self.count = 0

	def serve(self, Drink):
		self.count += 1
		if self.count > 10:
			raise self.BrokenMachineException
		if (random.randint(0, 1) == 1):
			return(Drink())
		return(self.EmptyCup())


if __name__ == '__main__':
	machine = CoffeeMachine()
	for i in range(7):
		try:
			print(machine.serve(Coffee).name)
			print(machine.serve(Chocolate).name)
			print(machine.serve(Cappuccino).name)
			print(machine.serve(Tea).name)
		except machine.BrokenMachineException as e:
			print(e)
			machine.repair()
