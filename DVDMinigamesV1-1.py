import pygame as p
#import pygame_menu
import time
from pygame import K_c, K_h, K_s, K_f, K_p, K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9, K_x
import os
import random

##Notes
 # #print(p.font.match_font('chalkboardttc')) pritns the font you want
#coin object
class Coin:
  def __init__(self, x, y, radius, visible):
    self.x = x
    self.y = y
    self.radius = radius
    self.visible = visible

#wall object
class Wall:
  def __init__(self, x, lx, rx, length, width, visible):
    self.x = x
    self.lx = lx
    self.rx = rx
    self.length = 100
    self.width = width
    self.visible = True

#some constants
gameModes = ["Coin Collect", "Maze Beta", "Geometry Guesser"]
buttonColor = (128,128,0)
black = (0,0,0)
active = True
mode = 0
p.init()
DISPLAY_WIDTH, DISPLAY_HEIGHT = 16*50, 9*50
RESCALE_W = 100
RESCALE_H = 100
SCREEN_WIDTH, SCREEN_HEIGHT = int(p.display.Info().current_w), int(p.display.Info().current_h) #max w and h
dvdImg = p.image.load('dvd.png')
dvdImg = p.transform.scale(dvdImg, (RESCALE_W,RESCALE_H))
coinImg = p.image.load('coin.jpg')
coinImg = p.transform.scale(coinImg, (RESCALE_W,RESCALE_H))
font = p.font.Font(None, 25)

gameDisplay = p.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
p.display.set_caption("The New Game")


main_dir = os.path.split(os.path.abspath(__file__))[0]

start_ticks = p.time.get_ticks()

x = DISPLAY_WIDTH-(RESCALE_W/2)+17
y = DISPLAY_HEIGHT-(RESCALE_H/2)+24
velocity = 2

#pygame custom functions
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def img(x,y):
    gameDisplay.blit(dvdImg, (int(x),int(y)))

def preReqs():
    seconds=(p.time.get_ticks()-start_ticks)/1000 #calculate how many seconds

    for event in p.event.get():
        if event.type == p.QUIT:
            active = False
            return False
    return True

def mainMenu():
    nextMode = 0
    active = True
    while active:

        active = preReqs()
        keys=p.key.get_pressed()
        cursorX = p.mouse.get_pos()[0]
        cursorY = p.mouse.get_pos()[1]
        click = p.mouse.get_pressed()[0]

        if keys[K_c]:
            print("Manual Override. Something must've went wrong or your just a pro-debugger")
            active = False
        if keys[K_p]:
            nextMode = 1
        gameDisplay.fill((200,200,200))
        #add backround rectangles
        if((cursorX > 0 and cursorX < 50) and (cursorY > 0 and cursorY < 20) and click):
            nextMode = 0 #return to main menu
        if((cursorX > DISPLAY_WIDTH/2 - 100 and cursorX < DISPLAY_WIDTH/2) and (cursorY > DISPLAY_HEIGHT/2 and cursorY < DISPLAY_HEIGHT/2 + 40) and click):
            nextMode = 2 #enter classic Mode
        if((cursorX > DISPLAY_WIDTH/2 + 10 and cursorX < DISPLAY_WIDTH/2 + 110) and (cursorY > DISPLAY_HEIGHT/2 and cursorY < DISPLAY_HEIGHT/2 + 40) and click):
            nextMode = 1 #enter coin Mode
        if nextMode != 0:
            active = False

        #add Title
        title = p.font.Font('/System/Library/Fonts/Supplemental/Chalkboard.ttc', 40)
        TextSurf, TextRect = text_objects("Digital Versatile", title)
        TextRect.center = (int((DISPLAY_WIDTH/2)),150)
        gameDisplay.blit(TextSurf, TextRect)

        #add Relax and Play Button
        p.draw.rect(gameDisplay,buttonColor, p.Rect(int(DISPLAY_WIDTH/2 - 100),int(DISPLAY_HEIGHT/2),100,40))
        modeText = p.font.Font('/System/Library/Fonts/Supplemental/Chalkboard.ttc', 20)
        textSurf, textRect = text_objects("Relax", modeText)
        textRect.center = (int((DISPLAY_WIDTH/2 - 50)), int((DISPLAY_HEIGHT/2 + 20)))
        gameDisplay.blit(textSurf, textRect)

        p.draw.rect(gameDisplay, buttonColor, p.Rect(int(DISPLAY_WIDTH/2 +10),int(DISPLAY_HEIGHT/2),100,40))
        textSurf, textRect = text_objects("Play", modeText)
        textRect.center = ((int(DISPLAY_WIDTH/2 + 60)), int((DISPLAY_HEIGHT/2 + 20)))
        gameDisplay.blit(textSurf, textRect)

        #add Home Button
        largeText = p.font.Font('freesansbold.ttf',15)
        TextSurf, TextRect = text_objects("Home", largeText)
        TextRect.left = 0
        gameDisplay.blit(TextSurf, TextRect)

        p.display.update()
    if nextMode == 1:
        gameMenu()
    if nextMode == 2:
        classicMode()
    if nextMode == 3:
        mazeMode()

