import pygame, player  

pygame.init()

display_width = 800
display_height = 600

#colors are a tuple with RGB values
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

#Display Settings and clock...
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Adventure game!")
clock= pygame.time.Clock()
playerImage = pygame.image.load('sprites/finger.png')

def updatePlayer(x,y):
    gameDisplay.blit(playerImage,(x,y))
x = (display_width * 0.45)
y = (display_height * 0.8)

while player.isAlive():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player.setAlive(False)
        #print(event)

    #update
    gameDisplay.fill(white)
    updatePlayer(x,y)
    pygame.display.update()
    player.update()
    #FPS is set here!
    clock.tick(60)

pygame.quit()
quit()
            


