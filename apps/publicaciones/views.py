from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Publicacion,Categoria
from .forms import FormularioPublicar, FormularioEditar

from apps.comentarios.models import Comentario

# Create your views here.

def home(request):
    categoria = request.GET.get('categoria',None)
    orden = request.GET.get('orden',None)
    publicaciones = Publicacion.objects.all()
    categorias = Categoria.objects.all()

    if orden == 'a':
        publicaciones = publicaciones.order_by('titulo')
    elif orden == 'z':
        publicaciones = publicaciones.order_by('-titulo')
    elif orden == 'nuevo':
        publicaciones = publicaciones.order_by('fechaCreacion')
    elif orden == 'antiguo':
        publicaciones = publicaciones.order_by('-fechaCreacion')
    
    if categoria != None:
        publicaciones = publicaciones.filter(categoria = categoria)
    
    contexto = {'publicaciones': publicaciones,'categorias':categorias}
    
    return render(request, 'publicaciones/home.html', contexto)

def mostrar(request, pk):
    publicacion = Publicacion.objects.get(pk = pk)
    contexto = {}
    contexto['publicacion'] = publicacion

    comentario = Comentario.objects.filter(publicacion = publicacion)
    contexto['comentarios'] = comentario
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

