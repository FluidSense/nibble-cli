import click
from init import init

@click.command()
@click.argument('command', nargs=-1)
def main(command):
    choices, cart = init()
    if command == 'list':
        print(choices)
    if command == 'add':
        addToCart(cart)
    if command == 'status':
        status(cart)

@click.command()
@click.argument('item')
def addToCart(cart, item):
    cart.addItem(item)

def status(cart):
    print(cart)


if __name__ == "__main__":
    main()
