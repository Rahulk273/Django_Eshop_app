from django import template


register = template.Library()

# Now we define a function which says the product is present in
# cart or not

@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)

    
@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

