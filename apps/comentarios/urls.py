from django.urls import path, include
from . import views

app_name = 'comentarios'

urlpatterns = [
    path('crear/<int:pk>', views.crearComentario, name = 'crearComentario'),
    path('editar/<int:pk>', views.editarComentario.as_view(), name = 'editarComentario'),
    path('eliminar/<int:pk>', views.eliminarComentario.as_view(), name = 'eliminarComentario')
]