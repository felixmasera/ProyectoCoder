from django.urls import path

from AppCoder import *
from .views import *

urlpatterns = [
    path('', inicio),
    path('cursos', cursos),
    path('profesores', profesores),
    path('estudiantes', estudiantes),
    path('entregables', entregables),
]