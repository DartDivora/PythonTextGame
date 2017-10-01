from Entity import Entity

class Enemy(Entity):
    location = 1
    items = []

    def __init__(self,location):
        self.location = location
        print("Enemy!")
