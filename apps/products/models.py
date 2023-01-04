import uuid
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save

from apps.categories.models import Category

# SETTINGS OF PROJECT
from Reposteria.settings import MEDIA_URL, STATIC_URL

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='products/', null=True, blank='True')
    category = models.ManyToManyField(Category, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/cinnamon01.jpg')
    
    def get_price(self):
        return 'Q {}'.format(self.price)

    def get_title(self):
        return self.title


def set_slug(sender, instance, *args, **kwargs): #callback
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8] )
            )

        instance.slug = slug

pre_save.connect(set_slug, sender=Product)
