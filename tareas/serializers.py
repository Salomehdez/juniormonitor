# tareas/serializers.py
from rest_framework import serializers
from .models import Tareas
from grupos.models import Grupos

class TareasSerializer(serializers.ModelSerializer):
    id_grupo = serializers.PrimaryKeyRelatedField(queryset=Grupos.objects.all())

    class Meta:
        model = Tareas
        fields = ['id', 'nombre_tarea', 'descripcion', 'id_grupo']
