from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render
#from django.template import loader
from datetime import datetime


# Create your views here.
def index(request):
    
   # indexTemplate = loader.get_template("index.html")
   # contexto = {"ahora": datetime.now}
   # indexTemplate_renderizado = indexTemplate.render(contexto, request)
   # respuesta = HttpResponse(indexTemplate_renderizado)
   return render(request, "index.html", {"ahora":datetime.now()})


def peliculas(request):
    #return HttpResponse("<h1> Todas las peliculas </h1>"  )
    return HttpResponse("<h1> Peliculas </h1>")


def archivo(request, year):
    if year == 2028:
        url = reverse("index")
        return HttpResponseRedirect(url)
    elif year == 2027:
        return HttpResponseServerError("<h1> Error de servidor </h1>")
    
    return HttpResponse(f'<h1>Peliculas de archivo del anio: {year}</h1>')

    return response


def contacto(request):
    return HttpResponse("<h1> Contacto</h1>")

def base_pelicula(request):
    return HttpResponse(f'<h1> Template base para vista de pelicula</h1>')