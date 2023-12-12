from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Comentario
from .forms import FormularioComentar, FormularioEditar

# Create your views here.

class Mostrar(ListView):
    model = Comentario
    template_name = 'comentarios/mostrar.html'
    context_object_name = 'comentario'

class Comentar(CreateView):
    model = Comentario
    template_name = 'comentarios/comentar.html'
    form_class = FormularioComentar
    success_url = reverse_lazy('publicaciones/publicacion.html')
    

class Editar(UpdateView):
    model = Comentario
    template_name = 'comentarios/editarComentario.html'
    form_class = FormularioEditar
    success_url = reverse_lazy('publicaciones/publicacion.html')
