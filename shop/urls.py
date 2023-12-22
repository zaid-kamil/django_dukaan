from django.urls import path
from . import views

urlpatterns = [
    # listing of products
    path('products/all/', views.all_products, name='all_products'),
    path('products/<slug:brand>/all/', views.brand_products, name='brand_products'),
    path('products/<slug:category>/all/', views.category_products, name='category_products'),
    path('products/<slug:brand>/<slug:category>/all/', views.brand_category_products, 
         name='brand_category_products'),
    # searching products
    path('products/search/', views.search_products, name='search_products'),
]