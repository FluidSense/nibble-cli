from cart import Cart, Item
from list import getStore

def init():
    choices = getStore()
    cart = Cart()
    return choices, cart
