# juniormonitorDjango/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import home, LoginView, enviar_correo

from django.urls import path
from .views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jardines_infantiles.urls')),  # Ajusta según tus aplicaciones
    path('', home, name='home'),  # Ruta para la URL raíz
    path('api/', include('padres.urls')),
    path('api/', include('grupos.urls')),
    path('api/', include('infantes.urls')),
    path('api/', include('tareas.urls')),
    path('api/', include('actividades.urls')),
    path('api/', include('profesores.urls')),
    path('api/', include('notificaciones.urls')),
    path('api/', include('notificaciones_padres.urls')),
    path('api/', include('pagos.urls')),
    path('enviar-correo/', enviar_correo, name='enviar_correo'),
    path('api/login/', LoginView, name='login'),
    path('api/', include('album.urls')),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
   
 # Resto de tus rutas
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
