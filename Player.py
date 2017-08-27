import TextAdventureStrings
from Entity import Entity


class Player(Entity):
    currentLocation = "1"
    isAlive = True
    isFighting = False
    currentText = TextAdventureStrings.npc["GameMaster"]
    previousText = []


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
