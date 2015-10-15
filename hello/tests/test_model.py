from django.test import TestCase

from hello.constants import TOTAL_POKEMON
from hello.models import Attempt, check


class AttemptTests(TestCase):
    def setUp(self):
        self.attempt = Attempt.objects.create()

    def test_check(self):
        self.attempt.last_guess = 'ChariZArD'
        self.attempt.last_poke_id = 6
        self.attempt.save()
        self.assertTrue(check(self.attempt))

        self.attempt.last_poke_id = 7
        self.attempt.save()
        self.assertFalse(check(self.attempt))

    def test_guessed_id_list(self):
        self.attempt.guessed_pokes = "[1, 2, 3]"
        expected = [1, 2, 3]
        actual = self.attempt.guessed_id_list
        self.assertEqual(expected, actual)

    def test_append_poke_id(self):
        self.attempt.guessed_pokes = "[1, 2, 3]"
        self.attempt.last_poke_id = 4
        self.attempt.append_poke_id()
        expected = "[1, 2, 3, 4]"
        actual = self.attempt.guessed_pokes
        self.assertEqual(expected, actual)

    def test_not_guessed_id_list(self):
        self.attempt.guessed_pokes = "[1, 2, 3]"
        expected = [4, 5, 6, 7, 8, 9]
        actual = self.attempt.not_guessed_id_list
        self.assertEqual(expected, actual)

    def test_game_complete(self):
        self.attempt.score = TOTAL_POKEMON - 1
        self.assertFalse(self.attempt.complete)
        self.attempt.score = TOTAL_POKEMON
        self.assertTrue(self.attempt.complete)
