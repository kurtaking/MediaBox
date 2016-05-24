from django.db import models

class User(models.Model):
    user_id = models.IntegerField(default=0)
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.CharField(max_length=25)

class Vinyl(models.Model):
    artist = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=20)
    label = models.CharField(max_length=20)
    format_size = models.IntegerField(default=0)
    isbn = models.CharField(max_length=25)

