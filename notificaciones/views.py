from django.shortcuts import render
# notificaciones/views.py
from rest_framework import generics
from .models import Notificaciones
from .serializers import NotificacionesSerializer

class NotificacionesListCreateView(generics.ListCreateAPIView):
    queryset = Notificaciones.objects.all()
    serializer_class = NotificacionesSerializer
# Create your views here.
