from django.http import HttpResponse
from django.shortcuts import render

def webproject(request):
    return HttpResponse("Hola")

def index(request):
    return render(request, 'index.html')

def contacto(request):
    return render(request, 'contacto.html')

def descargas(request):
    return render(request, 'descargas.html')

def donaciones(request):
    return render(request, 'donaciones.html')

def legales(request):
    return render(request, 'legales.html')

def quienes_somos(request):
    return render(request, 'quienes_somos.html')

def tutoriales(request):
    return render(request, 'tutoriales.html')

def tutoriales_especiales(request):
    return render(request, 'tutoriales_especiales.html')

def header(request):
    return render(request, 'header.html')

def footer(request):
    return render(request, 'footer.html')

