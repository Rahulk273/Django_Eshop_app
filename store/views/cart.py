from django.shortcuts import render , redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product

# Let's create class for login which handle login url inside login
# there is post request and get request that is handled by class

# after user perform login we want to save user information in session
class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys()) # we get product ids
        # we need full information of product and that we get from product model we pass list and we get all information
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request , 'cart.html' , {'products' : products})




