from django.db import models
from django.contrib.auth.models import User
from apps.publicaciones.models import Publicacion

# Create your models here.

class Comentario(models.Model):
    usuario = models.ForeignKey(User,on_delete = models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete = models.CASCADE)
    contenido = models.TextField()
    fechaCreacion = models.DateTimeField(
        'Creado',
        auto_now_add = True
    )
    fechaEdicion = models.DateTimeField(
        'Modificado',
        auto_now = True
    )
    
    def __str__(self):
        return self.contenido