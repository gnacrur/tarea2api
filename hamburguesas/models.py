from django.db import models
from ingredientes.models import Ingrediente

# Create your models here.
class Hamburguesa(models.Model):
    nombre      = models.TextField()
    precio      = models.IntegerField()
    descripcion = models.TextField()
    imagen      = models.TextField()
    ingredientes= models.ManyToManyField(Ingrediente, blank = True)