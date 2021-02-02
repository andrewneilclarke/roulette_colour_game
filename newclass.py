from random import randint
#import random integer function from random module
wheel = {'Red':[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
				'Black':[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
                'Green':[0],
				}

class Roulette():
	
	def __init__(self, outcomes=37):
		self.outcomes = outcomes	
		
	
	def roll(self):
	    return randint(0, self.outcomes-1)
	    

	def store_results(self, results):
		# Make some rolls, and store the results in a list.
		results = []
		self.results = results
		for x in range(15):
		    result = R.roll()	
		    results.append(result)
		return results

	def check_even_odd(self, result):
		#check if the result was odd or even and return the result
		self.result = result
		if result % 2 == 0:
			return True
		else:
			return False
	def check_red_black_green(self, result):
		self.result = result
		for c, l in wheel.items():
			for n in l:
				if n == result:
					return c
		

R = Roulette()
x = (R.roll())

#print(R.store_results(x))
#print(R.check_even_odd(x))
print(R.check_red_black_green(x))


"""   
# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
"""



for c, l in wheel.items():
    for n in l:
        if n == x:
            print(c, n)


#for k in numbers.keys():
#	k.print(numbers[R.roll()])
"""
roll1 = Roulette.display_roll()

print(roll1)
#print(Roulette.roll)
#print(Roulette.numbers.keys(roll))
	#for k, v in numbers.items():
	#	print(self.roll)	
	




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
									"""