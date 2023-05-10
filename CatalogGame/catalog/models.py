from django.db import models

from CatalogGame import settings


# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length = 100)
    genre = models.ForeignKey('Genres', on_delete = models.PROTECT)
    publisher = models.ForeignKey('Publishers', on_delete = models.PROTECT)
    photo = models.ImageField(upload_to = 'gameimg/%Y/%m/%d')
    describe = models.TextField(blank = True)
    date_publication = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Additions(models.Model):
    name = models.CharField(max_length = 100)
    orig = models.ForeignKey('Games', on_delete = models.PROTECT)
    describe = models.TextField(blank = True)
    photo = models.ImageField(upload_to = 'addimg/%Y/%m/%d')

    def __str__(self):
        return self.name

class Publishers(models.Model):
    name = models.CharField(max_length = 100)
    date_registration = models.DateTimeField(auto_now_add = True)
    number = models.IntegerField()
    site = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

class Genres(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Author(models.Model):
    
