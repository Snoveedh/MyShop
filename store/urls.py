"""Myshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from store.views.checkout import CheckOut
# from .views import index , signup, login
# from .views import index , Signup, Login
from .views import home, signup, login

# from .views.home import index
# from .views.signup import Signup
from .views.login import logout, Login
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
# from store.middlewares.auth import auth_middleware



urlpatterns = [
    # path('',index, name='homepage'),
    # path('',home.index, name='homepage'),
    path('',home.Index.as_view(), name='homepage'),
    # path('',index, name='homepage'),
    # path('signup',signup),
    # path('login', login),
    # path('signup',Signup.as_view()),
    path('signup',signup.Signup.as_view(), name='signup'),
    # path('signup',Signup.as_view(), name='signup'),
    # path('login', Login.as_view()),
    path('login', login.Login.as_view(), name='login'),
    # path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', Cart.as_view() , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', OrderView.as_view() , name='orders'),
    # path('orders', auth_middleware(OrderView.as_view()) , name='orders'),
    
    
]
