from django.shortcuts import render,redirect
from .forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario
from django.http import HttpResponse

from AppCoder.models import Curso, Profesor,Estudiante
# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def cursos(request):
    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)


        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_curso= Curso(nombre=informacion['curso'], camada=informacion['camada'])
            nuevo_curso.save()
            return redirect('inicio')


    mi_formulario = CursoFormulario()
    return render(request, 'AppCoder/cursos.html',{'cursos': mi_formulario})
    


def profesores(request):
    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST)


        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_profesor= Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            nuevo_profesor.save()
            return redirect('inicio')


    mi_formulario = ProfesorFormulario()
    return render(request, 'AppCoder/profesores.html',{'profesores': mi_formulario})


def estudiantes(request):
    if request.method == 'POST':
        mi_formulario =EstudianteFormulario(request.POST)


        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_e = Estudiante(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])
            nuevo_e.save()
            return redirect('inicio')


    mi_formulario = EstudianteFormulario()
    return render(request, 'AppCoder/estudiantes.html',{'estudiantes': mi_formulario})


def entregables(request):
    return render(request,'AppCoder/entregables.html')


def curso_formulario(request):

    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)


        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_curso= Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            nuevo_curso.save()
            return redirect('inicio')


    mi_formulario = CursoFormulario()
    return render(request, 'AppCoder/curso-formulario.html',{'formulario_curso': mi_formulario})



def profesor_formulario(request):
    if request.method == 'POST':
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'],
                                apellido=informacion['apellido'],
                                email=informacion['email'],            
                                profesion=informacion['profesion'])

            profesor.save()
            return redirect('inicio')
    else:
        mi_formulario = ProfesorFormulario()
        return render(request, 'AppCoder/profesor-formulario.html', {'formulario_profesor': mi_formulario})


def buscar_camada(request):

    return render(request, 'AppCoder/busqueda-camada.html')

def buscar(request):
    
    if request.GET['camada']:
        camada = request.GET['camada']
        resultado = Curso.objects.filter(camada__icontains = camada)
        return render(request, 'AppCoder/inicio.html', {'cursos': resultado, 'camada': camada})

    else: 
        resultado= 'Espacios en blanco'

        return render(request, 'AppCoder/inicio.html', {'resultado': resultado})
   
    