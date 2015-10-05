from random import randint

TOTAL_POKEMON = 9
FILE_NAMES = [
	'001Bulbasaur.png',
	'002Ivysaur.png',
	'003Venusaur.png',
	'004Charmander.png',
	'005Charmeleon.png',
	'006Charizard.png',
	'007Squirtle.png',
	'008Wartortle.png',
	'009Blastoise.png',
]


def random_pokemon():
	'''
	Decide which pokemon image to load in-game
	'''
	# Choose index of picture
	number = randint(0, TOTAL_POKEMON - 1)
	return FILE_NAMES[number]
