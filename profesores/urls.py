# En profesores/urls.py
from django.urls import path
from .views import ProfesoresListCreateView

urlpatterns = [
    path('profesores/', ProfesoresListCreateView.as_view(), name='profesores-list-create'),
    # Puedes agregar más rutas según sea necesario
]
