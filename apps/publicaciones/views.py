from django.shortcuts import render
from django.views.generic import CreateView
#from django.urls import reverse_lazy

from .models import Publicacion
from .forms import Formulario_Publicacion


# Create your views here.

class Crear_publicacion(CreateView):
	model = Publicacion
	template_name = 'publicaciones/crear_publicacion.html'
	form_class = Formulario_Publicacion
	#success_url = reverse_lazy('publicaciones:home_publicaciones')