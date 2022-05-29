# from datetime import datetime

from django.core.validators import MinValueValidator
from django.db import models

from faker import Faker

fake = Faker(['en_US', 'es_ES'])


class Die(models.Model):
    pass


class Player(models.Model):
    name = models.CharField(max_length=32, default=fake.first_name())

    def __str__(self):
        return self.name


class Score(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='scores')
    game = models.ForeignKey('Game', on_delete=models.CASCADE, related_name='scores')
    points = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.player.name} {self.points} ({self.game})'


class Game(models.Model):
    players = models.ManyToManyField(Player, related_name='matches')
    # scores = models.ManyToManyField(Score, related_name='matches')
    start_at = models.DateTimeField(auto_now_add=True)
    finish_at = models.DateTimeField(null=True, blank=True)

    @property
    def name(self):
        return f'Game {self.id}'

    def __str__(self):
        return self.name

    @property
    def duration(self):
        if not self.finish_at:
            return None, None

        delta = self.finish_at - self.start_at

        minutes = delta.total_seconds() / 60
        hours = delta.total_seconds() / 60 / 60

        value, unit = delta.total_seconds(), 'seconds'

        if minutes > 60:
            value, unit = hours, 'hours'

        elif delta.total_seconds() > 60:
            value, unit = minutes, 'minutes'

        return value, unit

    @property
    def duration_unit(self):
        _, unit = self.duration
        return unit

    @property
    def duration_value(self):
        value, _ = self.duration
        return value
