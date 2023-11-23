from django import template


register = template.Library()

# Now we define a function which says the product is present in
# cart or not

@register.filter(name='is_in_cart')
def is_in_cart(product ,cart):
    # logic to check product is present in cart or not
    # key which is present in cart of product which is match
    # with this product or not
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False;


@register.filter(name='cart_quantity')
def cart_quantity(product ,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id) # it returns the quantity in cart
    return 0;

@register.filter(name='price_total')
def price_total(product ,cart): #apply this price_total in html
    return product.price * cart_quantity(product , cart)

@register.filter(name='total_cart_price')
def total_cart_price(products , cart):
    sum = 0
    for p in products:
        sum += price_total(p, cart)

    return sum

    
