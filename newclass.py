from random import randint
#import random integer function from random module

class Roulette():
	
	def __init__(self, outcomes=37):
		self.outcomes = outcomes	


	def roll(self):
	    return randint(0, self.outcomes-1)
	    

	def assign_outcome(self, x):
		self.x = x
		wheel = {'Red':[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
				'Black':[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
	            'Green':[0],
					}
	
	
	def store_results(self, results):
		# Make some rolls, and store the results in a list.
		results = []
		self.results = results
		for x in range(15):
		    result = R.roll()	
		    results.append(result)
		return results



R = Roulette()
x = (R.roll())
#print(x)
#assign_outcome(x)
#print(R.store_results())

#store_results()

"""   
# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
"""

wheel = {'Red':[1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
				'Black':[2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35],
                'Green':[0],
				}

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
	


def check_odd_even(result):
	#check if the result was odd or even and return the result
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
									"""