# Generated by Django 3.2 on 2023-12-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.IntegerField()),
                ('contenido', models.TextField()),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('fechaEdicion', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('meGusta', models.IntegerField()),
                ('noMeGusta', models.IntegerField()),
            ],
        ),
    ]
