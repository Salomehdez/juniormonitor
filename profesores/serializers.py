# En profesores/serializers.py
from rest_framework import serializers
from .models import Profesores
from jardines_infantiles.serializers import JardinesInfantilesSerializer
from grupos.serializers import GruposSerializer

class ProfesoresSerializer(serializers.ModelSerializer):
    id_jardin_infantil = JardinesInfantilesSerializer()  # Serializador para el campo de relación
    id_grupo = GruposSerializer()  # Serializador para el campo de relación

    class Meta:
        model = Profesores
        fields = ['id', 'nombre', 'email', 'celular', 'contraseña', 'id_jardin_infantil', 'id_grupo']
