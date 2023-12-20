from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60, unique=True)
    def __str__(self):
        return self.name
class Brand(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60, unique=True)
    logo = models.ImageField(upload_to='brand/logo', blank=True, null=True)
    banner = models.ImageField(upload_to='brand/banner', blank=True, null=True)
    def __str__(self):
        return self.name
class Seller(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=60, unique=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='category')
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, related_name='brand')
    description = models.TextField()
    # related name helps to access the model from the related model
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING, related_name='seller')
    oprice = models.DecimalField(max_digits=10, decimal_places=2)
    sprice = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField(default=1)
    image = models.ImageField(upload_to='product/image', blank=True, null=True)

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    image = models.ImageField(upload_to='product/image', blank=True, null=True)
    def __str__(self):
        try:
            return self.image.url
        except:
            return self.product.name
        
from django.contrib.auth.models import User
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    review = models.TextField()
    rating = models.IntegerField(default=1)
    def __str__(self):
        return self.review
