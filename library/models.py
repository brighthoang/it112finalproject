from django.db import models
from django.forms import CharField, DateField
from django.contrib.auth.models import User

class Books(models.Model):
    book_title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    ISBN=models.CharField(max_length=40)
    publishyear=models.CharField(max_length=4)

    def __str__(self):
        return self.book_title

    class Meta:
        db_table='books'


class Movies(models.Model):
    movie_title=models.CharField(max_length=255)
    director=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    releaseyear=models.CharField(max_length=4)

    def __str__(self):
        return self.movie_title

    class Meta:
        db_table='movies'


class Music(models.Model):
    song_title=models.CharField(max_length=255)
    artist=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    releaseyear=models.CharField(max_length=4)

    def __str__(self):
        return self.song_title

    class Meta:
        db_table='music'

