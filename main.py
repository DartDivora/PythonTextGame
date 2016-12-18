import pygame, player, utils  

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
def updateText(x,y):
    gameDisplay.blit(text, textpos)
def playerCollision(offsetX,offsetY):
    x = player.getPlayerX() + offsetX
    y = player.getPlayerY() + offsetY
    print(x)
    print(y)
    if x > -1 and x <= (rows - 1) and offsetX != 0:
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
grid = []
for row in range(columns):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(rows):
        grid[row].append(0)  # Append a cell


# Fill background
background = pygame.Surface(gameDisplay.get_size())
background = background.convert()
background.fill((250, 250, 250))
# Display some text
font = pygame.font.Font(None, 36)
text = font.render("Welcome to the Dungeon, my dude.", 1, (10, 10, 10))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
background.blit(text, textpos)

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
            color = red
            pygame.draw.rect(gameDisplay,
                             color,
                             [(MARGIN + tile_width) * column + MARGIN,
                              (MARGIN + tile_height) * row + MARGIN,
                              tile_width,
                              tile_height])
            
    #update
    updatePlayer()
    updateText(0,0)            
    
    pygame.display.flip()
    #pygame.display.update()
    player.update()
    #FPS is set here!
    clock.tick(60)

pygame.quit()
quit()
            


