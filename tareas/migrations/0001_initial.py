# Generated by Django 4.2.7 on 2023-11-15 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grupos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tarea', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha_vencimiento', models.DateField()),
                ('id_grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupos.grupos')),
            ],
        ),
    ]