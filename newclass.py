import random

class Roulette():
	numbers = {(1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36): 'Red',
				(2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35): 'Black',
				0: 'Green',
				}
	def __init__(self, roll, numbers):
		self.roll = random.randint(0, 36)
		self.numbers = numbers
		return self.roll
		print(str(self.roll))

	def display_roll():
		print('hi')
		print(roll)

roll1 = Roulette.display_roll()

print(roll1)
#print(Roulette.roll)
#print(Roulette.numbers.keys(roll))
	#for k, v in numbers.items():
	#	print(self.roll)	
	
def roll():
	result = random.randint(0, 36)
	for result in Roulette.numbers():
		print(result)
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

#roll()


#print(Roulette.check_odd_even(13))
#print(Roulette.roll)
#print(Roulette.numbers)
#print(Roulette.result)
#print(Roulette.check_colour())
#Draw = Roulette(9)
#print(Roulette.rollball(result))
									