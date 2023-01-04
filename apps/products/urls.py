from django.urls import path

from django.contrib.auth.decorators import login_required


from . import views

app_name = 'products'

urlpatterns = [

    path('', views.Producto.as_view(), name = 'Producto'),
    path('admin/product/', login_required( views.ProductoAdmin.as_view()), name='ProductoAdmin'),
    path('detail/<slug:slug>/<int:pk>/', views.detailProduct, name ='ProductoDetalle'),
    path('admin/product/delete/<int:pk>/', login_required(views.deleteAdmin), name = 'deleteProduct'),
    path('admin/product/add/', login_required(views.CreateAdmin.as_view()), name = 'addProduct'),
    path('admin/product/update/<int:pk>/', login_required(views.UpdateAdmin.as_view()), name='updateProduct'),

]

'''
    Para el url del crud debe ir como:
    name/<int:pk>/
'''