from django.urls import path, include
from . import views

app_name = 'publicaciones'

urlpatterns = [
<<<<<<< HEAD
    path('crear/', views.Crear_publicacion.as_view(), name ='crear_publicacion'),
 ]
=======
    # READ DEL CRUD (TODAS LAS PUBLICACIONES)
    # 127.0.0.1:8000/publicaciones/
    path('', views.home.as_view(), name='homePublicaciones'),

    # READ DEL CRUD (UNA PUBLICACION ESPECIFICA)
    # 127.0.0.1:8000/publicaciones/1
    path('<int:pk>/', views.mostrarPublicacion, name='unaPublicacion'),
    
    # CREATE DEL CRUD.(CREAR UNA PUBLICACION)
    # 127.0.0.1:8000/publicaciones/crear
    path('crear/', views.publicar.as_view(), name='crearPublicacion'),

    # UPDATE DEL CRUD (EDITAR UNA PUBLICACION ESPECIFICA)
    # 127.0.0.1:8000/publicaciones/editar/1
    path('editar/<int:pk>', views.editarPublicacion.as_view(), name='editarPublicacion'),

    # DELETE DEL CRUD (ELIMINAR UNA PUBLICACION ESPECIFICA)
    # 127.0.0.1:8000/publicaciones/eliminar/1
    path('eliminar/<int:pk>', views.borrarPublicacion.as_view(), name='eliminarPublicacion'),
]
>>>>>>> 95a0110dfc28b7ab876d62170cf89f7b145315a5
