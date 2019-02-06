import os
import click
import json

appDir = click.get_app_dir("Nibble CLI")
stagepath = os.path.join(appDir, "stage.json")

def initStageFileIfNotExists():
  if not os.path.exists(stagepath):
    with open(stagepath, "w+") as stagefile:
      json.dump({},stagefile)

def stageItem(item, amount):
  global stagepath
  initStageFileIfNotExists()
  try:
    with open(stagepath) as stagefile:
      staged = json.load(stagefile)
  except FileNotFoundError:
    print("Could not stage item. If this is the first time you run Nibble CLI, run 'nibble --init'")
    return

  if item in staged:
    oldAmount = staged[item]
    if click.confirm(f"{item} already staged with amount of {oldAmount}. Overwrite amount?", abort=True):
      staged[item] = amount
  else:
    staged[item] = amount
  with open(stagepath, "w") as stagefile:
    json.dump(staged, stagefile)

def stageStatus():
  global stagepath
  try:
    with open(stagepath) as stagefile:
      print(json.load(stagefile))
  except FileNotFoundError:
    print("Run 'nibble --init'")
    return

  
