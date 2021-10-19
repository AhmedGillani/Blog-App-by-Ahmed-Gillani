from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/')
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    author = models.CharField(max_length=200)


class Feed(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    feed = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
