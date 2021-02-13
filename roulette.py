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
