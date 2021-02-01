import random

class Roulette():
	def __init__(self, numbers):
		numbers = {(1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36): 'Red',
				(2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35): 'Black',
				0: 'Green',
				}

		self.result = result
		

	def rollball():
		result = random.randint(0, 35)

		return result

	def check_colour():
		if result in numbers[0]:
			numbers[0] = True
		elif result in numbers[1]:
			numbers[1] = True
		else:
			numbers[2] 
		return numbers[0, 1, 2]
	rollball()
print(Roulette.check_colour())

result = random.randint(0, 35)
Draw = Roulette(1)
print(Draw.result)
