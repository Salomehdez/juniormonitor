from rest_framework import serializers
from .models import Infantes

class InfantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infantes
        fields = ['id', 'nombre', 'edad', 'id_padre', 'id_grupo']
