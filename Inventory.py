class Inventory:
    equippedItems = {}
    consumableItems = {}

    def printInventory(self):
        print("consumableItems: ")
        printDict(consumableItems)
        print("equippedItems: ")
        printDict(equippedItems)

    def printDict(self, dictToPrint):
        for x in dictToPrint:
            print(x)
            for y in dictToPrint[x]:
                print(y, ':', dictToPrint[x][y])

    def addConsumableItem(item):
        consumableItems.append(item)

    def addEquipItem(item):
        equippedItems.append(item)

    def __init__(self):
        print("Inventory!")


class Item:
    def __init__(self, id, itemName, value, itemDesc, type):
        print("Item!")
        self.id = id
        self.itemName = itemName
        self.desc = itemDesc
        self.value = value
        self.type = type

    def printItem(self):
        print("ID:" + str(self.id) + "\n" + "itemName:" + self.itemName)
