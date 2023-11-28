from django.shortcuts import render
# notificaciones_padres/views.py
from rest_framework import generics
from .models import Notificaciones_Padres
from .serializers import NotificacionesPadresSerializer

class NotificacionesPadresListCreateView(generics.ListCreateAPIView):
    queryset = Notificaciones_Padres.objects.all()
    serializer_class = NotificacionesPadresSerializer
# Create your views here.
