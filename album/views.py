# views.py
from rest_framework import generics
from .models import Album
from .serializers import AlbumSerializer

class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
