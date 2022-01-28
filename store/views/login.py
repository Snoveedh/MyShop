
from django.shortcuts import render , redirect, HttpResponseRedirect
from store.models.customer import Customer
from django.contrib.auth.hashers import  check_password
from django.views import View



class Login(View):
    
    # def get(self, request):
    #     return render(request, 'login.html')
    
    return_url = None
    def get(self, request):
        
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
            
        
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        
        error_message = None
        
        if customer:
            
            flag = check_password(password, customer.password)
            
            if flag:
                
                # Here we are going to store the sessions i.e., cookies to store the user id, email when user login so that it will be easy to the server to remind the user information
                
                # request.session['customer_id'] = customer.id
                request.session['customer'] = customer.id
                # request.session['email'] = customer.email
                
                # return redirect('homepage')
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = "Email or Password Invalid !!!!...."
            
        else:
            error_message = "Email or Password Invalid !!!!...."
        
        print(email, password)
        
        return render(request, 'login.html', {'error' : error_message})
    
    
    
    

def logout(request):
    request.session.clear()
    
    return redirect('login')