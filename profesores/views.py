from django.shortcuts import render
# En profesores/views.py
from rest_framework import generics
from .models import Profesores
from .serializers import ProfesoresSerializer

class ProfesoresListCreateView(generics.ListCreateAPIView):
    queryset = Profesores.objects.all()
    serializer_class = ProfesoresSerializer
# Create your views here.
