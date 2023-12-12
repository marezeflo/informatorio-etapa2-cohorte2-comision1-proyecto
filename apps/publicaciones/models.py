from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(max_length=50)

    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):

    usuario = models.ForeignKey(User, on_delete = models.CASCADE)

    titulo = models.CharField(max_length=250)

    imagen = models.ImageField(upload_to = 'publicaciones')

    contenido = models.TextField()

    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)

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

    def __str__(self):
        return self.titulo