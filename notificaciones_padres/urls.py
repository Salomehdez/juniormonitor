# notificaciones_padres/urls.py
from django.urls import path
from .views import NotificacionesPadresListCreateView

urlpatterns = [
    path('notificaciones_padres/', NotificacionesPadresListCreateView.as_view(), name='notificaciones-padres-list-create'),
    # Añade más rutas según sea necesario
]
