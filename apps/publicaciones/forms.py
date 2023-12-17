from django import forms
from .models import Publicacion

class FormularioPublicar(forms.ModelForm):

    class Meta:

        model = Publicacion
        fields = ['titulo','contenido','imagen','categoria']

class FormularioEditar(forms.ModelForm):

    class Meta:

        model = Publicacion
        fields = ['titulo','contenido','imagen','categoria']
