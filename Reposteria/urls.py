from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500, handler403
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/',views.login_view, name='login'),
    path('logout',views.logout_view, name='logout'),   
    path('perfil/admin', login_required(views.PerfilAdmin.as_view()), name = 'perfilAdmin'),
    path('user/perfil', login_required(views.perfilUser), name='perfilUsuario'),
    path('user/', include('apps.users.urls')),
    path('product/', include('apps.products.urls')),
    path('category/', include('apps.categories.urls')),
    path('comment/', include('apps.Comments.urls')),
    path('fav/',include('apps.favorite.urls')),
    path('orders/', include('apps.orders.urls')),
    path('admin/', admin.site.urls),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler403 = views.error403
handler404 = views.error404
handler500 = views.error500


if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