def gameMenu():
    nextMode = 1
    active = True
    while active:

        active = preReqs()
        keys=p.key.get_pressed()
        cursorX = p.mouse.get_pos()[0]
        cursorY = p.mouse.get_pos()[1]
        click = p.mouse.get_pressed()[0]

        if keys[K_c]:
            print("Manual Override. Something must've went wrong or your just a pro-debugger")
            active = False
        gameDisplay.fill((200,200,200))
        #add backround rectangles
        if((cursorX > DISPLAY_WIDTH - 50 and cursorX < DISPLAY_WIDTH - 5) and (cursorY > 0 and cursorY < 20) and click):
            nextMode = 0 #return to main menu
        if((cursorX > DISPLAY_WIDTH/2 - 100 and cursorX < DISPLAY_WIDTH/2) and (cursorY > DISPLAY_HEIGHT/2 and cursorY < DISPLAY_HEIGHT/2 + 40) and click):
            nextMode = 2 #enter classic Mode
        if((cursorX > 10 and cursorX < 260) and (cursorY > 40 and cursorY < 65) and click):
            nextMode = 3 #enter coin Mode
        if((cursorX > 10 and cursorX < 260) and (cursorY > 75 and cursorY < 100) and click):
            nextMode = 4 #enter maze Mode
        if((cursorX > 10 and cursorX < 260) and (cursorY > 115 and cursorY < 145) and click):
            nextMode = 5 #enter gemotry Mode
        if nextMode != 1:
            active = False

        #add Title
        title = p.font.Font('/System/Library/Fonts/Supplemental/Chalkboard.ttc', 20)
        TextSurf, TextRect = text_objects("Game Directory", title)
        TextRect.left = 10
        TextRect.top = 10
        gameDisplay.blit(TextSurf, TextRect)

        #add button for games
        modeText = p.font.Font('/System/Library/Fonts/Supplemental/Chalkboard.ttc', 20)

        boxX = 10
        boxY = 40
        boxWidth = 250
        boxHeight =  25

        for mode in gameModes:
            p.draw.rect(gameDisplay,buttonColor, p.Rect(boxX, boxY, boxWidth, boxHeight))
            textSurf, textRect = text_objects(mode, modeText)
            textRect.center = (130, boxY + 11)
            gameDisplay.blit(textSurf, textRect)
            boxY = boxY + 35

        #add Home Button
        largeText = p.font.Font('freesansbold.ttf',15)
        TextSurf, TextRect = text_objects("Home", largeText)
        TextRect.right = DISPLAY_WIDTH - 5
        gameDisplay.blit(TextSurf, TextRect)

        p.display.update()
    if nextMode == 0:
        mainMenu()
    if nextMode == 2:
        classicMode()
    if nextMode == 3:
        coinMode()
    if nextMode == 4:
        mazeMode()
    if nextMode == 5:
        geometryGuesser()


