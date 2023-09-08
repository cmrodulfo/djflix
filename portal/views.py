from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
#from django.shortcuts import render


# Create your views here.
def index(request):
    respuesta = HttpResponse("<h1>Bienvenido a DjFlix</h1>")
    return respuesta


def peliculas(request):
    return HttpResponse("<h1> Todas las peliculas </h1>"  )


def archivo(request, year):
    if year == 2028:
        url = reverse("index")
        return HttpResponseRedirect(url)
    
    return HttpResponse(f'<h1>Peliculas de archivo del anio: {year}</h1>')


def contacto(request):
    return HttpResponse("<h1> Contacto</h1>")