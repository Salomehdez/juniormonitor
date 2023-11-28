# En actividades/urls.py
from django.urls import path
from .views import ActividadesListCreateView

urlpatterns = [
    path('actividades/', ActividadesListCreateView.as_view(), name='actividades-list-create'),
    # Puedes agregar más rutas según sea necesario
]
