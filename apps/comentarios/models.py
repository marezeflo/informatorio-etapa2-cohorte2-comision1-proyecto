from django.db import models

# Create your models here.

class Comentario(models.Model):

    usuario = models.IntegerField()

    contenido = models.TextField()

    fechaCreacion = models.DateTimeField(
        'Creado',
        auto_now_add = True
    )

    fechaEdicion = models.DateTimeField(
        'Modificado',
        auto_now = True
    )

    meGusta = models.IntegerField()

    noMeGusta = models.IntegerField()