from django.shortcuts import render
from rest_framework import generics
from .models import Grupos
from .serializers import GruposSerializer

class GruposListCreateView(generics.ListCreateAPIView):
    queryset = Grupos.objects.all()
    serializer_class = GruposSerializer
# Create your views here.
