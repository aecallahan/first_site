import ast
from django.db import models

from hello.constants import TOTAL_POKEMON
from hello.utils import pokemon_name


class Attempt(models.Model):
    '''
    Represents an attempt to play the game
    '''
    score = models.IntegerField(default=0)
    player_name = models.CharField(max_length=25, null=True)
    last_guess = models.CharField(max_length=50, null=True)
    last_poke_id = models.IntegerField(null=True)
    guessed_pokes = models.CharField(max_length=2000, default="[]")

    @property
    def guessed_id_list(self):
        '''
        Returns a list representation of the id's of guessed pokemon
        '''
        return ast.literal_eval(self.guessed_pokes)

    @property
    def not_guessed_id_list(self):
        '''
        Return a list of id's of pokemon which haven't been guessed yet
        '''
        all_ids = range(1, TOTAL_POKEMON + 1)
        return [poke_id for poke_id in all_ids if poke_id not in self.guessed_id_list]

    @property
    def complete(self):
        return self.score == TOTAL_POKEMON

    @property
    def is_high_score(self):
        '''
        Returns whether or not the player achieved a high score
        '''
        all_attempts = Attempt.objects.all()
        if len(all_attempts) > 9:
            return self.score and self.score >= all_attempts[9].score
        return self.score > 0

    def append_poke_id(self):
        '''
        Appends a new pokemon id to the list of guessed pokemon ids
        '''
        poke_list = self.guessed_id_list
        poke_list.append(self.last_poke_id)
        self.guessed_pokes = "[%s]" % ', '.join(str(x) for x in poke_list)
        self.save()

    def increment_score(self):
        self.score += 1
        self.save()

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
