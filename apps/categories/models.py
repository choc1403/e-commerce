from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title