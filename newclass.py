class Roulette():
	def __init__(self, numbers, colours):
		numbers = {'Red': (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36),
					'Black': (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35),
					'Green': (0)
					}

		self.numbers = numbers
		self.colours = numbers.keys()

Draw = Roulette('Red', 'Black')
print(Draw.colours)
