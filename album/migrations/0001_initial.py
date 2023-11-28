# Generated by Django 4.2.7 on 2023-11-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.CharField(max_length=255)),
                ('nombre_album', models.CharField(max_length=255)),
                ('fotos', models.ImageField(blank=True, null=True, upload_to='album_fotos/')),
            ],
        ),
    ]