def classicMode():
    x = DISPLAY_WIDTH-(RESCALE_W/2)+17
    y = DISPLAY_HEIGHT-(RESCALE_H/2)+24
    vel=3
    counter = 0
    run = True
    forward = True
    upward = False
    goMain = False
    while run:
     gameDisplay.fill((255,255,255))

     #add Home Button
     largeText = p.font.Font('freesansbold.ttf',15)
     TextSurf, TextRect = text_objects("Home", largeText)
     TextRect.left = 0
     gameDisplay.blit(TextSurf, TextRect)


     seconds=(p.time.get_ticks()-start_ticks)/1000 #calculate how many seconds

     for event in p.event.get():
       if event.type == p.QUIT:
         run =False
     keys=p.key.get_pressed()
     cursorX = p.mouse.get_pos()[0]
     cursorY = p.mouse.get_pos()[1]
     click = p.mouse.get_pressed()[0]
     #print(K_c)

     if keys[K_c]:
         print("Manual Override. Something must've went wrong or your just a pro-debugger")
         run = False

     if forward and upward:
         x+=vel
         y-=vel

     if forward and not upward:
         x+=vel
         y+=vel

     if not forward and upward:
         x-=vel
         y-=vel

     if not forward and not upward:
         x-=vel
         y+=vel

     if x > DISPLAY_WIDTH-(RESCALE_W/2)+17: #Right
          forward = False

     if x < RESCALE_W/2-17: #Left
          forward = True

     if y > DISPLAY_HEIGHT-(RESCALE_H/2)+24:
          upward = True

     if y < (RESCALE_H/2)-24: #Top
          upward = False

     if seconds > 10:
         #vel = vel + 1;
         seconds = 0;
     if keys[p.K_LEFT]:
          forward = False
     if keys[p.K_RIGHT]:
          forward = True
     if keys[p.K_UP]:
          upward = True
     if keys[p.K_DOWN]:
          upward = False
     if (x == DISPLAY_WIDTH-(RESCALE_W/2)+17 and y == DISPLAY_HEIGHT-(RESCALE_H/2)+24) or (x == DISPLAY_WIDTH-(RESCALE_W/2)+17 and y == (RESCALE_H/2)-24) or (x == RESCALE_W/2-17 and y == DISPLAY_HEIGHT-(RESCALE_H/2)+24) or (x == RESCALE_W/2-17 and y == (RESCALE_H/2)-24):
         counter+=1
         print(counter)

     if((cursorX > 0 and cursorX < 50) and (cursorY > 0 and cursorY < 50) and click):
         print("We go home now.")
         goMain = True
         run = False

     img(x-50,y-50)

     p.display.update()

     if goMain == True:
         mainMenu()

