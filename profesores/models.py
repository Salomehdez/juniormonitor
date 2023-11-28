from django.db import models
from jardines_infantiles.models import JardinesInfantiles
from grupos.models import Grupos

class Profesores(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    celular = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=255)
    id_jardin_infantil = models.ForeignKey(JardinesInfantiles, on_delete=models.CASCADE)
    id_grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)
# Create your models here.
