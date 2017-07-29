alive = True
playerX = 0
playerY = 0
player_name = "Johnny Biscuits"

#player_name = input("What is your name?\n:")
print(player_name)

def isAlive():
    #print("Player is currently: " + str(alive))
    return alive


def setAlive(boolean):
    print("Setting alive to: " + str(boolean))
    alive = boolean


def update():
    #nothing for now...
    print("")


def setPlayerX(x):
    global playerX
    playerX = x


def setPlayerY(y):
    global playerY
    playerY = y

def offsetPlayerX(x):
    global playerX
    playerX += x


def offsetPlayerY(y):
    global playerY
    playerY += y

def getPlayerX():
    global playerX
    return playerX


def getPlayerY():
    global playerY
    return playerY
