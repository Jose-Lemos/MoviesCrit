from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from administracion.models import Pelicula, Actor, Director, Crítica
from administracion.forms import CriticasForm, PeliculasForm, ActoresForm, DirectoresForm
from django.db.models import Q
# Create your views here.
#Views Peliculas
class PeliculasListView(TemplateView):
    #model = Pelicula
    queryset = Pelicula.objects.all().order_by('-estrella')
    #context_object_name = 'peliculas'
    paginate_by = 12
    template_name = 'index.html'
    form_class = PeliculasForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        peliculas = list(self.queryset)
        for pelicula_obj in peliculas:
            criticas_pelicula = list(Crítica.objects.filter(pelicula = pelicula_obj.pk, valida = "válida"))
            
            if len(criticas_pelicula) > 0:
                suma_total = 0
                for critica in criticas_pelicula:
                    suma_total += critica.puntaje
                suma_total += pelicula_obj.estrella
                promedio = suma_total / (len(criticas_pelicula)+1)
                pelicula_obj.actualizar_estrellas(promedio)
            
        context['peliculas'] = self.queryset
        context['form'] = self.form_class
        return context
    
    def post(self, request, **kwargs):
        busqueda = request.POST.get("nombre")
        context = super().get_context_data(**kwargs)
        context['peliculas'] = self.queryset
        context['form'] = self.form_class

        if request.method == "POST":
            if busqueda: 
                peliculas = Pelicula.objects.filter(
                    Q(nombre__icontains = busqueda)
                ).distinct()
                if peliculas.exists() == True:
                    context['peliculas'] = peliculas
                return self.render_to_response(context)
            else:
                return self.render_to_response(context)
            
        
        
        

        

class PeliculasDetailView(TemplateView):
    #model = Pelicula
    template_name = 'pelicula-detail.html'
    form_class = CriticasForm
    #context_object_name = "pelicula"

    pelicula = Pelicula()




    def get_context_data(self, **kwargs):
        pk_peli = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['pelicula'] = Pelicula.objects.get(pk = pk_peli)
        self.pelicula = Pelicula.objects.get(pk=pk_peli)
        context['criticas'] = Crítica.objects.filter(pelicula = pk_peli, valida = "válida")
        context['actores'] = Actor.objects.filter(peliculas = self.pelicula)
        context['directores'] = Director.objects.filter(peliculas = self.pelicula)
        context['form'] = self.form_class
        #print(context['pelicula'])
        #print(context['criticas'])
        return context

    
    def post(self, request, *args, **kwargs):
        pk_peli = self.kwargs['pk']
        correo = request.POST['correo']
        puntaje = request.POST['puntaje']
        comentario = request.POST['comentario']
        new_critica = Crítica()
        new_critica.correo = correo
        new_critica.puntaje = puntaje
        new_critica.comentario = comentario
        new_critica.pelicula = Pelicula.objects.get(pk = pk_peli)
        new_critica.save()
        #print(correo, puntaje, comentario)
        #print(self.kwargs['pk'])
        #print(new_critica)
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

#Views Actores
class ActoresListView(TemplateView):
    #model = Actor
    queryset = Actor.objects.all()
    #context_object_name = 'actores'
    paginate_by = 12
    template_name = 'actores.html'
    form_class = ActoresForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actores'] = self.queryset
        context['form'] = self.form_class
        return context

    def post(self, request, **kwargs):
        busqueda = request.POST.get("nombre")
        context = super().get_context_data(**kwargs)
        context['actores'] = self.queryset
        context['form'] = self.form_class

        if request.method == "POST":
            if busqueda: 
                actores = Actor.objects.filter(
                    Q(nombre__icontains = busqueda)
                ).distinct()
                if actores.exists() == True:
                    context['actores'] = actores
                return self.render_to_response(context)
            else:
                return self.render_to_response(context)


class ActoresDetailView(DetailView):
    model = Actor
    template_name = 'actor-detail.html'   

    actor = Actor()

    def get_context_data(self, **kwargs):
        pk_actor = self.kwargs['pk']
        context = super().get_context_data(**kwargs) 
        context['actor'] = Actor.objects.get(pk = pk_actor)
        self.actor = Actor.objects.get(pk = pk_actor)
        context['peliculas'] = Pelicula.objects.filter(actores = self.actor)

        return context

#Views Directores
class DirectoresListView(TemplateView):
    #model = Director
    queryset = Director.objects.all()
    #context_object_name = 'directores'
    paginate_by = 12
    template_name = 'directores.html'
    form_class = DirectoresForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directores'] = self.queryset
        context['form'] = self.form_class
        return context

    def post(self, request, **kwargs):
        busqueda = request.POST.get("nombre")
        context = super().get_context_data(**kwargs)
        context['directores'] = self.queryset
        context['form'] = self.form_class

        if request.method == "POST":
            if busqueda: 
                directores = Director.objects.filter(
                    Q(nombre__icontains = busqueda)
                ).distinct()
                if directores.exists() == True:
                    context['directores'] = directores
                return self.render_to_response(context)
            else:
                return self.render_to_response(context)






class DirectoresDetailView(DetailView):
    model = Director
    template_name = 'director-detail.html'

    director = Director()

    def get_context_data(self, **kwargs):
        pk_director = self.kwargs['pk']
        context = super().get_context_data(**kwargs) 
        context['director'] = Director.objects.get(pk = pk_director)
        self.director = Director.objects.get(pk = pk_director)
        context['peliculas'] = Pelicula.objects.filter(directores = self.director)

        return context


