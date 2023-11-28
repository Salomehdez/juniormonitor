from django.urls import path
from .views import JardinesInfantilesListCreateView

urlpatterns = [
    path('jardines/', JardinesInfantilesListCreateView.as_view(), name='jardines-list-create'),
    # Puedes agregar más rutas aquí según sea necesario
]
