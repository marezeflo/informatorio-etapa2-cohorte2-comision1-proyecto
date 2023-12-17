from django.urls import path, include
from . import views

app_name = 'comentarios'

urlpatterns = [
    path('crear/<int:pk>', views.crear, name = 'crear'),
    path('editar/<int:pk>', views.editar.as_view(), name = 'editar'),
    path('eliminar/<int:pk>', views.eliminar.as_view(), name = 'eliminar')
]