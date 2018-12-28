import click
from init import init

@click.command()
@click.argument('command')
def main(command):
    choices, cart = init()
    if command == 'list':
        print(choices)
    if command == 'add':
        add()

@click.command()
@click.argument('item')
def add(item):
    cart.add(item)

if __name__ == "__main__":
    main()
