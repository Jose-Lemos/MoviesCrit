from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from administracion.models import Pelicula, Actor, Director, Crítica
from administracion.forms import CriticasForm
# Create your views here.
#Views Peliculas
class PeliculasListView(ListView):
    model = Pelicula
    queryset = Pelicula.objects.all()
    #context_object_name = 'peliculas'
    paginate_by = 12
    template_name = 'index.html'

    #def calculated_stars(self, **kwargs):
        
     #   criticas = []
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        peliculas_list = Pelicula.objects.values_list()  #return tupla: (1, 'DR STRANGE', 'Marvel', 2022, 'name_foto', promedio)
        
        for pelicula in peliculas_list:
            pelicula_obj =  Pelicula.objects.get(pk=pelicula[0])
            criticas_list = Crítica.objects.values_list('id', 'correo', 'comentario', 'puntaje').filter(pelicula = pelicula[0], valida = "válida")  #Lista de Críticas válidas de la película actual
            
            suma_total = 0.
            if (len(criticas_list) > 0):
                for critica in criticas_list:
                    suma_total += critica[3]
                    
                #print(suma_total)
                #print(len(criticas_list))
                promedio = suma_total / len(criticas_list)
                #print(promedio)
                pelicula_obj.estrella = promedio
                pelicula_obj.save()
                context['promedio'] = promedio

        context['peliculas'] = self.queryset
        
            #pelicula[5] = suma_total / len(criticas_list)
            #print(criticas_list)
            #print(pelicula[0]) // 1
        

        return context

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


