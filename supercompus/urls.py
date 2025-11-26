from django.urls import path
from . import views

urlpatterns = [
    # Ruta de la página principal
    # Ejemplo: http://127.0.0.1:8000/
    path('', views.lista_computadoras, name = 'lista_computadoras'),

    # Ruta para agregar
    # Ejemplo: http://127.0.0.1:8000/agregar/
    path('agregar/', views.agregar_computadora, name = 'agregar_computadora'),

    # Ruta para editar
    # Ejemplo: http://127.0.0.1:8000/editar/1/
    path('editar/<int:id>/', views.editar_computadora, name = 'editar_computadora'),

    # Ruta para borrar
    # Ejemplo: http://127.0.0.1:8000/borrar/1/
    path('borrar/<int:id>/', views.borrar_computadora, name = 'borrar_computadora'),
]