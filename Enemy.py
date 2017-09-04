from Entity import Entity

class Enemy(Entity):
    currentLocation = 1
    isAlive = True

    def printStats(self):
        text = "HP: " + self.HP + "\n"
        text = "Attack: " + self.attack + "\n"
        text = "Defense: " + self.defense + "\n"
        text = "Money: " + self.money + "\n"
