from django.urls import path
from .views import CategoryListCreateView, SubCategoryListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('subcategories/', SubCategoryListCreateView.as_view(), name='subcategory-list'),
]