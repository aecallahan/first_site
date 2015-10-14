from django.test import TestCase

from hello.constants import TOTAL_POKEMON
from hello.utils import random_id, image_file, pokemon_name


class UtilsTests(TestCase):
    def test_random_pokemon_id(self):
        expected = range(1, TOTAL_POKEMON + 1)
        actual = random_id()
        self.assertIn(actual, expected)

    def test_image_file(self):
        poke_id = 4
        expected = '004Charmander.png'
        actual = image_file(poke_id)
        self.assertEqual(expected, actual)

    def test_pokemon_name(self):
        poke_id = 6
        expected = 'Charizard'
        actual = pokemon_name(poke_id)
        self.assertEqual(expected, actual)
