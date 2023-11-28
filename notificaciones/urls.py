# notificaciones/urls.py
from django.urls import path
from .views import NotificacionesListCreateView

urlpatterns = [
    path('notificaciones/', NotificacionesListCreateView.as_view(), name='notificaciones-list-create'),
    # Añade más rutas según sea necesario
]
