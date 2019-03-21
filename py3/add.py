
def add(cart, choices, item):
    if item not in cart and item in choices:
        cart.add(item)

