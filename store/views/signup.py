from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
            # we do not send password to the server
            # so you have to fill the password again
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validatecustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)  # by this hashed password is saved
            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'value': value
            }
            return render(request, 'signup.html', data)  # show again same signup page

        # return HttpResponse(request.POST.get('email'))
        # return HttpResponse(request.POST) # we get key after submiting the form
        # if in above return statement we write  (request.POST.get('email')
        # then we get the email

    def validatecustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "First Name Required"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'

        return error_message

        # Saving
