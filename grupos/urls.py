from django.urls import path
from .views import GruposListCreateView

urlpatterns = [
    path('grupos/', GruposListCreateView.as_view(), name='grupos-list-create'),
]
