from rest_framework import serializers
from .models import Padres

class PadresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Padres
        fields = ['id', 'nombre', 'email', 'telefono', 'contraseña']
