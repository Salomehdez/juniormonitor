from rest_framework import serializers
from .models import Actividades
from grupos.models import Grupos  # Importa el modelo Grupos

class ActividadesSerializer(serializers.ModelSerializer):
    id_grupo = serializers.PrimaryKeyRelatedField(queryset=Grupos.objects.all())

    class Meta:
        model = Actividades
        fields = ['id', 'nombre_act', 'descripcion', 'id_grupo']
