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
        'peliculas': {
            '0': {'nombre':'Gladiador',
                'fecha': datetime.now(),
                'categoria': 'Aventura/Acción',
                'imagen': 'gladiador.jpg'
                },
            '1': {'nombre': 'The Matrix',
                'fecha': datetime.now(),
                'categoria': 'Ciencia Ficción',
                'imagen': 'matrix.jpg'
            },
        },
        'es_suscriptor': True, 
        }

    return render(request, "peliculas.html", context)


def detalle_pelicula(request, nombre_pelicula):
    return HttpResponse(
        f'<h1 style="color: purple"> Detalle de pelicula seleccionada, Estas por ver: {nombre_pelicula} </h1>')
    
    
def archivo(request, year):
    if year == 2028:
        url = reverse("index")
        return HttpResponseRedirect(url)
    elif year == 2027:
        return HttpResponseServerError("<h1> Error de servidor </h1>")
    
    return HttpResponse(f'<h1>Peliculas de archivo del anio: {year}</h1>')

    return response