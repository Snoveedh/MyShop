from django.shortcuts import render , redirect

from store.models.product import Product
from store.models.category import Category
from django.views import View



# Create your views here.


# Create your views here.
"""
def index(request):
    # return HttpResponse('<h1> Index page </h1>')
    # products = Product.get_all_products()
    products = None
    categories = Category.get_all_categories()
    
    categoryId = request.GET.get('category') # here to see the request which we received by user
    
    if categoryId:
        products = Product.get_all_products_by_categoryid(categoryId)
    else:
        products = Product.get_all_products()
    
    
    data = {}
    #here passing the key, values in data dictionary and assigining in return
    
    data['products'] = products
    data['categories'] = categories
    
    # Here checking the customer information storage using ession which is used in login.py and here we are validating whether user mail id is printing or not in the terminal
    print('You are: ',request.session.get('email'))
    
    
    return render(request, 'index.html', data )

"""


class Index(View):
    def get(self, request):
        
        
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        
        products = None
        categories = Category.get_all_categories()
        
        categoryId = request.GET.get('category') # here to see the request which we received by user
        
        if categoryId:
            products = Product.get_all_products_by_categoryid(categoryId)
        else:
            products = Product.get_all_products()
        
        
        data = {}
        #here passing the key, values in data dictionary and assigining in return
        
        data['products'] = products
        data['categories'] = categories
        
        # Here checking the customer information storage using ession which is used in login.py and here we are validating whether user mail id is printing or not in the terminal
        print('You are: ',request.session.get('email'))
        
        
        return render(request, 'index.html', data )
    

    
    
    
    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        # print(product)
        cart = request.session.get('cart')
        
        
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else: 
                        cart[product] = quantity-1
                else:
                    cart[product] = 1 + quantity
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
            
        request.session['cart'] = cart
        print('cart: ', request.session['cart'])
        
        return redirect('homepage')
