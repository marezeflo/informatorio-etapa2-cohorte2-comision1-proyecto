from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):

    usuario = models.ForeignKey(User,on_delete = models.CASCADE)

    contenido = models.TextField()

    fechaCreacion = models.DateTimeField(
        'Creado',
        auto_now_add = True
    )

    fechaEdicion = models.DateTimeField(
        'Modificado',
        auto_now = True
    )

    meGusta = models.IntegerField(default = 0)

    noMeGusta = models.IntegerField(default = 0)