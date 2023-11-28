from django.shortcuts import render
# pagos/views.py
from rest_framework import generics
from .models import Pagos
from .serializers import PagosSerializer

class PagosListCreateView(generics.ListCreateAPIView):
    queryset = Pagos.objects.all()
    serializer_class = PagosSerializer
# Create your views here.
