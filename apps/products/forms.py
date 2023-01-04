from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = [
            'title',
            'description',
            'price',            
            'category',
            'image'
            ]

        labels = {
            'title': 'Titulo',
            'description': 'Descripcion',
            'price': 'Precio',            
            'category': 'Categorias',
            'image':'Imagen',
        }

        widgets = {
            'title': forms.TextInput(attrs = {'class':'form-control'}),
            'description': forms.Textarea(attrs = {'class':'form-control', 'rows':'3'}),
            'price': forms.TextInput(attrs = {'class':'form-control', 'type': 'number', 'min': '0', 'step':"0.1"}),            
            'category':forms.CheckboxSelectMultiple(attrs={'type':'checkbox'}),
            'image':forms.FileInput(attrs={'type':'checkbox', 'name':'image', 'type':'file', 'accept':'image'})
        }