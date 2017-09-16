class Inventory:
    items = []

    def __init__(self):
        print("Inventory!")

class Item:
    def __init__(self, value, itemDesc):
        print("Item!")
        self.desc = itemDesc
        self.value = value
