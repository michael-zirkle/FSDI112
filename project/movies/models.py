from django.db import models

"""
Possible data types on models:
char (string)
int (int)
Float(decimal point numbers)
Boolean (true/false)
"""
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length = 255)

class Movie(models.Model):
    class Meta:
        verbose_name_plural = "movies"
    title = models.CharField(max_length = 255)
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Serie(models.Model):
    class Meta:
        verbose_name_plural = "series"

    title = models.CharField(max_length = 255)
    seasons = models.IntegerField()
    episodes = models.IntegerField()
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.CharField(max_length=255)

