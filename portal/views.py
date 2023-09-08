from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
#from django import reverse
#from django.shortcuts import render


# Create your views here.
def index(request):
    respuesta = HttpResponse("<h1>Bienvenido a DjFlix</h1>")
    return respuesta


def peliculas(request, singlemovie):
    return HttpResponse("<h1> Todas las peliculas desde el </h1> {singlemovie}" )

def contacto(request):
    return HttpResponse("<h1> Contacto</h1>")