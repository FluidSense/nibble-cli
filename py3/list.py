import requests, json

def getStore():
    store = requests.get("https://online.ntnu.no/api/v1/inventory")
    store = json.loads(store.text) if store.status_code == 200 else print("Error fetching inventoryi: " + str(store.status_code))
    priceList = {k["name"]:k["price"] for k in store}
    for k,v in priceList.items():
        print(k, v)
    return priceList
