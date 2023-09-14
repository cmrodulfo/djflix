from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render
from datetime import datetime


# Create your views here.

def peliculas(request):
    #return HttpResponse("<h1> Todas las peliculas </h1>" )
    return render(request, "pelicula_single.html", {"hoy":datetime.today()})


def base_pelicula(request):
    return HttpResponse(f'<h1 style="color: purple"> Template base para vista de pelicula single</h1>')