from django.db import models

class Ingrediente(models.Model):
    nombre      = models.TextField()
    descripcion = models.TextField()

