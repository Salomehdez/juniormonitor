# album/admin.py
from django.contrib import admin
from .models import Album

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['grupo', 'nombre_album', 'fotos']
    search_fields = ['grupo', 'nombre_album']
    list_filter = ['grupo', 'nombre_album']
