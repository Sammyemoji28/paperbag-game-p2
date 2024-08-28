
import pgzrun
import random

HEIGHT = 600
WIDTH = 800

center_x = WIDTH//2
center_y = HEIGHT//2
center = (center_x, center_y)
currentLevel = 1
finalLevel = 7
startspeed = 10
gameOver = False
gameComp = False
ITEMS = ["bag","battery","bottle","chips"]
items = []
animations = []

def displayMessage(heading,subheading):
    screen.draw.text(heading, fontsize = 60, center = center, color = "white")
    screen.draw.text(subheading, fontsize = 30, center = (center_x,center_y + 30))

def draw():
    global items, currentlevel, gameover, gameComp
    screen.clear()
    screen.blit("bgimg",(0,0))
    if gameOver:
        displayMessage("You lose!","try again!")
    elif gameComp:
        displayMessage("You win!","congrats")
    else:
        for actor in items:
            actor.draw()

def getOptionToCreate(number_extraItems):
    itemsToCreate = ["paper"]
    for i in range(number_extraItems):
        randomOpt = random.choice(ITEMS)
        itemsToCreate.append(randomOpt)

    return itemsToCreate

def createItems(itemsToCreate):
    newItems = []
    for item in itemsToCreate:
        a = Actor(item + "img")
        newItems.append(a)

    return newItems

def layoutItems(itemsToLayout):
    numOfGaps = len(itemsToLayout) + 1
    gapSize = WIDTH / numOfGaps
    random.shuffle(itemsToLayout)
    for index , item in enumerate(itemsToLayout):
        newXpos = (index + 1)* gapSize
        item.x = newXpos

def animateItems(itemsToAnimate):
    global animations
    for item in itemsToAnimate:
        duration = startspeed - currentLevel
        item.anchor = ("center","bottom")
        animation = animate(item, duration = duration, on_finished = handleGameover, y = HEIGHT)
        animations.append(animation)

def handleGameover():
    global gameOver
    gameOver = True

def handleGameComplete():
    global currentLevel, items, animations, gameComp
    stopAnimations(animations)
    if currentLevel == finalLevel:
        gameComp = True
    else:
        currentLevel += 1
        items = []
        animations = []

def stopAnimations(animationsToStop):
    pass

def makeItems(number_extraItems):
    itemsToCreate = getOptionToCreate(number_extraItems)
    actorsList = createItems(itemsToCreate)
    layoutItems(actorsList)
    animateItems(actorsList)

    return actorsList

def update():
    global items
    if len(items) == 0:
        items = makeItems(currentLevel)

pgzrun.go