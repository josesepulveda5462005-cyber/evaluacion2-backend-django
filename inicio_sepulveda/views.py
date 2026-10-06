from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio_sepulveda/inicio.html')

def ciberseguridad(request):
    return render(request, 'inicio_sepulveda/ciberseguridad.html')

def proyectos(request):
    return render(request, 'inicio_sepulveda/proyectos.html')
