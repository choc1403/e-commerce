from django.urls import reverse

def breadcrumb(products = False):
    return [
        {'title':'Productos', 'active':products, 'url': reverse('products:Producto')}
        
    ]

def breadcrum_detail(products = True, product = False, nombre=None, slug=None, pk=None):
    return [
        {'title':'Productos', 'active':products, 'url': reverse('products:Producto')},
        {'title': '{}'.format(nombre), 'active':product },
        
    ]

