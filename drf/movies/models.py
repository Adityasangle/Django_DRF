from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre
# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    imdb = models.DecimalField(max_digits=4,decimal_places=2)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    
    

