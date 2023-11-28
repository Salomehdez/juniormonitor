from rest_framework import generics
from .models import Actividades
from .serializers import ActividadesSerializer

class ActividadesListCreateView(generics.ListCreateAPIView):
    queryset = Actividades.objects.all()
    serializer_class = ActividadesSerializer

    def perform_create(self, serializer):
        serializer.save()
