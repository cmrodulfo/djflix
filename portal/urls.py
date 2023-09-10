"""
URL configuration for djflix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name = "index"),
    path('portal/', views.index, name = "index"),
    path('peliculas/', views.peliculas, name = "Peliculas"),
    path('archivo/<int:year>', views.archivo, name = "Archivo "),
    path('contacto/', views.contacto, name = "Contacto"),
    path('base_pelicula/', views.base_pelicula, name="Base pelicula single")
]