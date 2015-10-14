from random import randint


from hello.constants import FILE_NAMES, POKEMON_NAMES, TOTAL_POKEMON


def random_id():
 	'''
 	Return a random pokemon id
	'''
	return randint(1, TOTAL_POKEMON)


def image_file(pokemon_id):
    '''
    Return the image file name associated with a pokemon's id
    '''
    return FILE_NAMES[pokemon_id - 1]


def pokemon_name(pokemon_id):
	'''
	Return a pokemon name given its id
	'''
	return POKEMON_NAMES[pokemon_id - 1]
