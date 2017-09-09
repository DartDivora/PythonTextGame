class Entity:

    level = 1
    exp = 50
    HP = 20
    attack = 4
    defense = 0
    money = 0
    isAlive = True
    currentLocation = "1"

    def printStats(self):
        text = "HP: " + str(self.HP) + "\n"
        text += "Attack: " + str(self.attack) + "\n"
        text += "Defense: " + str(self.defense) + "\n"
        text += "Money: " + str(self.money) + "\n"
        print(text)
        return text

    def __init__(self):
        print("Entity!")

    def update(self):
        pass
