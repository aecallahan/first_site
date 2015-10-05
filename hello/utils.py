from random import randint

TOTAL_PICTURES = 4
FILE_NAMES = [
	'lang-logo.png',
	'one.png',
	'two.jpg',
	'three.jpg'
]


def random_image():
	'''
	Decide which image to load in-game
	'''
	# Choose index of picture
	number = randint(0, TOTAL_PICTURES - 1)
	return FILE_NAMES[number]
