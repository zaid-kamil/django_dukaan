from django.contrib import admin
from .models import Category, Brand, Seller, Product, ProductImage, ProductReview

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name','slug','logo')

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name','description')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','brand','seller','category','sprice', 'qty')

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product','image')

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product','user','review','rating')


