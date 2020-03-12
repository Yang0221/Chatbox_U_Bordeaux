from django.db import models


class Salle(models.Model):
    Nom = models.CharField(max_length = 255)
    Activite = models.Charfield(max_lenght = 255)
    NombreSalles = models.IntegerField
