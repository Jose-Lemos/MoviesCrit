from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from administracion.models import Pelicula, Actor, Director, Crítica

# Create your views here.
#Views Peliculas
class PeliculasListView(ListView):
    model = Pelicula
    queryset = Pelicula.objects.all()
    context_object_name = 'peliculas'
    paginate_by = 12
    template_name = 'index.html'

class PeliculasDetailView(DetailView):
    model = Pelicula
    template_name = 'pelicula-detail.html'

#Views Actores
class ActoresListView(ListView):
    model = Actor
    queryset = Actor.objects.all()
    context_object_name = 'actores'
    paginate_by = 12
    template_name = 'actores.html'

class ActoresDetailView(DetailView):
    model = Actor
    template_name = 'actor-detail.html'    

#Views Directores
class DirectoresListView(ListView):
    model = Director
    queryset = Director.objects.all()
    context_object_name = 'directores'
    paginate_by = 12
    template_name = 'directores.html'

class DirectoresDetailView(DetailView):
    model = Director
    template_name = 'director-detail.html'

class TemplateCriticas(TemplateView):
    template_name = 'criticas.html'


    
    def get_context_data(self, **kwargs ) :
        context = super().get_context_data(**kwargs)   
        context['criticas'] = Crítica.objects.filter()
        return context     

    #def get_queryset(self):
     #   self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
      #  return Book.objects.filter(publisher=self.publisher)