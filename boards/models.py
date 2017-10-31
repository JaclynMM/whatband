from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    artist_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, unique=True)
    last_name = models.CharField(max_length=100, unique=True)
    hometown = models.CharField(max_length=150)
    twitter_id = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Band(models.Model):
    band_id = models.CharField(max_length=100)
    band_name = models.CharField(max_length=150, unique=True)
    genre_id = models.CharField(max_length=150)
    year_span = models.IntegerField()
    hometown = models.CharField(max_length=150)
    website = models.CharField(max_length=150)
    twitter_id = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Album(models.Model):
    album_id = models.CharField(max_length=100)
    band_id = models.CharField(max_length=100)
    name = models.CharField(max_length=150, unique=True)
    create_date= models.IntegerField()

    def __str__(self):
        return self.name
