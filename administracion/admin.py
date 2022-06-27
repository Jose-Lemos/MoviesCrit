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

    def get_peliculas(self, instance):  #mostrar peliculas en la que participa el Actor
        return [pelicula.nombre for pelicula in instance.peliculas.all()] 

     #[tag.name for tag in instance.tags.all()]
    get_peliculas.short_description = 'peliculas'  #cambio el nombre de la columna de la tabla

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
    ordering = ('-estrella','nombre')
    #search_fields = ('nombre', )
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


@admin.action(description='Validar Críticas Seleccionadas')
def validar_criticas(modeladmin, request, queryset):
    #print(queryset)
    #list_query = list(queryset)
    #suma_total = 0
    #cantidad_criticas_validas = 0
    #for critica in list_query:
     #   suma_total += critica.puntaje
      #  cantidad_criticas_validas += 1

    #promedio = suma_total / cantidad_criticas_validas
    #print(promedio)
    queryset.update(valida="válida")
    list_query = list(queryset)
    if len(list_query) > 0:
        list_query[0].actualizar_puntaje_pelicula()

@admin.action(description='Rechazar Críticas Seleccionadas')
def rechazar_criticas(modeladmin, request, queryset):
    queryset.update(valida="Rechazada")
    list_query = list(queryset)
    if len(list_query) > 0:
        list_query[0].actualizar_puntaje_pelicula()

@admin.register(Crítica)
class CriticaAdmin(admin.ModelAdmin):
    list_display = ('id', 'correo', 'comentario', 'puntaje', 'valida', 'pelicula', 'fecha')
    list_filter = ('valida', 'fecha', 'puntaje', 'pelicula', 'correo')
    list_display_links = ('correo',)
    ordering = ('-fecha',)
    list_editable = ('comentario', 'valida')
    exclude = ('correo','puntaje', 'fecha', 'pelicula')
    actions = [validar_criticas, rechazar_criticas]

    def has_add_permission(self, request):
        return False



@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  #vista tipo tabla
    ordering = ('nombre',)  #ordenamiento
    search_fields = ('nombre',)  #buscador
    list_display_links = ('nombre',)  #link a formulario
    list_per_page = 10 #paginacion