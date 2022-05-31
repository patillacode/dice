from django.core.validators import MinValueValidator
from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Score(models.Model):
    player = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='scores')
    points = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.player.name} - {self.points}'


class Game(models.Model):
    players = models.ManyToManyField(Player, related_name='games')
    scores = models.ManyToManyField(Score, related_name='game')
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    @property
    def name(self):
        return f'Game {self.id}'

    def __str__(self):
        return self.name

    def calculate_duration(self):
        if not self.finished_at:
            return None, None

        delta = self.finished_at - self.started_at

        minutes = delta.total_seconds() / 60
        hours = delta.total_seconds() / 60 / 60

        value, unit = delta.total_seconds(), 'seconds'

        if minutes > 60:
            value, unit = round(hours, 2), 'hours'

        elif delta.total_seconds() > 60:
            value, unit = round(minutes, 2), 'minutes'

        return value, unit

    @property
    def duration(self):
        value, unit = self.calculate_duration()
        return f'{value} {unit}'
