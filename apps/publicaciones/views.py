from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Publicacion
from .forms import FormularioPublicar, FormularioEditar

# Create your views here.

class home(ListView):
    model = Publicacion
    template_name = 'publicaciones/home.html'
    context_object_name = 'publicacion'

class publicacion(ListView):
    model = Publicacion
    template_name = 'publicaciones/publicacion.html'
    context_object_name = 'publicacion'

class publicar(CreateView):
    model = Publicacion
    template_name = 'publicaciones/publicar.html'
    form_class = FormularioPublicar
    succes_url = reverse_lazy('publicaciones:home')

class editarPublicacion(UpdateView):
    model = Publicacion
    template_name = 'publicaciones/editarPublicacion.html'
    form_class = FormularioEditar

class borrarPublicacion(DeleteView):
    model = Publicacion
    sucess_url = reverse_lazy('publicaciones:home')

