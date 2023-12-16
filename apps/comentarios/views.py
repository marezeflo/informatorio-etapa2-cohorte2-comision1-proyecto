from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Comentario
from .forms import FormularioEditar
from apps.publicaciones.models import Publicacion

# Create your views here.

def crearComentario(request, pk):
    contenido = request.POST.get('comentario', None)
    publicacion = Publicacion.objects.get(pk=pk)
    usuario = request.user 
    Comentario.objects.create(contenido=contenido, usuario=usuario, publicacion=publicacion)
    return HttpResponseRedirect(reverse_lazy('publicaciones:unaPublicacion', kwargs={'pk':pk}))

class editarComentario(UpdateView):
    model = Comentario
    form_class = FormularioEditar
    template_name = 'comentarios/editar.html'
    def get_success_url(self):
        return reverse_lazy('publicaciones:unaPublicacion', kwargs={'pk': self.object.pub.pk})
    
class eliminarComentario(DeleteView):
    model = Comentario
    def get_success_url(self):
        return reverse_lazy('publicaciones:unaPublicacion', kwargs={'pk': self.object.pub.pk})