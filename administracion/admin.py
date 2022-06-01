from django.contrib import admin
from administracion.models import Actor, Director, Pelicula, Crítica, Categoria

# Register your models here.
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre' , 'get_peliculas')  #vista tipo tabla
    ordering = ('nombre',)  #ordenamiento
    search_fields = ('nombre',)  #buscador
    list_display_links = ('nombre',)  #link a formulario
    list_filter = ('nacionalidad', 'año_nacimiento')  #filtros
    list_per_page = 10 #paginacion

    def get_peliculas(self, instance):
        return [pelicula.nombre for pelicula in instance.peliculas.all()] 

     #[tag.name for tag in instance.tags.all()]
    get_peliculas.short_description = 'peliculas'

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'get_peliculas')  #vista tipo tabla
    ordering = ('nombre',)  #ordenamiento
    search_fields = ('nombre',)  #buscador
    list_display_links = ('nombre',)  #link a formulario
    list_filter = ('nacionalidad', 'año_nacimiento')  #filtros
    list_per_page = 10 #paginacion

    def get_peliculas(self, instance):
        return [pelicula.nombre for pelicula in instance.peliculas.all()] 

     #[tag.name for tag in instance.tags.all()]
    get_peliculas.short_description = 'peliculas'

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'resumen', 'año_realización', 'get_actores', 'get_directores', 'get_categorias')
    ordering = ('estrella','nombre')
    search_fields = ('nombre', )
    list_display_links = ('nombre',)
    list_filter = ('categorias', 'actores', 'directores', 'año_realización')


    
    def get_actores(self, instance):
        return [actor.nombre for actor in instance.actores.all()] 

     #[tag.name for tag in instance.tags.all()]
    get_actores.short_description = 'actores'

    def get_directores(self, instance):
        return [director.nombre for director in instance.directores.all()] 

    get_directores.short_description = 'directores'

    def get_categorias(self, instance):
        return [categoria.nombre for categoria in instance.categorias.all()] 

    get_categorias.short_description = 'categorias'

@admin.register(Crítica)
class CriticaAdmin(admin.ModelAdmin):
    list_display = ('id', 'correo', 'comentario', 'puntaje', 'valida', 'pelicula', 'fecha')
    ordering = ('fecha',)
    list_editable = ('comentario', 'valida')
    exclude = ('correo','puntaje', 'fecha', 'pelicula')

    def has_add_permission(self, request):
        return False



@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  #vista tipo tabla
    ordering = ('nombre',)  #ordenamiento
    search_fields = ('nombre',)  #buscador
    list_display_links = ('nombre',)  #link a formulario
    list_per_page = 10 #paginacion