from django.http import HttpResponse


# Create your views here.
def index(request):
    respuesta = HttpResponse("<h1>Bienvenido a DjFlix</h1>")
    return respuesta


def peliculas(request):
    return HttpResponse("<h1> Todas las peliculas desde el </h1>")

def contacto(request):
    return HttpResponse("<h1> Contacto</h1>")