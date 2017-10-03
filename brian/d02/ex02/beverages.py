
class Beverage:
	price = 0.30
	name = "hot beverage"

	def __str__(self):
		s = "name : " + self.name + "\nprice : " + str(self.price) + "\ndescription : " + self.description()
		return s

	def description(self):
		return "Just some hot water in a cup."


class Coffee(Beverage):
	price = 0.40
	name = "coffee"

	def description(self):
		return "A coffee, to stay awake."


class Cappuccino(Beverage):
	price = 0.45
	name = "cappuccino" 

	def description(self):
		return "Un po' di Italia nella sua tazza!"


class Chocolate(Beverage):
	price = 0.50
	name = "chocolate"

	def description(self):
		return "Chocolate, sweet chocolate..."


class Tea(Beverage):
	name = "tea"


if __name__ == '__main__' :
	b = Beverage()
	print(b)
	c = Coffee()
	print(c)
	t = Tea()
	print(t)
	choc = Chocolate()
	print(choc)
	cappuccino = Cappuccino()
	print(cappuccino)
