from rest_framework import serializers
from .models import JardinesInfantiles

class JardinesInfantilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JardinesInfantiles
        fields = '__all__'
