# Generated by Django 4.2.7 on 2023-11-27 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0002_remove_actividades_fecha_realizacion'),
        ('tareas', '0002_remove_tareas_fecha_vencimiento'),
        ('notificaciones', '0002_remove_notificaciones_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificaciones',
            name='id_actividades',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='actividades.actividades'),
        ),
        migrations.AlterField(
            model_name='notificaciones',
            name='id_tareas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tareas.tareas'),
        ),
    ]
