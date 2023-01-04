# URL
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

#MODULOS
from django.contrib.auth.models import User
from apps.products.models import Product
from apps.orders.models import Order

#CRUD
from django.views.generic import TemplateView

#LOGIN
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate

#HTTP ERROR
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import UserPassesTestMixin

#Formularios
from .forms import RegisterForm

#MENSAJE
from django.contrib import messages

# This is page main
def index(request):
    product_list = Product.objects.order_by('-id')[:6]
    product_exists = Product.objects.all()
    return render(request, 'index.html',{
        'title': 'Inicio', 
        'product_list': product_list,
        'product_exist': product_exists
    })

def perfilUser(request):
    if not request.user.is_superuser:
        return render(request,"User's/perfil.html",{
            'title':'Usuario'
        }) 
    else:
        return redirect('perfilAdmin')

    

class user_authenticate(UserPassesTestMixin):
    '''
    Evalua si el usuario es un super usuario
    '''
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        else:
            return False

# Test for users is not admin
class PerfilAdmin(user_authenticate,TemplateView):
    template_name = "User's/Admin's/perfil.html"
    

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['count_user'] = User.objects.all().count()
        context['title'] = 'Perfil'
        context['count_product'] =Product.objects.all().count()
        context['product_exist'] = Product.objects.all()
        context['order_count'] = Order.objects.all().count()
        #product_list        
        return context

    def handle_no_permission(self):
        '''
        Si el usuario esta registrado lo regresa al inicio
        :return:
        '''
        return HttpResponseRedirect(reverse('index')) 




# login
def login_view(request):
    product_exists = Product.objects.all()
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username') #diccionario
        password = request.POST.get('password') #None

        user = authenticate(username=username, password=password)#None
        if user:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])

            if user.is_superuser:
                messages.success(request, 'Bienvenido ADMINISTRADOR: {}'.format(user.username))
                return redirect('perfilAdmin')
            else:
                messages.success(request, 'Bienvenido USUARIO: {}'.format(user.username))
                return redirect('perfilUsuario')

        else:
            messages.error(request, 'Usuario o contraseña no validos')

    return render(request, "User's/login.html", {
        'title':'LOGIN',
        'product_exist': product_exists,

    })

# logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')    



#ERRRO'S type HTTP
def error404(request, exception=None):
    return render(request, "Error's/error_404.html",{
        'title':'error 404'
    })

def error500(request, exception=None):
    return render(request, "Error's/error_500.html",{
        'title':'error 500'
    })

def error403(request, exception=None):
    return render(request, "Error's/error_403.html",{
        'title':'error 403'
    })   

def permission_denied_view(request):
    raise PermissionDenied