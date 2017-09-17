class Inventory:
    items = []

    def __init__(self):
        print("Inventory!")

class Item:
    def __init__(self,id, itemName, value, itemDesc):
        print("Item!")
        self.id = id
        self.itemName = itemName
        self.desc = itemDesc
        self.value = value

    def printItem(self):
        print("ID:" + str(self.id) + "\n" + "itemName:" + self.itemName)
