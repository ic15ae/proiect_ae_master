from django.db import models

class Produse (models.Model):
    titlu = models.CharField(max_length=200)
    descriere = models.TextField()
    pret = models.IntegerField()
    image = models.FilePathField(path="/img")
