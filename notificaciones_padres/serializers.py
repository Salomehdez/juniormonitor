# notificaciones_padres/serializers.py
from rest_framework import serializers
from .models import Notificaciones_Padres

class NotificacionesPadresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificaciones_Padres
        fields = '__all__'
