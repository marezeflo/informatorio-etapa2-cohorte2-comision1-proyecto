from django import forms
from .models import Comentario



class FormularioEditar(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('contenido',)