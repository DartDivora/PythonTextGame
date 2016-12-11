import pygame, player, utils  

pygame.init()

display_width = 512
display_height = 512
tile_width = 20
tile_height = 20
columns = 12
rows = 12
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

def updatePlayer(x,y):
    gameDisplay.blit(playerImage,(x,y))
def updateText(x,y):
    gameDisplay.blit(text, textpos)
player.setPlayerX(0 + MARGIN)
player.setPlayerY(0 + MARGIN)

 
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
                player.offsetPlayerX(-1 * (tile_width + MARGIN))
            elif event.key == pygame.K_RIGHT:
                player.offsetPlayerX(tile_width + MARGIN)
            elif event.key == pygame.K_UP:
                player.offsetPlayerY(-1 * (tile_height + MARGIN))
            elif event.key == pygame.K_DOWN:
                player.offsetPlayerY(tile_height + MARGIN)
                
         
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
    updatePlayer(player.getPlayerX(),player.getPlayerY())
    updateText(0,0)            
    
    pygame.display.flip()
    #pygame.display.update()
    player.update()
    #FPS is set here!
    clock.tick(60)

pygame.quit()
quit()
            


