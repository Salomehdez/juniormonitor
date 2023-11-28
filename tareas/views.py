# tareas/views.py
from rest_framework import generics
from .models import Tareas
from .serializers import TareasSerializer

class TareasListCreateView(generics.ListCreateAPIView):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializer

    def perform_create(self, serializer):
        serializer.save()
