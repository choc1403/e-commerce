import logging
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'Comments'

urlpatterns = [
    path('add/', login_required(views.add), name='add'),   
    path('', views.list.as_view(), name='comentarios'),
    
]