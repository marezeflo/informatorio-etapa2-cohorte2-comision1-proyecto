from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Publicacion,Categoria
from .forms import FormularioPublicar, FormularioEditar

from apps.comentarios.models import Comentario

#CONTROLA SI EL USUARIO ESTA LOGEADO EN UNA VISTA BASADA EN CLASES
from django.contrib.auth.mixins import LoginRequiredMixin
#CONTROLA SI EL USUARIO ESTA LOGEADO EN UNA VISTA BASADA EN FUNCIONEs
from django.contrib.auth.decorators import login_required

#CONTROLA QUE EL USUARIO SEA STAFF VISTA BASADA EN FUNCION
from django.contrib.admin.views.decorators import staff_member_required
#CONTROLA QUE EL USUARIO SEA STAFF PARA VISTA BASADA EN CLASE
from django.contrib.auth.mixins import UserPassesTestMixin

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
        publicaciones = publicaciones.order_by('-fechaCreacion')
    elif orden == 'antiguo':
        publicaciones = publicaciones.order_by('fechaCreacion')
    
    if categoria != None:
        publicaciones = publicaciones.filter(categoria = categoria)
    
    contexto = {'publicaciones': publicaciones,'categorias':categorias}
    
    return render(request, 'publicaciones/home.html', contexto)

def mostrar(request, pk):
    publicacion = Publicacion.objects.get(pk = pk)
    contexto = {}
    contexto['publicacion'] = publicacion

    comentario = Comentario.objects.filter(publicacion = publicacion)
    contexto['comentarios'] = comentario.order_by('-fechaCreacion')
    return render(request, 'publicaciones/mostrar.html', contexto)

@login_required
def crear(request):
    categorias = Categoria.objects.all()

    if request.method == 'POST':
        formulario = FormularioPublicar(request.POST, request.FILES)
        if formulario.is_valid():
            titulo = formulario.cleaned_data['titulo']
            imagen = formulario.cleaned_data['imagen']
            contenido = formulario.cleaned_data['contenido']
            categoria = formulario.cleaned_data['categoria']
            Publicacion.objects.create(
                usuario=request.user,
                titulo=titulo,
                imagen=imagen,
                contenido=contenido,
                categoria=categoria
            )
            return HttpResponseRedirect(reverse_lazy('publicaciones:home'))
    else:
        formulario = FormularioPublicar()

    contexto = {'categorias': categorias, 'formulario': formulario}
    return render(request, 'publicaciones/crear.html', contexto)

class editar(LoginRequiredMixin,UpdateView):
    model = Publicacion
    template_name = 'publicaciones/editar.html'
    form_class = FormularioEditar
    success_url = reverse_lazy('publicaciones:home')

class eliminar(LoginRequiredMixin,DeleteView):
    model = Publicacion
    success_url = reverse_lazy('publicaciones:home')

