# Generated by Django 4.2.7 on 2023-12-16 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publicaciones', '0004_auto_20231212_0934'),
        ('comentarios', '0004_categoria'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='meGusta',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='noMeGusta',
        ),
        migrations.AddField(
            model_name='comentario',
            name='publicacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='publicaciones.publicacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]