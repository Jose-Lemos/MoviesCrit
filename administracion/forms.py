from django import forms
from .models import Crítica


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


