from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render
from datetime import datetime


# Create your views here.

def peliculas(request):
    #return HttpResponse("<h1> Todas las peliculas </h1>" )
    return render(request, "base_peliculas.html", {"hoy":datetime.today()})


def pelicula_single(request):
    return HttpResponse(f'<h1 style="color: purple"> Template base para vista de pelicula individual</h1>')