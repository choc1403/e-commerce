from django.urls import reverse

def breadcrumb(products = False):
    return [
        {'title':'Productos', 'active':products, 'url': reverse('products:Producto')}
        
    ]