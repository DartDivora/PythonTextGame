from Inventory import Item

ItemListTuple = {
    "Boot": (0, 200, "It's a dang boot"),
    "Gem": (0, 200, "A shiny gem")
}

ItemList = {}

for key in ItemListTuple:
    item = ItemListTuple.get(key)
    ItemList[key] = Item(item[0],key,item[1],item[2])

def getItemByName(name):
    return ItemList.get(name)
