from rest_framework import generics
from .models import Category, SubCategory
from .serializers import CategorySerializer, SubCategorySerializer

# Existing views
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryListCreateView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    
    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            return SubCategory.objects.filter(category_id=category_id)
        return super().get_queryset()

# 🔥 Add this new view for PATCH/DELETE
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer