import requests, json
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
    store = json.loads(store.text) if store.status_code == 200 else print("Error fetching inventory: " + str(store.status_code))
    with open(storepath,"w+") as storefile:
        json.dump(store,storefile)

def printPriceList():
    try:
        with open(storepath) as storefile:
            store = json.load(storefile)
    except FileNotFoundError:
        print("Could not read store, try --update to force reload")
        return False
    priceList = {k["name"]:k["price"] for k in store}
    for k,v in priceList.items():
        print(k, v)
    return priceList
