# Redirectores
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy, reverse

# Modulos
from .models import Category
from apps.products.models import Product

#Librerias para el crud
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Decoradores
from django.contrib.auth.mixins import UserPassesTestMixin

#forms
from .forms import CategorieForms
# Create your views here.
class user_admin(UserPassesTestMixin):
    '''
    Evalua si el usuario esta identificado
    '''
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False

class ListCategoryAdmin(user_admin, ListView):
    template_name = 'categories/listCategory.html'
    queryset = Category.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Categorias'
        context['product_exist'] = Product.objects.all()

        
        return context

    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))



class CreateCategoryAdmin(user_admin, CreateView):
    model = Category
    form_class = CategorieForms
    template_name = 'categories/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_exist'] = Product.objects.all()
        context['title'] = 'Agregar'
        context['info'] = 'Editar'

        return context
    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))

    success_url = reverse_lazy('categories:ListCategory')

def delete(request, pk):
    if request.user.is_superuser:
        categoria = get_object_or_404(Category, pk=pk)
        if categoria:
            categoria.delete()
        return redirect('categories:ListCategory')
    else:
        return redirect('index')

class UpdateCategoryAdmin(user_admin, UpdateView):
    model = Category
    form_class = CategorieForms
    template_name = 'categories/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_exist'] = Product.objects.all()
        context['title'] = 'Editar'
        context['info'] = 'Editar'

        return context
    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))

    success_url = reverse_lazy('categories:ListCategory')