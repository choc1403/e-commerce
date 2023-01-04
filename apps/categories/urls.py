from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
app_name = 'categories'

urlpatterns = [
    path('admin/list/', login_required( views.ListCategoryAdmin.as_view()), name='ListCategory'),   
    path('admin/add/', login_required( views.CreateCategoryAdmin.as_view()), name='addCategory'),
    path('admin/delete/<int:pk>/', login_required( views.delete), name='deleteCategories'),
    path('admin/update/<int:pk>/', login_required(views.UpdateCategoryAdmin.as_view()), name='updateCategories'),
]