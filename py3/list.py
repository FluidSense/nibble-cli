import requests
import json
import click
import os

storepath = os.path.join(click.get_app_dir("Nibble CLI"), 'store.json')


def initAppDir(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    appDir = click.get_app_dir("Nibble CLI")
    if not os.path.isdir(appDir):
        os.makedirs(appDir)
    ctx.exit()


def getStore():
    store = requests.get("https://online.ntnu.no/api/v1/inventory")
    store = (
        json.loads(store.text) if store.status_code == 200
        else print("Error fetching inventory: " + str(store.status_code)))
    try:
        with open(storepath, "w+") as storefile:
            json.dump(store, storefile)
    except FileNotFoundError:
        print("could not save store, try --init if it's the first time using Nibble CLI")
        return


def readStore():
    try:
        with open(storepath) as storefile:
            store = json.load(storefile)
            return store
    except FileNotFoundError:
        print("Could not read store, try --update to force reload")
        return


def printPriceList():
    store = readStore()
    priceList = {k["name"]: k["price"] for k in store}
    for k, v in priceList.items():
        print(k, ":", f"{v}kr")
    return priceList
