from random import randint

TOTAL_PICTURES = 4


def generateNumber():
	'''
	Decide which image to load in-game
	'''
	# Choose index of picture
	number = randint(0, TOTAL_PICTURES - 1)
	return number
