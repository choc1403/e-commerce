from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [

    path('signUp/', views.SignUp.as_view(), name = 'signUp'),
    path('list/register/', views.Register.as_view(), name = 'listRegister'),
    path('admin/user/add', views.userCreate.as_view(), name='addUser'),
    path('admin/user/update/<int:pk>', views.userUpdate.as_view(), name='updateUser'),

]