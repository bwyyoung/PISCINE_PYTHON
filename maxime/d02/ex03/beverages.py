
class HotBeverage:
	price = 0.3
	name = 'beverage'

	def __str__(self):
		return (
			'name : ' + self.name + '\n'
			'price : ' + '%.2f' % self.price + '\n'
			'description : ' + self.description())

	def description(self):
		return ('Just some hot water in a cup.')

class Coffee(HotBeverage):
	price = 0.4
	name = 'coffee'

	def description(self):
		return ('A coffee, to stay awake.')

class Tea(HotBeverage):
	name = 'tea'

class Chocolate(HotBeverage):
	price = 0.5
	name = 'chocolate'

	def description(self):
		return ('Chocolate, sweet chocolate...')

class Cappuccino(HotBeverage):
	price = 0.45
	name = 'cappuccino'

	def description(self):
		return ('Un po’ di Italia nella sua tazza!')

if __name__ == '__main__':
	beverage = HotBeverage()
	coffee = Coffee()
	chocolate = Chocolate()
	cappuccino = Cappuccino()
	tea = Tea()
	print(beverage)
	print(coffee)
	print(tea)
	print(chocolate)
	print(cappuccino)
