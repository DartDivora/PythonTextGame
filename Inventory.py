class Inventory:
    items = []

    def __init__(self):
        print("Inventory!")

class Item:
    def __init__(self):
        print("Item!")
        self.desc = "This is an item!"
