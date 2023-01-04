from tkinter import Widget
from django import forms
from .models import favorito

class FavoritoForm(forms.ModelForm):
    class Meta:
        model = favorito

        fields = [
            'usuario',
            'producto'
        ]
        labels = {
            'usuario': 'usuario',
            'producto':'producto',
        }
        widgets = {
            'usuario': forms.Select(),
            'producto': forms.RadioSelect()
            }
            