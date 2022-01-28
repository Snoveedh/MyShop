from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

# Register your models here.

# admin.site.register(Product)
# admin.site.register(Category)


# writing the class to show the category names and product names in the django admin otherwise it wont show the real names of the category and products....only it shows as category 1 & 2, Product 1 & 2

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    
    
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    
    

    
    
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)