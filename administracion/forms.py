from django import forms
from matplotlib import widgets
from .models import Director, Pelicula, Crítica, Actor


class CriticasForm(forms.ModelForm):
    class Meta:
        model = Crítica

        fields = [
                'correo',
                'comentario',
                'puntaje',
            ]


        widgets = {
            'correo': forms.EmailInput(attrs={'class':'form-control', 'id': 'email', 'placeholder': 'Email', 'required':True}), 
            'comentario':forms.Textarea(attrs={'class':'form-control', 'rows':8, 'placeholder':'Comentario', 'size': 300, 'required':True}),
            'puntaje':forms.NumberInput(attrs={'class':'form-control', 'id':'name', 'min':0., 'max':5., 'placeholder':'Puntaje','required':True}), 
        }


class PeliculasForm(forms.ModelForm):
    class Meta: 
        model = Pelicula

        fields = [
            'nombre',
        ]

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Peliculas', })
        }


class CategoriasForm(forms.ModelForm):
    class Meta: 
        model = Pelicula

        fields = [
            'categorias',
        ]

        widgets = {
            'categorias' : forms.TextInput(attrs={'class':'form-control',  })
        }

class DirectoresForm(forms.ModelForm):
    class Meta: 
        model = Director

        fields = [
            'nombre',
        ]

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Directores', })
        }

class ActoresForm(forms.ModelForm):
    class Meta: 
        model = Actor

        fields = [
            'nombre',
        ]

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Actores', })
        }


