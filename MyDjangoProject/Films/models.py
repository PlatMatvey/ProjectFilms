from django.db import models

# Create your models here.
class Titles(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    data = models.DateField()
    limit = models.IntegerField()
    img = models.ImageField()
    description = models.CharField(max_length=1000)
    country = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    budget = models.IntegerField()
    director = models.CharField(max_length=100)
    hls_video = models.CharField(max_length=255)

class Comments(models.Model):
    text = models.TextField()
    username = models.CharField(max_length=52)
    day = models.DateField()