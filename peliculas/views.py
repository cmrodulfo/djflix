from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render
from datetime import datetime
from django.template import Template

# Create your views here.

def peliculas(request):
    #return HttpResponse("<h1> Todas las peliculas </h1>" )
    #Contexto: el o  los datos que le damos a la plantilla para que se cargue
    context = {
        'nombre_pelicula': 'Gladiador',
    }
    
    return render(request, "peliculas.html", context)


def detalle_pelicula(request, nombre_pelicula):
    return HttpResponse(
        f'<h1 style="color: purple"> Estas por ver: {nombre_pelicula} </h1>')