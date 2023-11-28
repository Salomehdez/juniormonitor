
# models.py
from django.db import models

class Album(models.Model):
    grupo = models.CharField(max_length=255)
    nombre_album = models.CharField(max_length=255)
    fotos = models.ImageField(upload_to='album_fotos/', blank=True, null=True)

    def _str_(self):
        return f"{self.grupo} - {self.nombre_album}"
# Create your models here.
