import pygame


class EntitySprite(pygame.sprite.Sprite):

    def __init__(self):
        super(EntitySprite, self).__init__()
        self.images = []
        self.images.append(pygame.image.load('sprites/player1.png'))
        self.images.append(pygame.image.load('sprites/player2.png'))
        # assuming both images are 64x64 pixels

        self.index = 0
        self.fpsCounter = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 50, 1024, 1024)

    def update(self):
        self.fpsCounter += 1
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        if self.fpsCounter >= 60:
            self.fpsCounter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
