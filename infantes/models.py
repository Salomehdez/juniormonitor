from django.db import models
from padres.models import Padres
from grupos.models import Grupos

class Infantes(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    id_padre = models.ForeignKey(Padres, on_delete=models.CASCADE)
    id_grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
# Create your models here.
