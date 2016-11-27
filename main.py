import pygame, player  

pygame.init()

#Display Settings and clock...
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Adventure game!")
clock= pygame.time.Clock()

playerAlive = True

while player.isAlive():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player.setAlive(False)
        print(event)

    #update
    pygame.display.update()
    player.update()
    #FPS is set here!
    clock.tick(60)

pygame.quit()
quit()
            


