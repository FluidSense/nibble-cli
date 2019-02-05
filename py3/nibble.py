import click
from list import getStore

staged = {}

@click.group()
def main():
    pass

@main.command()
def list():
    getStore()

@main.command("add")
@click.argument("item", type=str)
@click.option("-a", "--amount", default=1, help="amount you wish to buy")
def add(item, amount):
    global staged
    #TODO Save and load dict inbetween commands
    staged[item] = amount

@main.command("status")
def status():
    #TODO Echo staged items
    click.echo("Not yet implemented")

@main.command("buy")
@click.option('--password', prompt=True, hide_input=True)
def buy(password):
    #TODO Pass staged items to OW to buy.
    click.echo("Not yet implemented.")

@main.command("balance")
def balance():
    #TODO Get balance from API
    click.echo("Not yet implemented")

# Perhaps extract this and subcommands to it's own file
@click.group()
def config():
    pass

@config.command("user")
@click.argument("username")
def addUsername(username):
    #TODO
    pass