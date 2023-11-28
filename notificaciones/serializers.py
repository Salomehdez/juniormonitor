# notificaciones/serializers.py
from rest_framework import serializers
from .models import Notificaciones

class NotificacionesSerializer(serializers.ModelSerializer):
    descripcion_tarea = serializers.CharField(source='obtener_descripcion_tarea', read_only=True)
    descripcion_actividad = serializers.CharField(source='obtener_descripcion_actividad', read_only=True)
    nombre_grupo = serializers.CharField(source='obtener_nombre_grupo', read_only=True)

    class Meta:
        model = Notificaciones
        fields = ['id', 'mensaje', 'descripcion_tarea', 'descripcion_actividad', 'nombre_grupo']
