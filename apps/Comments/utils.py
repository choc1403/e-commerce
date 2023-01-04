from .models import Comentario

def get_or_create_comment(request):
    user = request.user if request.user.is_authenticated else None
    