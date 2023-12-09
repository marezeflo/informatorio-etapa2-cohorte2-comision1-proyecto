from django.db import models

# Create your models here.

class Publicacion(models.Model):

    titulo = models.CharField(max_length=250)

    contenido = models.TextField()

    categoria = models.CharField(max_length=15)

    fechaCreacion = models.DateTimeField(
        'Creado',
        auto_now_add = True
    )

    fechaEdicion = models.DateTimeField(
        'Modificado',
        auto_now = True
    )

    def __str__(self):
        return self.titulo