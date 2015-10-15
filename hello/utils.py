from random import randint


from hello.constants import FILE_NAMES, POKEMON_NAMES


def random_id(attempt):
    '''
    Randomly return a pokemon id which hasn't been seen yet
    '''
    ids_to_choose_from = attempt.not_guessed_id_list
    return ids_to_choose_from[randint(0, len(ids_to_choose_from) - 1)]


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
