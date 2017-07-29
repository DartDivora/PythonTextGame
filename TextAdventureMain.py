import pygame, time

pygame.init()

isAlive = True
display_width = 512
display_height = 512
tile_width = 20
tile_height = 20
columns = 5
rows = 6
# This sets the margin between each cell
MARGIN = 5

#colors are a tuple with RGB values
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#Display Settings and clock...
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Text Adventure game!")
clock= pygame.time.Clock()

def updateText(x,y):
    text = font.render("hello", 1, white)
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    gameDisplay.blit(text, textpos)

# Fill background
background = pygame.Surface(gameDisplay.get_size())
background = background.convert()
background.fill((250, 250, 250))
# Display some text
font = pygame.font.Font(None, 36)

while isAlive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isAlive = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Exiting the game!")
                isAlive = False
    # Set the screen background
    gameDisplay.fill(black)
    #update
    updateText(0,0)
    pygame.display.flip()
    #pygame.display.update()
    #FPS is set here!
    clock.tick(60)

pygame.quit()
quit()
