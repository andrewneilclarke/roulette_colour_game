from random import randint
#import random integer function from random module

wheel = {'Red':[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
				'Black':[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
                'Green':[0],
				}

class Roulette():
	
	def __init__(self, result=None, colour=None, firsttwelve=None, secondtwelve=None, thirdtwelve=None):
		self.result = randint(0, 36)	
		self.colour = colour
		self.firsttwelve = firsttwelve
		self.secondtwelve = secondtwelve
		self.thirdtwelve = thirdtwelve

	
	def roll(self):
	    return randint(0, 36)
	    

	def store_results(self, results, spins):
		# Make some rolls, and store the results in a list.
		results = []
		self.results = results
		self.spins = spins
		for x in range(spins):
		    result = R.roll()	
		    results.append(result)
		return results

	def is_even(self):
		#check if the result was odd or even and return the result
		if self.result % 2 == 0:
			return True
		else:
			return False

	def check_colour(self, result):
		self.result = result
		if result in wheel['Red']:
			self.colour = 'Red'
		elif result in wheel['Black']:
			self.colour = 'Black'
		else:
			self.colour = 'Green'
		return self.colour
	
	def check_twelve(self, result):
		self.result = result
		if result > 0 < 13:
			return 'First 12'
		elif result > 12:
			return 'Second 12'
		else:
			return 'Third 12'

	def check_second12(self, result):
		self.result = result
		if result > 12 < 25:
			return True
		else:
			return False

	def check_last12(self, result):
		self.result = result
		if result > 12 < 25:
			return True
		else:
			return False

R = Roulette()
x = (R.roll())

#print(R.store_results(x, 9))
#print(R.check_even_odd(x))
#print(R.check_red_black_green(x))
#print(R.check_twelve(x))
#print(R.check_colour(x))
J = Roulette()
print(J.result)
print(J.is_even())
print(J.firsttwelve())

#print(J.store_results(x, 9))

"""

for c, l in wheel.items():
    for n in l:
        if n == x:
            print(c, n)


#for k in numbers.keys():
#	k.print(numbers[R.roll()])

roll1 = Roulette.display_roll()

print(roll1)
#print(Roulette.roll)
#print(Roulette.numbers.keys(roll))
	#for k, v in numbers.items():
	#	print(self.roll)	
	"""
