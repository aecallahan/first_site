from django.test import TestCase

from hello.utils import FILE_NAMES, random_pokemon


class ImageLoaderTests(TestCase):
    def test_random_pokemon(self):
        file_name = random_pokemon()
        self.assertIn(file_name, FILE_NAMES)
