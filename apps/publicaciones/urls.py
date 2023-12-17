from django.urls import path, include
from . import views

app_name = 'publicaciones'

urlpatterns = [
    # READ DEL CRUD (TODAS LAS PUBLICACIONES)
    # 127.0.0.1:8000/publicaciones/
    # path('', views.home.as_view(), name='homePublicaciones'),
    path('', views.home.as_view(), name='home'),

    # READ DEL CRUD (UNA PUBLICACION ESPECIFICA)
    # 127.0.0.1:8000/publicaciones/1
    path('<int:pk>/', views.mostrar, name='mostrar'),
    
    # CREATE DEL CRUD.(CREAR UNA PUBLICACION)
    # 127.0.0.1:8000/publicaciones/crear
    path('crear/', views.crear.as_view(), name='crear'),

    # UPDATE DEL CRUD (EDITAR UNA PUBLICACION ESPECIFICA)
    # 127.0.0.1:8000/publicaciones/editar/1
    path('editar/<int:pk>', views.editar.as_view(), name='editar'),

    # DELETE DEL CRUD (ELIMINAR UNA PUBLICACION ESPECIFICA)
    # 127.0.0.1:8000/publicaciones/eliminar/1
    path('eliminar/<int:pk>', views.eliminar.as_view(), name='eliminar'),
]