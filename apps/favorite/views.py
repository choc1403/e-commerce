

#URLS
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render,redirect, get_object_or_404

#MODELS
from .models import favorito
from apps.products.models import Product
from django.db.models import Q 

#CRUD
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

#formulario
from .forms import FavoritoForm

# Create your views here.

class list(ListView):
    template_name = 'favorite/list.html'
    queryset = favorito.objects.all()

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        return context

def addFav(request):
    if request.method == 'POST':
        slug = request.POST.get('product_slug')
        prId = request.POST.get('product_id')

        username = request.user
        product = get_object_or_404(Product, pk=request.POST.get('product_id'))
        
        
        favorit = favorito(producto=product, usuario = username)        
        favorit.save()
        
        return redirect('products:ProductoDetalle', slug, prId )
    else:
        return redirect('products:Producto')
     
 

def delete(request,slug, prodId, pk):    
    
    fav = get_object_or_404(favorito, pk=pk)

    if fav:
        fav.delete()
    return redirect('products:ProductoDetalle', slug, prodId)

