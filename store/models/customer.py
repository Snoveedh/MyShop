from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    
    
    # Here creating a func to save the customer details nce after submit and below is the process to save.
    
    def register(self):
        self.save()
        
    # Now look into the views objects are stored in values and register func is called from this model to save orelse you use "objectname.save()" directly
    
    
    
    # Here we are taking the email as unique constraint so user cant have multiple acc based on one email.if it see any email already exists then it wont create the account
    
    
    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        
        return False
    
    
    #Creating a func to get the hashi pwd using email from user data and that hash pwd is coverted using check_pwd by giving pwd as object
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
    
    
            
    