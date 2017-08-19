import TextAdventureStrings


class Player:
    level = 1
    exp = 50
    currentLocation = "1"
    HP = 20
    attack = 4
    defense = 0
    money = 0
    isAlive = True
    isFighting = False
    currentText = TextAdventureStrings.npc["GameMaster"]
    previousText = []

    def printStats(self):
        text = "HP: " + str(self.HP) + "\n"
        text += "Attack: " + str(self.attack) + "\n"
        text += "Defense: " + str(self.defense) + "\n"
        text += "Money: " + str(self.money) + "\n"
        print(text)
        return text

    def goBack(self):
        self.currentText = self.previousText.pop()

    def setCurrentText(self, dialogID):
        self.previousText.append(self.currentText)
        self.currentText = dialogID

    def levelUp(self):
        self.attack += 1
        self.defense = self.defense + 1
        self.HP = self.HP + 5
        self.level = self.level + 1
        self.printStats()

    def checkLevelUp(self):
        if self.exp > (self.level * 25):
            return True
        return False

    def update(self):
        if self.checkLevelUp():
            self.levelUp()
