from django.shortcuts import render
from django.views.generic import ListView
from administracion.models import Pelicula, Actor, Director

# Create your views here.
class PeliculasListView(ListView):
    model = Pelicula
    queryset = Pelicula.objects.all()
    context_object_name = 'peliculas'
    paginate_by = 12
    template_name = 'index.html'



class ActoresListView(ListView):
    model = Actor
    queryset = Actor.objects.all()
    context_object_name = 'actores'
    paginate_by = 12
    template_name = 'actores.html'


class DirectoresListView(ListView):
    model = Director
    queryset = Director.objects.all()
    context_object_name = 'directores'
    paginate_by = 12
    template_name = 'directores.html'

