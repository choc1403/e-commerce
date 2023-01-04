

# Librerias para el crud
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, DeleteView, UpdateView

# Modulos
from .models import Product
from apps.categories.models import Category
from apps.votes.models import VotoProducto
from apps.favorite.models import favorito
from apps.Comments.models import Comentario, Respuesta
from django.db.models import Q 

# URL
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# DECORADORES
from django.contrib.auth.mixins import UserPassesTestMixin
from .utils import breadcrumb, breadcrum_detail

# forms
from .forms import ProductForm

#DESARROLLO PARA CLIENTES
class Producto(ListView):
    # APARTADO PARA MOSTRAR EL LISTADO DE PRODUCTOS
    template_name = "products/products.html"
    queryset = Product.objects.all().order_by('-id')
    paginate_by = 12

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] =  'Producto'
        context['breadcrumb'] = breadcrumb()
        context['category_list'] = Category.objects.all()
        context['product_exist'] = Product.objects.all()
        context['count'] = Product.objects.all().count()
        return context


def detailProduct(request,slug,pk):
    product = Product.objects.get(pk=pk)  
    slug = Product.objects.get(slug=slug)
    us = request.user.id
    estrelas=['1','2','3','4','5']

   

    filtro = Comentario.objects.filter(Q(product=pk))
    fav = favorito.objects.filter(Q(producto=pk) & Q(usuario=us))
    product_exists = Product.objects.all()
    

    context = {
        'title': slug,
        'product': product,
        'comentario_list':filtro,
        'favorito_list':fav,
        'product_exist': product_exists,
        'breadcrumb':breadcrum_detail(nombre=product),
        'estrella':estrelas
        

    }
    return render(request, 'products/detail.html', context)
    


# DESARROLLO PARA ADMINISTRADORES
class user_authenticate(UserPassesTestMixin):
    '''
    Evalua si el usuario es un super usuario
    '''
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False

class ProductoAdmin(user_authenticate,ListView):
    template_name = "products/admin/products.html"
    queryset = Product.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context['title'] =  'Producto Admin'
        context['product_exist'] = Product.objects.all()
        
        return context

    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index')) 

def deleteAdmin(request, pk):
    if request.user.is_superuser:
        producto = get_object_or_404(Product, pk=pk)
        if producto:
            producto.delete()
        return redirect('products:ProductoAdmin')
    else:
        return redirect('index')

class CreateAdmin(user_authenticate, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/admin/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar'
        context['product_exist'] = Product.objects.all()
        context['info'] = 'Agregar'
        return context

    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index')) 
    
    success_url = reverse_lazy('products:ProductoAdmin')

class UpdateAdmin(user_authenticate, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/admin/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['product_exist'] = Product.objects.all()
        context['info'] = 'Editar'
        return context

    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index')) 
    
    success_url = reverse_lazy('products:ProductoAdmin')