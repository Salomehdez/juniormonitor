from django.db import models
from grupos.models import Grupos

class Actividades(models.Model):
    nombre_act = models.CharField(max_length=255)
    descripcion = models.TextField()
    id_grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
