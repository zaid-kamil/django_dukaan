from django.shortcuts import render
from .models import Product, Brand, Category
from .filters import ProductFilter

def all_products(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request,'shop/products.html',{
        'filter': f,
        'brands': Brand.objects.filter(favorite=True),
        'categories': Category.objects.all()
    })

def brand_products(request, brand):
    brandObj = Brand.objects.get(slug=brand)
    products=Product.objects.filter(brand=brandObj)
    return render(request,'shop/brand_products.html',{
        'brand': brandObj,
        'products': products,
        'brands': Brand.objects.all(),
        'categories': Category.objects.all()
    })

def category_products(request, category):
    pass

def brand_category_products(request, brand, category):
    pass

def search_products(request):
    pass