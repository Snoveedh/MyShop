from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

# Create your views here.


# Create your views here.



# Here views.py is not needed all the code is copied and made diff views file under views folder.

# In this page you can see the function based and class based views for the home, signup, login 


# This page is only for reference and not being used anywhere in the project. Only using the views folder with diff view files.







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
    return render(request, 'index.html', data )



"""
def validateCustomer(customer):
    
    error_message = None
            
    if (not customer.first_name):
        error_message = "First Name Required!"
    elif len(customer.first_name) < 4:
        error_message = 'First Name Must be atleast 4 charecters long'
            
    elif len(customer.last_name) < 4:
        error_message = 'Last Name Must be atleast 4 charecters long'
                
    elif not customer.phone:
        error_message = " Phone Number is required"
            
    elif len(customer.phone) < 10:
        error_message = "Phone Number must be 10 char Long!!!"
                
    elif len(customer.email) < 5:
        error_message = 'Email must be 5 char long'
            
    elif len(customer.password) < 6:
        error_message = 'Password must be atleast 6 char Long'
                
    elif customer.isExists():
        error_message = 'Email Address is already registered'    
                
            
    return error_message
                

"""




"""
# This func code and above func code is used in signup class in post func. so commenting it


def registerUser(request):
    first_name = request.POST.get('first_name') # POST.get is used to get the specific object which was given by user
    last_name = request.POST.get('last_name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    password = request.POST.get('password')
        
    # Validations
        
    value = {
        'first_name' : first_name,
        'last_name' : last_name,
        'phone' : phone,
        'email' : email
            
    }
        
    error_message= None
        
        
    customer = Customer(first_name=first_name,
                            last_name = last_name,
                            phone = phone,
                            email = email,
                            password = password)
            
    
    error_message = validateCustomer(customer)    

    # Saving
    if not error_message:
        print(first_name, last_name,phone,email,password)
        customer.password = make_password(customer.password)
        customer.register()
            
            
            
        # return render(request, 'index.html')  # Here we served index page but products will not sow once after creating account so we need to copy the index func code to get all products. but instead of copying we are using redirect option to reuse the index code
            
        # return redirect('http://localhost:8000')
        return redirect('homepage')
            
    
    else:
            
        data = {
            'error' : error_message,
            'values' : value
        }
        return render(request, 'signup.html', data) 
        
        
"""
    
    
    


"""
def signup(request):
    # return render(request, 'signup.html')
    
    #Here GET will be taken when page reolad and POST is taken when user clicks on create acc button. So depends on GEt, POST we are writing the login wit same signup template
    
    if request.method== 'GET':
        return render(request, 'signup.html')
    
    else:
        return registerUser(request)
    
    
        """
        

            
        
        
        
    
    
    
    # Creating a function to convert the user given pwd to hashcode and save in db and simliary check pwd which will import te hash pwd while login
    
    
    
    
    
"""
# check the signup code in views folder and created a separate views file for signup.

class Signup(View):
    
    def get(self, request):
        return render(request, 'signup.html')
    
    
    
    def post(self, request):
        
        first_name = request.POST.get('first_name') # POST.get is used to get the specific object which was given by user
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
            
        # Validations
            
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email
                
        }
            
        error_message= None
            
            
        customer = Customer(first_name=first_name,
                                last_name = last_name,
                                phone = phone,
                                email = email,
                                password = password)
                
        
        error_message = self.validateCustomer(customer)    

        # Saving
        if not error_message:
            print(first_name, last_name,phone,email,password)
            customer.password = make_password(customer.password)
            customer.register()
                
                
                
            # return render(request, 'index.html')  # Here we served index page but products will not sow once after creating account so we need to copy the index func code to get all products. but instead of copying we are using redirect option to reuse the index code
                
            # return redirect('http://localhost:8000')
            return redirect('homepage')
                
        
        else:
                
            data = {
                'error' : error_message,
                'values' : value
            }
            return render(request, 'signup.html', data) 
    
    
    
    
    def validateCustomer(self, customer):
    
        error_message = None
                
        if (not customer.first_name):
            error_message = "First Name Required!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name Must be atleast 4 charecters long'
                
        elif len(customer.last_name) < 4:
            error_message = 'Last Name Must be atleast 4 charecters long'
                    
        elif not customer.phone:
            error_message = " Phone Number is required"
                
        elif len(customer.phone) < 10:
            error_message = "Phone Number must be 10 char Long!!!"
                    
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
                
        elif len(customer.password) < 6:
            error_message = 'Password must be atleast 6 char Long'
                    
        elif customer.isExists():
            error_message = 'Email Address is already registered'    
                    
                
        return error_message
                    
        
    """





"""
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        
        error_message = None
        
        if customer:
            
            flag = check_password(password, customer.password)
            
            if flag:
                return redirect('homepage')
            else:
                error_message = "Email or Password Invalid !!!!...."
            
        else:
            error_message = "Email or Password Invalid !!!!...."
        
        print(email, password)
        
        return render(request, 'login.html', {'error' : error_message})
        
        
        """
    
    
    
    # Now we will use the class based models instead of function based. using class based there will be less coding and more features
    
    
    
"""

# check the Login code in views folder and created a separate views file for Login.
   

class Login(View):
    
    def get(self, request):
        return render(request, 'login.html')
            
        
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        
        error_message = None
        
        if customer:
            
            flag = check_password(password, customer.password)
            
            if flag:
                return redirect('homepage')
            else:
                error_message = "Email or Password Invalid !!!!...."
            
        else:
            error_message = "Email or Password Invalid !!!!...."
        
        print(email, password)
        
        return render(request, 'login.html', {'error' : error_message})
        
        
        """ 