from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm

# Create your views here.

class Registro(CreateView):
	# formulario de registro del usuario
	form_class = RegistroForm
	success_url = reverse_lazy('login')
	template_name = 'usuarios/registro.html'
