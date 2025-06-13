from django.db import models
from categories.models import SubCategory

class Product(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.URLField(blank=True, null=True)
    iframe_link = models.TextField(blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
