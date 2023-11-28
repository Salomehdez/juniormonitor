# En tareas/urls.py
from django.urls import path
from .views import TareasListCreateView

urlpatterns = [
    path('tareas/', TareasListCreateView.as_view(), name='tareas-list-create'),
    # Puedes agregar más rutas aquí según sea necesario
]
