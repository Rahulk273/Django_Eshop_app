from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.orders import Order
from store.middlewares.auth import auth_middleware



class OrderView(View):


    def get(self , request):
        customer = request.session.get('customer') # So we get customer and from customer we get the id of that customer and we fetch all the orders with the help of customers id
        orders = Order.get_orders_by_customer(customer)
        print(orders)

        return render(request , 'orders.html' , {'orders' : orders})
