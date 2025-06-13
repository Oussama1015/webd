from rest_framework import serializers
from .models import Product
from categories.serializers import SubCategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(read_only=True)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'image_url', 'iframe_link', 'subcategory']