def coinMode():
    #set needed vars
    start_ticks = p.time.get_ticks()
    x = DISPLAY_WIDTH-(RESCALE_W/2)+17
    y = DISPLAY_HEIGHT-(RESCALE_H/2)+24
    randomX = random.randint(50,DISPLAY_WIDTH-50)
    randomY = random.randint(50,DISPLAY_HEIGHT-50)
    c = Coin(randomX,randomY,5,False)
    vel=3
    counter, collected = 0,0
    run = False
    forward = True
    upward = False
    goMain, gotGrabbed = False, False
    while not run:
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False

        keys=p.key.get_pressed()
        gameDisplay.fill((255,255,255))

        #add Tutorial
        largeText = p.font.Font('freesansbold.ttf',15)
        TextSurf, TextRect = text_objects("The goal of Coin Collect is in the name! Collect as many coins before time runs out.", largeText)
        TextRect.center = (DISPLAY_WIDTH/2,DISPLAY_HEIGHT-8)
        gameDisplay.blit(TextSurf, TextRect)

        output_string = "Time Left: {0:02}".format(60)
        text = font.render(output_string, True, black)
        gameDisplay.blit(text, [370, 0])

        if keys[K_x]:
            run = True
            seconds = 0

        if keys[K_c]:
            print("Manual Override. Something must've went wrong or your just a pro-debugger")
            run = True

        if keys[K_p]:
            print("Time to start")
            run = True

        p.display.update()

    while run:
        #white background
        gameDisplay.fill((255,255,255))

        #add Home Button
        largeText = p.font.Font('freesansbold.ttf',15)
        TextSurf, TextRect = text_objects("Home", largeText)
        TextRect.left = 0
        gameDisplay.blit(TextSurf, TextRect)

        #add coin at 10 seconds
        seconds=int((p.time.get_ticks()-start_ticks)/1000) #calculate how many seconds

        output_string = "Coins Collected: {0:02}".format(collected)
        text = font.render(output_string, True, black)
        gameDisplay.blit(text, [640, 430])
        output_string = "Time Left: {0:02}".format(60-seconds)
        text = font.render(output_string, True, black)
        gameDisplay.blit(text, [370, 0])
        #print(c.visible)
        if seconds % 5 == 0 and seconds > 1:
            c.visible = True# = Coin(randomX,randomY,5,True)

        if c.visible == True:
            p.draw.circle(gameDisplay, (122,12,11), (randomX - c.radius,randomY - c.radius), 20)
        if(x > randomX-50 and x < randomX+50) and (y > randomY-45 and y < randomY+35):
            collected += 1
            c.visible = False
            randomX = random.randint(0,DISPLAY_WIDTH)
            randomY = random.randint(0,DISPLAY_HEIGHT)

        for event in p.event.get():
            if event.type == p.QUIT:
                run = False

        keys=p.key.get_pressed()
        cursorX = p.mouse.get_pos()[0]
        cursorY = p.mouse.get_pos()[1]
        click = p.mouse.get_pressed()[0]
        #print(K_c)

        if keys[K_c]:
            print("Manual Override. Something must've went wrong or your just a pro-debugger")
            vel = vel - 0.1
            #run = False
        if forward and upward:
            x+=vel
            y-=vel
        if forward and not upward:
            x+=vel
            y+=vel
        if not forward and upward:
            x-=vel
            y-=vel
        if not forward and not upward:
            x-=vel
            y+=vel

        if x > DISPLAY_WIDTH-(RESCALE_W/2)+17: #Right
            forward = False
        if x < RESCALE_W/2-17: #Left
            forward = True
        if y > DISPLAY_HEIGHT-(RESCALE_H/2)+24:
            upward = True
        if y < (RESCALE_H/2)-24: #Top
            upward = False

        if keys[p.K_LEFT]:
            forward = False
        if keys[p.K_RIGHT]:
            forward = True
        if keys[p.K_UP]:
            upward = True
        if keys[p.K_DOWN]:
            upward = False

        if((cursorX > 0 and cursorX < 50) and (cursorY > 0 and cursorY < 50) and click):
            print("We go home now.")
            goMain = True
            run = False
        if seconds > 60:
            run = False
            endScene = True

        img(x-50,y-50)

        p.display.update()

    while endScene:
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False

        keys=p.key.get_pressed()
        cursorX = p.mouse.get_pos()[0]
        cursorY = p.mouse.get_pos()[1]
        click = p.mouse.get_pressed()[0]

        gameDisplay.fill((255,255,255))

        p.draw.rect(gameDisplay,buttonColor, p.Rect(int(DISPLAY_WIDTH/2 - 100),int(DISPLAY_HEIGHT/2+30),100,40))
        modeText = p.font.Font('/System/Library/Fonts/Supplemental/Chalkboard.ttc', 20)
        textSurf, textRect = text_objects("Home", modeText)
        textRect.center = (int((DISPLAY_WIDTH/2 - 50)), int((DISPLAY_HEIGHT/2 + 50)))
        gameDisplay.blit(textSurf, textRect)

        p.draw.rect(gameDisplay, buttonColor, p.Rect(int(DISPLAY_WIDTH/2 +10),int(DISPLAY_HEIGHT/2+30),100,40))
        textSurf, textRect = text_objects("Replay", modeText)
        textRect.center = ((int(DISPLAY_WIDTH/2 + 60)), int((DISPLAY_HEIGHT/2 + 50)))
        gameDisplay.blit(textSurf, textRect)

        output_string = "Final Score: {0:02}".format(collected)
        text = font.render(output_string, True, black)
        gameDisplay.blit(text, [DISPLAY_WIDTH/2-50,DISPLAY_HEIGHT/2])

        largeText = p.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("Game Over!", largeText)
        TextRect.center = (DISPLAY_WIDTH/2,DISPLAY_HEIGHT/2-70)
        gameDisplay.blit(TextSurf, TextRect)

        if keys[K_x]:
            run = True
            seconds = 0

        if keys[K_c]:
            print("Manual Override. Something must've went wrong or your just a pro-debugger")
            run = True

        if keys[K_p]:
            print("Time to start")
            run = True

        if((cursorX > DISPLAY_WIDTH/2 - 100 and cursorX < DISPLAY_WIDTH/2) and (cursorY > DISPLAY_HEIGHT/2+30 and cursorY < DISPLAY_HEIGHT/2 +70) and click):
            goMain = True
            endScene = False
        if((cursorX > DISPLAY_WIDTH/2 + 10 and cursorX < DISPLAY_WIDTH/2 + 110) and (cursorY > DISPLAY_HEIGHT/2+30 and cursorY < DISPLAY_HEIGHT/2 +70) and click):
            goMain = True
            endScene = False
        p.display.update()

    if goMain == True:
     mainMenu()

