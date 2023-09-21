from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.urls import reverse
from django.shortcuts import render
#from django.template import loader
from datetime import datetime
from django.template import Template


# Create your views here.
def index(request):
    
   # indexTemplate = loader.get_template("index.html")
   # contexto = {"ahora": datetime.now}
   # indexTemplate_renderizado = indexTemplate.render(contexto, request)
   # respuesta = HttpResponse(indexTemplate_renderizado)
   return render(request, "index.html", {"ahora":datetime.now()})


def contacto(request):
    return render(request, "contact_form.html")
 
 
def base(request):
    return render(request, "base.html")


def precios(request):
    return render(request, "precios.html")



