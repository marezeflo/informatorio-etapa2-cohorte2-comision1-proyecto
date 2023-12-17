from django import forms
from .models import Publicacion

<<<<<<< HEAD

class Formulario_Publicacion(forms.ModelForm):

	class Meta:
		model = Publicacion
		fields = ['titulo','contenido','categoria']
=======
class FormularioPublicar(forms.ModelForm):

    class Meta:

        model = Publicacion
        fields = ['titulo','contenido','imagen','categoria']

class FormularioEditar(forms.ModelForm):

    class Meta:

        model = Publicacion
        fields = ['titulo','contenido','imagen','categoria']
>>>>>>> 95a0110dfc28b7ab876d62170cf89f7b145315a5
