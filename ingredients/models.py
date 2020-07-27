from django.db import models

# Create your models here.

class Personaje(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pelicula(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    planets = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    producers = models.CharField(max_length=100)
    personajes = models.ManyToManyField(Personaje, related_name='peliculas')

    def __str__(self):
        return self.name

