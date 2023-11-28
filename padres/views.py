from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Padres
from .serializers import PadresSerializer

class PadresListCreateView(generics.ListCreateAPIView):
    queryset = Padres.objects.all()
    serializer_class = PadresSerializer
    permission_classes = []
# Create your views here.
