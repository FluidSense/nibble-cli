import click
from list import getStore
@click.command()
@click.argument('command')
def main(command):
    if command == 'list':
        list()

def list():
    getStore()

if __name__ == "__main__":
    main()
