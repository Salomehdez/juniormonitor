from django.db import models
from django.contrib.auth.models import User

class Padres(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # Haciendo el campo 'email' único
    telefono = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=255)
    
    # Otros campos si los tienes
# Create your models here.
