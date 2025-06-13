from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'image_url')
    list_filter = ('subcategory', 'subcategory__category')
    search_fields = ('name', 'subcategory__name')
    raw_id_fields = ('subcategory',)