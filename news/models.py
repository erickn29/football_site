from django.db import models
from django.urls import reverse
from random import randint


class News(models.Model):
    club = models.CharField(max_length=299, default='*')
    title = models.CharField(max_length=160)
    content = models.TextField(null=False)
    date = models.DateTimeField(auto_now=True, null=True)
    url = models.CharField(max_length=80, default=f'{randint(1,99)}{randint(1,99)}{randint(1,99)}')


    def get_url(self):
        return reverse('article', args=[self.url])


    def __str__(self):
        return f'{self.title}'


class Club(models.Model):
    name = models.CharField(max_length=160, default='*')
    coach = models.CharField(max_length=160, default='*')
    players = models.TextField(default='*')
    logo = models.TextField(default='*')


    def __str__(self):
        return f'{self.name}'


class League_tables(models.Model):
    country = models.CharField(max_length=160, default='*')
    rank = models.IntegerField(default=0)
    name = models.CharField(max_length=160, default='*')
    played = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    draw = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    goalsDiff = models.CharField(max_length=160, default='*')
    points = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class Club_players_stats(models.Model):
    club = models.CharField(max_length=160, default='*')
    name = models.CharField(max_length=160, default='*')
    age = models.CharField(max_length=160, default='*')
    position = models.CharField(max_length=160, default='*')
    appearences = models.CharField(max_length=160, default='*')
    total = models.CharField(max_length=160, default='*')
    assists = models.CharField(null=True, max_length=160, default='*')
    rating = models.FloatField(default=6.0)

    def __str__(self):
        return f'{self.name}'
