class HotBeverage:
	price = 0.30
	name = "hot beverage"
	def description(self):
		return ("Just some hot water in a cup.")

	def __str__(self):
		return (
			'name : ' + self.name +
			'\nprice : ' + "%.2f"%self.price +
			'\ndescription : ' + self.description())

class Coffee(HotBeverage):
	price = 0.40
	name = "coffe"
	def description(self):
		return("A coffee, to stay awake.")

class Chocolate(HotBeverage):
	price = 0.50
	name = "chocolate"
	def description(self):
		return("Chocolate, sweet chocolate...")

class Cappuccino(HotBeverage):
	price = 0.45
	name = "cappuccino"
	def description(self):
		return("Un po’ di Italia nella sua tazza!")

class Tea(HotBeverage):
	name = "tea"

if __name__ == '__main__':
	hot = HotBeverage()
	coffee = Coffee()
	chocolate = Chocolate()
	cappuccino = Cappuccino()
	tea = Tea()
	print(hot)
	print(coffee)
	print(chocolate)
	print(cappuccino)
	print(tea)
