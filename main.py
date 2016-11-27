import pygame   

def test():
    print("hello!")

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Adventure game!")
clock= pygame.time.Clock()

isPlayerAlive = True

while isPlayerAlive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isPlayerAlive = False
        print(event)
    pygame.display.update()

test()    
            


