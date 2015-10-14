from django.test import TestCase

from hello.models import Attempt


class AttemptTests(TestCase):
    def setUp(self):
        self.attempt = Attempt.objects.create()

    def test_check(self):
        self.attempt.last_guess = 'ChariZArD'
        self.attempt.last_poke_id = 6
        self.attempt.save()
        self.assertTrue(self.attempt.check())

        self.attempt.last_poke_id = 7
        self.attempt.save()
        self.assertFalse(self.attempt.check())
