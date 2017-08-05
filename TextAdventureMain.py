import pygame
import time
import TextAdventureStrings


def updateText(surface, text, pos, font, color=pygame.Color('black')):
    # 2D array where each row is a list of words.
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def getConfig(key):
    return TextAdventureStrings.config[key]


def getColor(key):
    return TextAdventureStrings.colors[key]


def getCurrentText():
    textToDisplay = ""
    for tup in currentText:
        if tup[0] != 0:
            textToDisplay += str(tup[0]) + ": "
        textToDisplay += tup[1] + "\n"
    return textToDisplay


def getDialog(key):
    return TextAdventureStrings.dialog[key]


def processInput(keyPressed):
    if keyPressed == pygame.K_ESCAPE:
        print("Exiting the game!")
        isAlive = False
    elif keyPressed == pygame.K_1:
        print("pressed 1")
    elif keyPressed == pygame.K_2:
        print("pressed 2")
    elif keyPressed == pygame.K_3:
        print("pressed 3")
    elif keyPressed == pygame.K_4:
        print("pressed 4")


pygame.init()

isAlive = True
display_width = getConfig("display_width")
display_height = getConfig("display_height")
currentText = TextAdventureStrings.dialog["GameMaster"]

# Display Settings and clock...
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Text Adventure game!")
clock = pygame.time.Clock()

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
            processInput(event.key)
    # Set the screen background
    gameDisplay.fill(getColor("black"))
    # update
    updateText(gameDisplay, getCurrentText(), (0, 0), font, getColor("white"))
    pygame.display.flip()
    # pygame.display.update()
    # FPS is set here!
    clock.tick(getConfig("FPS"))


pygame.quit()
quit()