def mazeMode():
    #set needed vars
    start_ticks = p.time.get_ticks()
    x = DISPLAY_WIDTH-(RESCALE_W/2)+17
    y = DISPLAY_HEIGHT-(RESCALE_H/2)+24
    randomX = random.randint(0,DISPLAY_WIDTH)
    randomY = random.randint(0,DISPLAY_HEIGHT)
    c = Coin(randomX,randomY,5,False)
    w = Wall(randomX,randomX-2,randomX+2,10,4,True)
    vel=2
    counter = 0
    run, preview = True, True
    forward = True
    upward = False
    goMain, gotGrabbed = False, False
    # while preview:
    #     #white background
    #     gameDisplay.fill((255,255,255))
    #
    #     #add Home Button
    #     largeText = p.font.Font('freesansbold.ttf',15)
    #     TextSurf, TextRect = text_objects("Home", largeText)
    #     TextRect.left = 0
    #     gameDisplay.blit(TextSurf, TextRect)
    #
    #     keys=p.key.get_pressed()
    #     cursorX = p.mouse.get_pos()[0]
    #     cursorY = p.mouse.get_pos()[1]
    #     click = p.mouse.get_pressed()[0]
    #
    #     if((cursorX > 0 and cursorX < 50) and (cursorY > 0 and cursorY < 50) and click):
    #         run = True
    #         preview = False
    #
    #     for event in p.event.get():
    #         if event.type == p.QUIT:
    #             preview = False
    #
    #     p.display.update()

    while run:
        #white background
        gameDisplay.fill((255,255,255))

        #add Home Button
        largeText = p.font.Font('freesansbold.ttf',15)
        TextSurf, TextRect = text_objects("Home", largeText)
        TextRect.left = 0
        gameDisplay.blit(TextSurf, TextRect)

        #add coin at 10 seconds
        seconds=int((p.time.get_ticks()-start_ticks)/1000) #calculate how many seconds

        #WALL SECTION
        if w.visible == True:
            p.draw.line(gameDisplay, (122,11,132), (randomX,0), (randomX, w.length),width=4)

        p.draw.line(gameDisplay, (122,11,132), (20,0), (100, w.length),width=4)
        p.draw.line(gameDisplay, (122,11,132), (60,0), (200, w.length),width=4)
        p.draw.line(gameDisplay, (122,11,132), (100,0), (300, w.length),width=4)
        p.draw.line(gameDisplay, (122,11,132), (140,0), (400, w.length),width=4)

        if seconds % 5 == 0 and seconds > 1:
            c.visible = True# = Coin(randomX,randomY,5,True)
        if c.visible == True:
            p.draw.circle(gameDisplay, (122,12,11), (randomX - c.radius,randomY - c.radius), 20)
        if(x > randomX-10 and x < randomX+10) and (y > randomY-10 and y < randomY+10):
            c.visible = False

        for event in p.event.get():
            if event.type == p.QUIT:
                run = False

        keys=p.key.get_pressed()
        cursorX = p.mouse.get_pos()[0]
        cursorY = p.mouse.get_pos()[1]
        click = p.mouse.get_pressed()[0]

        #border conditions
        if x > DISPLAY_WIDTH-(RESCALE_W/2)+17: #Right
            forward = False

        if x < RESCALE_W/2-17: #Left
            forward = True

        if y > DISPLAY_HEIGHT-(RESCALE_H/2)+24:
            upward = True

        if y < (RESCALE_H/2)-24: #Top
            upward = False

        #special wall conditions
        #if right side of the logo hits the wall, switch to fors False
        if x + (RESCALE_W/2)-12 > w.lx and x + (RESCALE_W/2)-12 < w.rx and y < w.length+22:
            forward = False

        if x - (RESCALE_W/2)+12 < w.rx and x - (RESCALE_W/2)+12 > w.lx and y < w.length+22:
            forward = True

        if y-24 < w.length and x > (w.x - 30) and x < (w.x + 30):
            upward = False

        if keys[K_f]:
            vel = vel * 2
            time.sleep(1)

        if keys[K_s]:
            vel = vel / 2
            time.sleep(1)

        if keys[K_c]:
            print("Manual Override. Something must've went wrong or you're just a pro-debugger")
            run = False

        if keys[K_h]:
            print("Manual Override. Something must've went wrong or you're just a pro-debugger")
            goMain = True
            run = False

        if forward and upward:
            x+=vel
            y-=vel

        if forward and not upward:
            x+=vel
            y+=vel

        if not forward and upward:
            x-=vel
            y-=vel

        if not forward and not upward:
            x-=vel
            y+=vel

        if keys[p.K_LEFT]:
            forward = False
        if keys[p.K_RIGHT]:
            forward = True
        if keys[p.K_UP]:
            upward = True
        if keys[p.K_DOWN]:
            upward = False
        if (x == DISPLAY_WIDTH-(RESCALE_W/2)+17 and y == DISPLAY_HEIGHT-(RESCALE_H/2)+24) or (x == DISPLAY_WIDTH-(RESCALE_W/2)+17 and y == (RESCALE_H/2)-24) or (x == RESCALE_W/2-17 and y == DISPLAY_HEIGHT-(RESCALE_H/2)+24) or (x == RESCALE_W/2-17 and y == (RESCALE_H/2)-24):
            counter+=1
            print(counter)

        if((cursorX > 0 and cursorX < 50) and (cursorY > 0 and cursorY < 50) and click):
            print("We go home now.")
            goMain = True
            run = False

        img(x-50,y-50)

        p.display.update()

    if goMain == True:
     mainMenu()

