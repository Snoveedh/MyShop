from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from .category import Category
import os.path

# Create your models here.

class Product(models.Model):
    
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=CASCADE, default=1)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500, default='',null=True,blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    category = models.ForeignKey(Category, on_delete=CASCADE, default=1)
    
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category= category_id)
        else:
            return Product.get_all_products()
        
        
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)  # Here id__in is used to get the list and the values in the ids list
    
    
    