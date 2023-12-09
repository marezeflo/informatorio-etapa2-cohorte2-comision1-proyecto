from django.urls import path, include
from . import views

app_name = 'publicaciones'

urlpatterns = [
    path('crear/', views.Crear_publicacion.as_view(), name ='crear_publicacion'),
 ]