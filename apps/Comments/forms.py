from cProfile import label
from tkinter import Widget
from .models import Comentario, Respuesta
from django import forms

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario

        fields = [
            'comentario'
            ]
        labels = {'comentario':'Comentario'}

        widgets = {
            'comentario': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
        }

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['respuesta']
        labels = {'respuesta':'Respuesta'}

        widgets = {
            'respuesta': forms.Textarea(attrs={'class':'form-control', 'rows':'2'}),
        }

        