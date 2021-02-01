import random

class Roulette():
	def __init__(self, numbers):
		self.numbers = {(1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36): 'Red',
				(2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35): 'Black',
				0: 'Green',
				}
		
	def roll(numbers):
		result = random.randint(0, 36)
		for k, v in numbers.keys():
			print(k)
		return result
	
	def check_odd_even(result):
		""" check if the result was odd or even and return the result """
		odd = False
		even = False
		if result % 2 == 0:
			even = True
		else:
			odd = True
		return odd, even

	def check_colour():
		if result in numbers[0]:
			numbers[0] = True
		elif result in numbers[1]:
			numbers[1] = True
		else:
			numbers[2] 
		return numbers[0, 1, 2]
	#roll(numbers)

print(Roulette.check_odd_even(13))
print(Roulette.roll)
#print(Roulette.numbers)
#print(Roulette.result)
#print(Roulette.check_colour())
#Draw = Roulette(9)
#print(Roulette.rollball(result))
