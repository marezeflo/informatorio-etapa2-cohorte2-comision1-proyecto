from django.shortcuts import render
from apps.publicaciones.models import Publicacion

def home(request):

    ultimasTresPublicaciones = Publicacion.objects.order_by('-fechaCreacion')[:3]
    contexto = {'ultimasTresPublicaciones': ultimasTresPublicaciones }
    return render(request, 'home.html', contexto)

def contacto(request):
    return render(request, 'contacto.html')

def sobreNosotros(request):
    return render(request, 'sobrenosotros.html')