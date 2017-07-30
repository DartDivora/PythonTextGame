import pygame, time, TextAdventureStrings

def updateText():
    textToDisplay = ""
    for tup in currentText:
        if tup[0] != 0:
            textToDisplay += str(tup[0]) + ": "
        textToDisplay += tup[1] + "\n"

    text = font.render(textToDisplay, 1, getColor("white"))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    gameDisplay.blit(text, textpos)

def getConfig(key):
    return TextAdventureStrings.config[key]

def getColor(key):
    return TextAdventureStrings.colors[key]

def getDialog(key):
    return TextAdventureStrings.dialog[key]

pygame.init()

isAlive = True
display_width = getConfig("display_width")
display_height = getConfig("display_height")
currentText = TextAdventureStrings.dialog["Billy"]

#Display Settings and clock...
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Text Adventure game!")
clock= pygame.time.Clock()

# Fill background
background = pygame.Surface(gameDisplay.get_size())
background = background.convert()
background.fill(getColor("black"))
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
            elif event.key == pygame.K_1:
                print("pressed 1")
            elif event.key == pygame.K_2:
                print("pressed 2")
            elif event.key == pygame.K_2:
                print("pressed 3")
            elif event.key == pygame.K_2:
                print("pressed 4")
    # Set the screen background
    gameDisplay.fill(getColor("black"))
    #update
    updateText()
    pygame.display.flip()
    #pygame.display.update()
    #FPS is set here!
    clock.tick(getConfig("FPS"))

pygame.quit()
quit()
