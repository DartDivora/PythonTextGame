import TextAdventureStrings


class Player:
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
        text = "HP: " + self.HP + "\n"
        text = "Attack: " + self.attack + "\n"
        text = "Defense: " + self.defense + "\n"
        text = "Money: " + self.money + "\n"

    def goBack(self):
        self.currentText = self.previousText.pop()

    def setCurrentText(self, dialogID):
        self.previousText.append(self.currentText)
        self.currentText = dialogID

    def update(self):
        print("stuff")
