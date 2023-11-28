from django.urls import path
from .views import InfantesListCreateView

urlpatterns = [
    path('infantes/', InfantesListCreateView.as_view(), name='infantes-list-create'),
]
