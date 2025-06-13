from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        subcategory_id = self.request.query_params.get('subcategory_id')
        if subcategory_id:
            return Product.objects.filter(subcategory_id=subcategory_id)
        return super().get_queryset()