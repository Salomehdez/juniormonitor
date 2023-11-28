from django.shortcuts import render
from rest_framework import generics
from .models import Infantes
from .serializers import InfantesSerializer

class InfantesListCreateView(generics.ListCreateAPIView):
    queryset = Infantes.objects.all()
    serializer_class = InfantesSerializer
# Create your views here.
