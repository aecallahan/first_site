from django.db import models


class Attempt(models.Model):
	'''
	Represents an attempt to play the game
	'''
	score = models.IntegerField(default=0)
