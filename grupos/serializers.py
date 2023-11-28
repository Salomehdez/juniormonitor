from rest_framework import serializers
from .models import Grupos

class GruposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupos
        fields = ['id', 'nombre', 'cantidad', 'id_jardin_infantil']
