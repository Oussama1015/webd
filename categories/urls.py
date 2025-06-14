from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,  # New view for PATCH/DELETE
    SubCategoryListCreateView
)

urlpatterns = [
    # Categories
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),  # New!
    
    # Subcategories
    path('subcategories/', SubCategoryListCreateView.as_view(), name='subcategory-list'),
]