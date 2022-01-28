from django.shortcuts import render , redirect
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View






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
                    