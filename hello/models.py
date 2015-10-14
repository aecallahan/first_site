from django.db import models

from hello.utils import pokemon_name


class Attempt(models.Model):
    '''
    Represents an attempt to play the game
    '''
    score = models.IntegerField(default=0)
    player_name = models.CharField(max_length=25, null=True)
    last_guess = models.CharField(max_length=50, null=True)
    last_poke_id = models.IntegerField(null=True)

    def __str__(self):
        return "Name: %s, Score: %s" % (self.player_name, self.score)

    class Meta:
        # Sort attempt objects from highest to lowest score
        ordering = ['-score']


def check(attempt):
    '''
    Check that the most recent guess matches the most recent pokemon
    '''
    if not attempt.last_guess and attempt.last_poke_id:
        return False

    correct_name = pokemon_name(attempt.last_poke_id)
    return correct_name == attempt.last_guess.lower()
