from django import forms
from .models import Category

class CategorieForms(forms.ModelForm):
    class Meta:
        model = Category

        fields = [
            'title',
            'description'
        ]

        labels = {
            'title': 'Titulo',
            'description': 'Descripcion'
        }

        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-control'}),
            'description': forms.Textarea(attrs = {'class':'form-control', 'rows':'3'}),
            
        }
