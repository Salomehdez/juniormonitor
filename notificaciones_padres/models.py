from django.db import models
from notificaciones.models import Notificaciones
from padres.models import Padres

class Notificaciones_Padres(models.Model):
    id_notificacion = models.ForeignKey(Notificaciones, on_delete=models.CASCADE)
    id_padre = models.ForeignKey(Padres, on_delete=models.CASCADE)
# Create your models here.
