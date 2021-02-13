from random import randint

class Roulette():
	#represent the roulette wheel which has 37 outcomes
	def __init__(self):
	    self.number = randint(0, 37)
	    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36,]
	    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35,]
	    green = [0]
	    if self.number in red:
	    	self.colour = "Red"
	    elif self.number in black:
	        self.colour = 'Black'
	    else:
	        self.colour = 'Green'

	def is_even(self):
		#check if the result was even or not
		if self.number == 0:
			return False
		elif self.number % 2 == 0:
			return True
		else:
			return False

	def check_twelve(self):
		if self.number == 0:
			return None
		elif self.number < 13:
			return 'First 12'
		elif self.number < 25:
			return 'Second 12'
		else:
			return 'Third 12'

r1 = Roulette()
print(r1.number)
print(r1.colour)
print(r1.is_even())
print(r1.check_twelve())
r2 = Roulette()
print(r2.number)
print(r2.colour)
print(r2.check_twelve())



"""

	def store_results(self, results, spins):
		# Make some rolls, and store the results in a list.
		results = []
		self.results = results
		self.spins = spins
		for x in range(spins):
		    result = J.roll()	
		    results.append(result)
		return results
	
	def check_twelve(self):
		if self.result < 13:
			return 'First 12'
		elif self.result < 25:
			return 'Second 12'
		else:
			return 'Third 12'

R = Roulette()
x = (R.roll())

print(R.store_results(x, 9))
print(R.is_even())
print(R.assign_colour(x))
print(R.check_twelve(x))

J = Roulette(2)
x = J.roll()
print(J.result)
print(J.is_even())
print(J.check_twelve())
print(J.store_results(x, 5))



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
