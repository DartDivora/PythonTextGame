import pygame, player, utils, time

pygame.init()

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
pygame.display.set_caption("Adventure game!")
clock= pygame.time.Clock()
playerImage = pygame.image.load('sprites/player.png')
playerImage = pygame.transform.scale(playerImage, (tile_width, tile_height))

def updatePlayer():
    pixelX = (MARGIN + tile_width) * player.getPlayerX() + MARGIN
    pixelY = (MARGIN + tile_width) * player.getPlayerY() + MARGIN
    gameDisplay.blit(playerImage,(pixelX,pixelY))
    #2 means already explored...
    grid[player.getPlayerX()][player.getPlayerY()] = 2
def updateText(x,y):
    text = font.render(gridData[str(player.getPlayerX()) + "," + str(player.getPlayerY())], 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    gameDisplay.blit(text, textpos)
def playerCollision(offsetX,offsetY):
    x = player.getPlayerX() + offsetX
    y = player.getPlayerY() + offsetY
    utils.debugPrint(x)
    utils.debugPrint(y)
    if x > -1 and x <= (rows - 1) and y > -1 and y <= (columns - 1) and grid[x][y] == 1:
        #Add Taylor's fighting logic here
        if True:
            print("Monster!")
            grid[x][y] = 0
            playerCollision(offsetX,offsetY)
    elif x > -1 and x <= (rows - 1) and offsetX != 0:
        player.offsetPlayerX(offsetX)
        return True
    elif y > -1 and y <= (columns - 1) and offsetY != 0:
        player.offsetPlayerY(offsetY)
        return True
    else:
        return False

player.setPlayerX(0)
player.setPlayerY(0)


# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = [[0 for x in range(columns)] for y in range(rows)]
gridData = {}
utils.debugPrint(grid)
for i in range(rows):
    for j in range(columns):
        #Generates a random number for the grid value. Currently being used
        # as a rudimentary monster spawner.
        grid[i][j] = utils.rand_num_gen(0,1)
        #Generates the description
        if i == 0 and j == 0:
            gridData[str(i) + "," + str(j)] = "Welcome to the Dungeon, my dude."
            #Having a monster on the starting square would be bad news...
            grid[0][0] = 0
        else:
            gridData[str(i) + "," + str(j)] = utils.randomDescription()
        utils.debugPrint(grid[i][j])

# Fill background
background = pygame.Surface(gameDisplay.get_size())
background = background.convert()
background.fill((250, 250, 250))
# Display some text
font = pygame.font.Font(None, 36)
updateText(0,0)

while player.isAlive():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player.setAlive(False)
        if event.type == pygame.KEYDOWN:
            #maybe change these to offsets...
            if event.key == pygame.K_LEFT:
                playerCollision(-1,0)
            elif event.key == pygame.K_RIGHT:
                playerCollision(1,0)
            elif event.key == pygame.K_UP:
                playerCollision(0,-1)
            elif event.key == pygame.K_DOWN:
                playerCollision(0,1)


        #print(event)



    # Set the screen background
    gameDisplay.fill(green)

    # Draw the grid
    for row in range(columns):
        for column in range(rows):
            if grid[column][row] == 0:
                color = red
            elif grid[column][row] == 1:
                color = blue
            elif grid[column][row] == 2:
                color = white
            pygame.draw.rect(gameDisplay,
                             color,
                             [(MARGIN + tile_width) * column + MARGIN,
                              (MARGIN + tile_height) * row + MARGIN,
                              tile_width,
                              tile_height])

    #update
    updateText(0,0)
    updatePlayer()
    pygame.display.flip()
    #pygame.display.update()
    #FPS is set here!
    clock.tick(60)

pygame.quit()
quit()
