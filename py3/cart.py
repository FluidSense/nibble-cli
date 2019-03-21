
class Cart:
    def __init__(self):
        self.inventory = []

    def addItem(self, item):
        self.inventory.add(item)

class Item:
    def __init__(self, price, name):
        self.price = price
        self.name = name
        self.quantity = 0

    def addOne(self):
        self.quantity += 1

