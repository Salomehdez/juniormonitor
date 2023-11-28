# notificaciones/models.py
from django.db import models
from tareas.models import Tareas
from actividades.models import Actividades
from grupos.models import Grupos

class Notificaciones(models.Model):
    mensaje = models.TextField()
    id_tareas = models.ForeignKey(Tareas, on_delete=models.SET_NULL, null=True, blank=True)
    id_actividades = models.ForeignKey(Actividades, on_delete=models.SET_NULL, null=True, blank=True)
    id_grupo = models.ForeignKey(Grupos, on_delete=models.CASCADE)

    def obtener_descripcion_tarea(self):
        return self.id_tareas.descripcion if self.id_tareas else None

    def obtener_descripcion_actividad(self):
        return self.id_actividades.descripcion if self.id_actividades else None

    def obtener_nombre_grupo(self):
        return self.id_grupo.nombre if self.id_grupo else None

# Resto del modelo o cualquier otro código adicional que puedas tener
