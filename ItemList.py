from Inventory import Item

ItemListTuple = {
    "Boot": (0, 200, "It's a dang boot","equipment"),
    "Gem": (0, 200, "A shiny gem","misc")
}

ItemList = {}

for key in ItemListTuple:
    item = ItemListTuple.get(key)
    ItemList[key] = Item(item[0],key,item[1],item[2],item[3])

def getItemByName(name):
    return ItemList.get(name)
