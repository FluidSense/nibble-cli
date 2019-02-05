import os
from configparser import ConfigParser
import click
from list import getStore, printPriceList, initAppDir
from stage import stageItem, stageStatus

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
    with open(cfg,"w") as configfile:
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
    #TODO Save and load dict inbetween commands
    stageItem(item, amount)

@main.command("status")
def status():
    #TODO Echo staged items
    stageStatus()

@main.command("buy")
@click.option("--username", default= lambda: os.environ.get("USER", ""))
@click.option('--password', prompt=True, hide_input=True)
def buy(password):
    #TODO Pass staged items to OW to buy, and get username from .
    click.echo("Not yet implemented.")

@main.command("reset")
@click.option("-i","--item")
@click.option("--all")
def reset(item, all):
    #TODO Reset either all or single staged item
    click.echo("Not yet implemented")

@main.command("balance")
def balance():
    #TODO Get balance from API
    click.echo("Not yet implemented")

# FIXME Perhaps extract this and subcommands to it's own file
@click.group()
def config():
    pass

@config.command("user")
@click.argument("username")
def addUsername(username):
    #TODO
    pass