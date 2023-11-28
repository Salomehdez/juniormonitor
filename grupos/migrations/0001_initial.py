# Generated by Django 4.2.7 on 2023-11-15 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jardines_infantiles', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('cantidad', models.IntegerField()),
                ('id_jardin_infantil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jardines_infantiles.jardinesinfantiles')),
            ],
        ),
    ]
