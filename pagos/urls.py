# pagos/urls.py
from django.urls import path
from .views import PagosListCreateView

urlpatterns = [
    path('pagos/', PagosListCreateView.as_view(), name='pagos-list-create'),
    # Añade más rutas según sea necesario
]
