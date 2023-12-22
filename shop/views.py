from django.shortcuts import render
from .models import Product, Brand, Category
from .filters import ProductFilter

def all_products(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request,'shop/products.html',{
        'filter': f,
        'brands': Brand.objects.all(),
        'categories': Category.objects.all()
    })

def brand_products(request, brand):
    pass

def category_products(request, category):
    pass

def brand_category_products(request, brand, category):
    pass

def search_products(request):
    pass