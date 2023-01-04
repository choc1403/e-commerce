
# Redirectores
from re import U
from warnings import filters
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse


#Librerias para el crud
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q 

# Modulos
from django.contrib.auth.models import User
from .models import Profile
from apps.products.models import Product
# Formularios
from .forms import RegistroForm

# Decoradores
from django.contrib.auth.mixins import UserPassesTestMixin

# Login
from django.contrib.auth import login
from django.contrib.auth import authenticate



# Create your views here.


# Decoradores
class user_authenticate(UserPassesTestMixin):
    '''
    Evalua si el usuario esta identificado
    '''
    def test_func(self):
        if not self.request.user.is_authenticated:
            return True
        else:
            return False

class user_admin(UserPassesTestMixin):
    '''
    Evalua si el usuario esta identificado
    '''
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False

# Creando cuenta nueva
class SignUp(user_authenticate,CreateView):
    '''
    MODULO PARA REGISTRO DE USUARIOS
    '''
    model = User
    form_class = RegistroForm    
    template_name = 'users/signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Register'
        context['messages.success'] = 'BIENVENIDO'
        context['product_exist'] = Product.objects.all()

        return context

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.success(self.request, 'USUARIO CREADO EXITOSAMENTE')
        return redirect('perfilUsuario')

    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))

# Funciones que hace el admin
# Listar usuarios
class Register(user_admin, ListView):
    '''
    Modulo para ver el listado de usuarios registrados
    '''
    template_name = 'users/registerList.html'
    queryset =  User.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'REGISTROS'
        context['product_exist'] = Product.objects.all()
        
        return context

    def handle_no_permission(self):
        '''
        Si el usuario no es admin
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))

# Crear Usuarios
class userCreate(user_admin, CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'users/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'createUser'
        context['product_exist'] = Product.objects.all()
        context['info'] = 'Agregar'
        return context
    
    def handle_no_permission(self):
        '''
        Si el usuario no es admin
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))
    
    success_url = reverse_lazy('users:listRegister')

# Detalles de un usuario
class userDetail(user_admin, DetailView):
    model = User
    template_name = 'users/detail.html'   

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'detailUser'
        context['product_exist'] = Product.objects.all()
        return context

    def handle_no_permission(self):
        '''
        Si el usuario no es admin
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))

#Eliminar usuario
class userDelete(user_admin, DeleteView):
    model = User
    template_name = 'users/delete.html'

    def handle_no_permission(self):
        '''
        Si el usuario no es admin
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))

    success_url = reverse_lazy('users:listRegister')

#Modificar usuario
class userUpdate(user_admin, UpdateView):
    model = User
    form_class = RegistroForm
    template_name = 'users/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'updateUser'
        context['product_exist'] = Product.objects.all()
        context['info'] = 'Editar'
        return context

    def handle_no_permission(self):
        '''
        Si el usuario no es admin
        :return:
        '''
        return HttpResponseRedirect(reverse('index'))
    
    success_url = reverse_lazy('users:listRegister')

# Buscar usuario
class userSearch(user_admin, ListView):
    template_name = 'users/search.html'

    def get_queryset(self):
        filters = Q(first_name__icontains = self.queryset()) | Q(last_name__icontains = self.queryset()) | Q(username__icontains = self.queryset())

        return User.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query
        context['count'] = context['object_list'].count()
        context['title'] = 'Search'
        context['product_exist'] = Product.objects.all()

        return context