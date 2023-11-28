from django.urls import path
from .views import PadresListCreateView
urlpatterns = [
    path('padres/', PadresListCreateView.as_view(), name='padres-list-create'),
]
