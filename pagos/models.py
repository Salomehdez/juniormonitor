from django.db import models
from padres.models import Padres
from jardines_infantiles.models import JardinesInfantiles

class Pagos(models.Model):
    monto = models.IntegerField()
    fecha_pago = models.DateField()
    id_padre = models.ForeignKey(Padres, on_delete=models.CASCADE)
    id_jardin_infantil = models.ForeignKey(JardinesInfantiles, on_delete=models.CASCADE)
# Create your models here.
