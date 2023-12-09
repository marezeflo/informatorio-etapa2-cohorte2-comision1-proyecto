from django import forms
from .models import Publicacion


class Formulario_Publicacion(forms.ModelForm):

	class Meta:
		model = Publicacion
		fields = ['titulo','contenido','categoria']