from django.db import models


class Attempt(models.Model):
    '''
    Represents an attempt to play the game
    '''
    score = models.IntegerField(default=0)
    player_name = models.CharField(max_length=25)

    def __str__(self):
        return "Name: %s, Score: %s" % (self.player_name, self.score)

    class Meta:
        # Sort attempt objects from highest to lowest score
        ordering = ['-score']
