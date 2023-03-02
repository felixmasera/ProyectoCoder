from django.urls import path

from AppCoder import *
from .views import *

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('cursos/', cursos,name='cursos'),
    path('profesores/', profesores, name= 'profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('entregables/', entregables,name='entregables'),
    #path('curso-formulario/',curso_formulario, name='curso-formulario'),
    path('profesor-formulario/', profesor_formulario,name='profesor-formulario' ),
    #path('busqueda-camada/',buscar_camada, name='busqueda-camada'),
    path('buscar/', buscar,name='buscar'),
    path('leer-profesores/',leer_profesores, name = 'leer-profesores'),
    path('eliminar-profesor/<profesor_id>',eliminar_profesor, name='eliminar-profesor')
]