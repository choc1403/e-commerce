
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'favorite'

urlpatterns = [
    path('add/', login_required(views.addFav), name='add'),
    path('',login_required(views.list.as_view()), name='favoritos' ),
    path('delete/<slug:slug>/<int:prodId>/<int:pk>', login_required(views.delete), name = 'delete')
    
    
]