def geometryGuesser():
    #set needed vars
    start_ticks = p.time.get_ticks()
    x = DISPLAY_WIDTH-(RESCALE_W/2)+17
    y = DISPLAY_HEIGHT-(RESCALE_H/2)+24
    randomX = random.randint(0,DISPLAY_WIDTH)
    randomY = random.randint(0,DISPLAY_HEIGHT)
    c = Coin(randomX,randomY,5,False)
    w = Wall(randomX,randomX-2,randomX+2,10,4,True)
    wallHits, vel, counter = 0, 2, 0
    run = False
    forward, upward = True, False
    goMain, gotGrabbed = False, False
    guess = 111
    endScreen = False
    #starting positions for object
    obStartX = random.randint(50,100)
    obStartY = random.randint(50,100)
    x = obStartX
    y = obStartY
    yHoleStart = random.randint(0,300)
    yHoleEnd = yHoleStart + 200
    while not run:
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False

        keys=p.key.get_pressed()
        gameDisplay.fill((255,255,255))

        #add Tutorial
        largeText = p.font.Font('freesansbold.ttf',15)
        TextSurf, TextRect = text_objects("Enter a number or + if it's more than 9!", largeText)
        TextRect.center = (DISPLAY_WIDTH/2,DISPLAY_HEIGHT-8)
        gameDisplay.blit(TextSurf, TextRect)

        if keys[K_0]: run,guess = True, 0
        if keys[K_1]: run,guess = True, 1
        if keys[K_2]: run,guess = True, 2
        if keys[K_3]: run,guess = True, 3
        if keys[K_4]: run,guess = True, 4
        if keys[K_5]: run,guess = True, 5
        if keys[K_6]: run,guess = True, 6
        if keys[K_7]: run,guess = True, 7
        if keys[K_8]: run,guess = True, 8
        if keys[K_9]: run,guess = True, 9
        if keys[K_x]: run,guess = True, 111

        if keys[K_c]:
            print("Manual Override. Something must've went wrong or your just a pro-debugger")
            run = True

        if keys[K_p]:
            print("Time to start")
            run = True

        p.draw.line(gameDisplay, (122,11,132), (randomX,0), (randomX, DISPLAY_HEIGHT),width=4)
        p.draw.line(gameDisplay, (255,255,255), (randomX,yHoleStart), (randomX, yHoleEnd), width=4)

        img(x-50,y-50)

        p.display.update()

    while run:
        seconds=int((p.time.get_ticks()-start_ticks)/1000) #calculate how many seconds

        #white background
        gameDisplay.fill((255,255,255))

        #add Home Button
        largeText = p.font.Font('freesansbold.ttf',15)
        TextSurf, TextRect = text_objects("Home", largeText)
        TextRect.left = 0
        gameDisplay.blit(TextSurf, TextRect)

        # #add WallHit counter
        largeText = p.font.Font('freesansbold.ttf',15)
        TextSurf, TextRect = text_objects(wallHits, largeText)
        TextRect.left = DISPLAY_WIDTH/2
        gameDisplay.blit(TextSurf, TextRect)

        #WALL SECTION
        p.draw.line(gameDisplay, (122,11,132), (randomX,0), (randomX, w.length),width=4)

        p.draw.line(gameDisplay, (122,11,132), (randomX,0), (randomX, DISPLAY_HEIGHT),width=4)
        p.draw.line(gameDisplay, (255,255,255), (randomX,yHoleStart), (randomX, yHoleEnd), width=4)

        for event in p.event.get():
            if event.type == p.QUIT:
                run = False

        keys=p.key.get_pressed()
        cursorX = p.mouse.get_pos()[0]
        cursorY = p.mouse.get_pos()[1]
        click = p.mouse.get_pressed()[0]

        if x > w.x + (RESCALE_W/2)+17: #Right
            run = False
            endScreen = True
        if x < RESCALE_W/2-17: #Left
            forward = True
            wallHits += 1
        if y > DISPLAY_HEIGHT-(RESCALE_H/2)+24:
            upward = True
            wallHits += 1
        if y < (RESCALE_H/2)-24: #Top
            upward = False
            wallHits += 1

        #special wall conditions
        if x + (RESCALE_W/2)-12 > w.lx and x + (RESCALE_W/2)-12 < w.rx and y < yHoleStart+22:
            forward = False
            wallHits += 1
        if x - (RESCALE_W/2)+12 < w.rx and x - (RESCALE_W/2)+12 > w.lx and y < yHoleStart+22:
            forward = True
            wallHits += 1
        if y-24 < yHoleStart and x > (w.x - 30) and x < (w.x + 30):
            upward = False
            wallHits += 1

        if x + (RESCALE_W/2)-12 > w.lx and x + (RESCALE_W/2)-12 < w.rx and y > yHoleEnd-22:
            forward = False
            wallHits += 1
        if x - (RESCALE_W/2)+12 < w.rx and x - (RESCALE_W/2)+12 > w.lx and y > yHoleEnd-22:
            forward = True
            wallHits += 1
        if y+24 > yHoleEnd and x > (w.x - 30) and x < (w.x + 30):
            upward = True
            wallHits += 1

        if keys[K_f]:
            vel = vel * 2
            time.sleep(1)

        if keys[K_s]:
            vel = vel / 2
            time.sleep(1)

        if keys[K_c]:
            print("Manual Override. Something must've went wrong or your just a pro-debugger")
            run = False

        if keys[K_h]:
            print("Manual Override. Something must've went wrong or your just a pro-debugger")
            goMain = True
            run = False

        if forward and upward:
            x+=vel
            y-=vel

        if forward and not upward:
            x+=vel
            y+=vel

        if not forward and upward:
            x-=vel
            y-=vel

        if not forward and not upward:
            x-=vel
            y+=vel

        if keys[p.K_LEFT]:
            forward = False
        if keys[p.K_RIGHT]:
            forward = True
        if keys[p.K_UP]:
            upward = True
        if keys[p.K_DOWN]:
            upward = False
        if (x == DISPLAY_WIDTH-(RESCALE_W/2)+17 and y == DISPLAY_HEIGHT-(RESCALE_H/2)+24) or (x == DISPLAY_WIDTH-(RESCALE_W/2)+17 and y == (RESCALE_H/2)-24) or (x == RESCALE_W/2-17 and y == DISPLAY_HEIGHT-(RESCALE_H/2)+24) or (x == RESCALE_W/2-17 and y == (RESCALE_H/2)-24):
            counter+=1
            print(counter)

        if((cursorX > 0 and cursorX < 50) and (cursorY > 0 and cursorY < 50) and click):
            print("We go home now.")
            goMain = True
            run = False

        img(x-50,y-50)

        p.display.update()

    while endScreen:
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False

        keys=p.key.get_pressed()
        cursorX = p.mouse.get_pos()[0]
        cursorY = p.mouse.get_pos()[1]
        click = p.mouse.get_pressed()[0]

        gameDisplay.fill((255,255,255))

        #add Home Button
        largeText = p.font.Font('freesansbold.ttf',15)
        TextSurf, TextRect = text_objects("Home", largeText)
        TextRect.left = 0
        gameDisplay.blit(TextSurf, TextRect)
        if((cursorX > 0 and cursorX < 50) and (cursorY > 0 and cursorY < 50) and click):
            goMain, endScreen = True, False

        if (wallHits == guess) or (wallHits > 9 and guess == 111):
            #add Win text
            largeText = p.font.Font('freesansbold.ttf',60)
            TextSurf, TextRect = text_objects("You Won!", largeText)
            TextRect.center = (DISPLAY_WIDTH/2,DISPLAY_HEIGHT/2)
            gameDisplay.blit(TextSurf, TextRect)
        else:
            #add Lose text
            largeText = p.font.Font('freesansbold.ttf',60)
            TextSurf, TextRect = text_objects("You Lost :(", largeText)
            TextRect.center = (DISPLAY_WIDTH/2,DISPLAY_HEIGHT/2)
            gameDisplay.blit(TextSurf, TextRect)

        p.display.update()

    if goMain == True:
     mainMenu()

#mode = {0 : mainMenu, 1 : classicMode}

    #
    # if mode == 1:
    #     #print("In 1")
    #     classicMode()
    # #elif mode == 2:
    #     #coinMode()


mainMenu()

p.quit()


###Game Mode: Corners Hit counter. Based on timer, shows score at the end.
