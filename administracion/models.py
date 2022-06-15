import datetime
from django.db import models
from PIL import Image

# Create your models here.

class Elenco(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    año_nacimiento = models.PositiveIntegerField()
    resumen_biografico = models.TextField(max_length=300)

    # Modifico el save para que redimensione la imagen antes de guardar
    #def save(self, *args, **kwargs):
    #    super().save(*args, **kwargs)
    #    if self.foto:
    #        img = Image.open(self.foto.path)
    #        if img.height > 300 or img.width > 300:
    #            img.thumbnail((300, 300))
    #            img.save(self.foto.path)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]

#El admin carga los actores
class Actor(Elenco):
    foto = models.ImageField(upload_to="actores/",default="elenco-default.png",null=True, blank=True)


#El admin carga los directores
class Director(Elenco):
    foto = models.ImageField(upload_to="directores/",default="elenco-default.png",null=True, blank=True)

#El admin carga las categorias
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

#El admin carga las peliculas
class Pelicula(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    resumen = models.TextField(max_length=300)
    año_realización = models.PositiveIntegerField()
    foto = models.ImageField(upload_to="peliculas/", default="pelicula-default.png", null=True, blank=True)
    categorias = models.ManyToManyField(Categoria, related_name='peliculas')
    actores = models.ManyToManyField(Actor, related_name='peliculas')
    directores = models.ManyToManyField(Director, related_name='peliculas')
    estrella = models.FloatField()

    def ranking():
        pass

    def cantidad_criticas():
        pass

    #def get_actores(self):
     #   for actor in self.actores :


    def __str__(self):
        return self.nombre
    

#Los usuarios realizan las críticas
class Crítica(models.Model):
    ESTADO_CHOICES = (
        ('espera', "Esperando Validación"),
        ('rechazada', "Rechazada"),
        ('valida', "válida"),
    )
    correo = models.EmailField()
    comentario = models.TextField(max_length=300)
    puntaje = models.FloatField()
    valida = models.CharField(max_length=100, choices=ESTADO_CHOICES, default='espera')
    pelicula = models.ForeignKey(Pelicula, on_delete=models.DO_NOTHING)
    fecha = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '{0} {1} {2}'.format(self.correo, self.comentario, self.puntaje)


