class Enemy:
    currentLocation = 1
    HP = 20
    attack = 1
    defense = 0
    money = 5
    isAlive = True

    def printStats(self):
        text = "HP: " + self.HP + "\n"
        text = "Attack: " + self.attack + "\n"
        text = "Defense: " + self.defense + "\n"
        text = "Money: " + self.money + "\n"
