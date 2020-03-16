from django.db import models

# Create your models here.

class Jogo(models.Model):

    nome = models.CharField(max_length=30, unique=True)
    plataforma = models.CharField(max_length=50)
    genero = models.CharField(max_length=20)

    def __str__(self):
        return self.name