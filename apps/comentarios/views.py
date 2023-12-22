from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Comentario
from .forms import FormularioEditar
from apps.publicaciones.models import Publicacion

#CONTROLA SI EL USUARIO ESTA LOGEADO EN UNA VISTA BASADA EN CLASES
from django.contrib.auth.mixins import LoginRequiredMixin
#CONTROLA SI EL USUARIO ESTA LOGEADO EN UNA VISTA BASADA EN FUNCIONEs
from django.contrib.auth.decorators import login_required

#CONTROLA QUE EL USUARIO SEA STAFF VISTA BASADA EN FUNCION
from django.contrib.admin.views.decorators import staff_member_required
#CONTROLA QUE EL USUARIO SEA STAFF PARA VISTA BASADA EN CLASE
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

@login_required
def crear(request, pk):
    contenido = request.POST.get('comentario', None)
    publicacion = Publicacion.objects.get(pk=pk)
    usuario = request.user 
    Comentario.objects.create(contenido=contenido, usuario=usuario, publicacion=publicacion)
    return HttpResponseRedirect(reverse_lazy('publicaciones:mostrar', kwargs={'pk':pk}))

class editar(LoginRequiredMixin,UpdateView):
    model = Comentario
    form_class = FormularioEditar
    template_name = 'comentarios/editar.html'
    def get_success_url(self):
        return reverse_lazy('publicaciones:mostrar', kwargs={'pk': self.object.publicacion.pk})
    
class eliminar(LoginRequiredMixin,DeleteView):
    model = Comentario
    def get_success_url(self):
        return reverse_lazy('publicaciones:mostrar', kwargs={'pk': self.object.publicacion.pk})