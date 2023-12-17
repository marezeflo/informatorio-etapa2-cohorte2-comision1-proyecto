from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Publicacion
from .forms import FormularioPublicar, FormularioEditar

from apps.comentarios.models import Comentario

# Create your views here.

class home(ListView):
    model = Publicacion
    template_name = 'publicaciones/home.html'
    context_object_name = 'publicaciones'

def mostrar(request, pk):
    publicacion = Publicacion.objects.get(pk = pk)
    contexto = {}
    contexto['publicacion'] = publicacion

    comentario = Comentario.objects.filter(publicacion = publicacion)
    contexto['comentario'] = comentario
    return render(request, 'publicaciones/mostrar.html', contexto)

class crear(CreateView):
    model = Publicacion
    template_name = 'publicaciones/crear.html'
    form_class = FormularioPublicar
    succes_url = reverse_lazy('publicaciones:home')

class editar(UpdateView):
    model = Publicacion
    template_name = 'publicaciones/editar.html'
    form_class = FormularioEditar

class eliminar(DeleteView):
    model = Publicacion
    sucess_url = reverse_lazy('publicaciones:home')

