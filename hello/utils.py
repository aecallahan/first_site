from random import randint

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
TOTAL_POKEMON = len(FILE_NAMES)


def random_pokemon():
    '''
    Randomly return a string which matches a image file name
    '''
    # Choose index of picture
    number = randint(0, TOTAL_POKEMON - 1)
    return FILE_NAMES[number]
