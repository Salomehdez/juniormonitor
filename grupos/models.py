from django.db import models
from jardines_infantiles.models import JardinesInfantiles

class Grupos(models.Model):
    nombre = models.TextField()
    cantidad = models.IntegerField()
    id_jardin_infantil = models.ForeignKey(JardinesInfantiles, on_delete=models.CASCADE)
# Create your models here.
