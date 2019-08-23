import os
from configparser import ConfigParser
import click
import requests
from list import getStore, printPriceList, initAppDir, readStore, getItemNames
from stage import stageItem, stageStatus, resetAll, resetItem

staged = {}

APP_NAME = 'Nibble CLI'

def read_config():
    cfg = os.path.join(click.get_app_dir(APP_NAME), 'config.ini')
    parser = ConfigParser()
    parser.read([cfg])
    rv = {}
    for section in parser.sections():
        for key, value in parser.items(section):
            rv['%s.%s' % (section, key)] = value
    return rv

def write_config(readfile=None, init=False):
    config = ConfigParser()
    if readfile:
        config.read_dict(readfile)
    elif init:
        getStore()
        config["DEFAULT"] = {}
    cfg = os.path.join(click.get_app_dir(APP_NAME), 'config.ini')
    with open(cfg,"w+") as configfile:
        config.write(configfile)


@click.group()
@click.option("--init", is_flag=True, callback=initAppDir, is_eager=True, expose_value=False)
def main():
    config = read_config()

@main.command()
@click.option("--update", default=False, is_flag=True, help="force download of fresh item list")
def list(update):
    if update:
        getStore()
    printPriceList()


@main.command("add")
@click.argument("item", type=str)
@click.option("-a", "--amount", default=1, help="amount you wish to buy")
def add(item, amount):
    if item not in [k["name"] for k in readStore()]:
        click.echo(f"'{item}' not in item list. See 'nibble list' for options")
        return
    stageItem(item, amount)

@main.command("status")
def status():
    stageStatus()

@main.command("buy")
@click.option("--username", default= lambda: os.environ.get("USER", ""))
@click.option('--password', prompt=True, hide_input=True)
def buy(password):
    #TODO Pass staged items to OW to buy, and get username from .
    click.echo("Not yet implemented.")

@main.command("reset")
@click.argument("item", required=False, default=None, type=str)
@click.option("--quantity","-q", type=str, default=None)
@click.option("--all", default=False, is_flag=True)
def reset(item, quantity, all):
    if item and quantity:
        resetItem(item, quantity)
    elif item:
        resetItem(item)
    elif all:
        resetAll()


@main.command("balance")
def balance():
    #TODO Get balance from API
    click.echo("Not yet implemented")
    username = click.prompt("Enter username")
    password = click.prompt("Password", hide_input=True)
    headers = {'content-type': 'application/json', 'authentication:':''}
    balance = requests.get("https://online.ntnu.no/api/v1/usersaldo/", headers=headers)

@click.group(name="Config")
def user_config():
    config = read_config()