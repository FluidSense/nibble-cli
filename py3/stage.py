import os
import click
import json

appDir = click.get_app_dir("Nibble CLI")
stagepath = os.path.join(appDir, "stage.json")


def initStageFileIfNotExists():
    if not os.path.exists(stagepath):
        with open(stagepath, "w+") as stagefile:
            json.dump({}, stagefile)


def readStaged():
    global stagepath
    try:
        with open(stagepath) as stagefile:
            staged = json.load(stagefile)
            return staged
    except FileNotFoundError:
        print("Could not complete action due to missing staging area. Run nibble --init")


def updateStaged(newStaged):
    global stagepath
    with open(stagepath, "w+") as stagefile:
        json.dump(newStaged, stagefile)


def stageItem(item, amount):
    global stagepath
    initStageFileIfNotExists()
    staged = readStaged()
    if item in staged:
        oldAmount = staged[item]
        if click.confirm(f"{item} already staged with amount of {oldAmount}. Overwrite amount?", abort=True):
            staged[item] = amount
    else:
        staged[item] = amount
    updateStaged(staged)


def stageStatus():
    global stagepath
    try:
        with open(stagepath) as stagefile:
            print(json.load(stagefile))
    except FileNotFoundError:
        print("Run 'nibble --init'")
        return


def resetItem(item, quantity=None):
    global stagepath
    initStageFileIfNotExists()
    staged = readStaged()
    if quantity and item:
        if item in staged:
            staged[item] -= quantity
    else:
        staged.pop(item, None)
    updateStaged(staged)


def resetAll():
    global stagepath
    updateStaged({})
