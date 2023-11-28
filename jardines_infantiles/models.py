from django.db import models

class JardinesInfantiles(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.TextField()
    contacto = models.CharField(max_length=255)
    detalles_ubicacion = models.TextField()




# Create your models here.
