from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View



# Let's create class for login which handle login url inside login
# there is post request and get request that is handled by class

# after user perform login we want to save user information in session
class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        # now from this email we bring the customer/user
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)

                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email or Password invalid'


        else:
            error_message = 'Email or Password invalid'
        print(email, password)
        return render(request, 'login.html', {'error': error_message})
        # from database for the input email we access  the
        # values and we take customer record and also match
        # the password

    # lec no 31 To handle the requests we use class based views because
    # there are many ways of request


def logout(request):
    request.session.clear()
    return redirect('login')