class HotBeverage:
	Price = 0.30
	Name = "hot beverage"
	des = "Just some hot water in a cup."

	def description(self):
		return self.des

	def __str__(self):
		return "name : " + self.Name + "\nprice : " + ('%.2f' %self.Price) + "\ndescription : " + self.des

class Coffee(HotBeverage):
	Price = 0.40
	Name = "coffee"
	des = "A coffee, to stay awake."

class Tea(HotBeverage):
	Name = "tea"

class Chocolate(HotBeverage):
	Price = 0.50
	Name = "chocolate"
	des = "Chocolate, sweet chocolate..."

class Capuccino(HotBeverage):
	Price = 0.45
	Name = "capuccino"
	des = "Un po' di Italia nella sua tazza!"
