from django.db import models

# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(max_length=50)

    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):

    # usuario = models.ForeignKey()

    titulo = models.CharField(max_length=250)

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