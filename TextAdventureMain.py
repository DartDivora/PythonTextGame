import pygame
import time
import TextAdventureStrings
from random import randint
from random import choice
from Player import Player
from Enemy import Enemy


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


def getDialog(key):
    return TextAdventureStrings.dialog[key]

def getLocation(key):
    return TextAdventureStrings.locations[key]

def getCurrentText():
    counter = 0
    for tup in getDialogOptions(player.currentText):
        if counter == 0:
            textToDisplay = getDialog(tup) + "\n"
        else:
            textToDisplay += "     " + \
                str(counter) + ": " + getDialog(tup) + "\n"
        counter += 1
    return textToDisplay


def getDialogOptions(key):
    return TextAdventureStrings.dialog_options[key]


def processInput(keyPressed):
    if keyPressed == pygame.K_ESCAPE:
        print("Exiting the game!")
        player.isAlive = False
    elif keyPressed == pygame.K_1:
        optionPressed(1)
    elif keyPressed == pygame.K_2:
        optionPressed(2)
    elif keyPressed == pygame.K_3:
        optionPressed(3)
    elif keyPressed == pygame.K_4:
        optionPressed(4)
    elif keyPressed == pygame.K_5:
        optionPressed(5)


def optionPressed(number):
    global player
    dialogTup = getDialogOptions(player.currentText)
    if (len(dialogTup) - 1) >= number:
        choice = dialogTup[number]
        if choice == "Exit":
            print("Exiting the game!")
            player.isAlive = False
        elif choice == "Explore":
            #Replace with random choice
            player.setCurrentText(TextAdventureStrings.events[player.currentLocation][0])
        elif choice == "Attack":
            if player.isFighting:
                fight()
            else:
                goBack()
        elif choice == "Fight":
            print("You are having a fight!")
            player.isFighting = True
            player.setCurrentText("8")
        elif choice == "Stats":
            player.setCurrentText("Stats")
        elif choice == "Back":
            player.goBack()
        else:
            print(player.previousText)
            player.setCurrentText(choice)


def fight():
    global player, enemy
    if not enemy:
        enemy = Enemy()
    playerDamage = randint(0, player.attack) - enemy.defense
    if playerDamage > 0:
        enemy.HP = enemy.HP - playerDamage
    enemyDamage = randint(0, enemy.attack) - player.defense
    if enemyDamage > 0:
        player.HP = player.HP - enemyDamage
    if player.HP <= 0:
        player.isAlive = False
        print("You died, son...")
        fighting = False
        return
    elif enemy.HP <= 0:
        print("You win!")
        player.money = player.money + enemy.money
        fighting = False


pygame.init()
display_width = getConfig("display_width")
display_height = getConfig("display_height")
#currentText = TextAdventureStrings.npc["GameMaster"]
player = Player()
enemy = Enemy()
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

while player.isAlive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player.isAlive = False
        elif event.type == pygame.KEYDOWN:
            processInput(event.key)
    # Set the screen background
    gameDisplay.fill(getColor("black"))
    # update
    updateText(gameDisplay, getCurrentText(), (0, 0), font, getColor("white"))
    pygame.display.flip()
    # pygame.display.update()
    # FPS is set here!
    clock.tick(getConfig("FPS") * 1000)
    player.update()

pygame.quit()
quit()
