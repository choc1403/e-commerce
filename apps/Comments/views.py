

# URLS

from django.urls import reverse_lazy
from django.shortcuts import render,redirect, get_object_or_404



# LIBRERIAS PARA CREAR EL CRUD
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic.detail import DetailView
from django.db.models import Q

#MODELOS
from .models import Comentario, Respuesta
from apps.products.models import Product


#Formularios
from .forms import ComentarioForm, RespuestaForm

# OTROS
#from .utils 

# Create your views here.

def add(request):
    

    if request.method == 'POST':
        username = request.user
        product = get_object_or_404(Product, pk=request.POST.get('product_id'))
        slug = request.POST.get('product_slug')
        prId = request.POST.get('product_id')
        comentario = request.POST.get('comentario')
        coment = Comentario(product=product, user = username, comentario=comentario)        
        coment.save()
        
        return redirect('products:ProductoDetalle', slug, prId )
       
    else:
        return redirect('products:Producto' )




class list(ListView):
    template_name = 'Comments/list.html'

    queryset = Comentario.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


