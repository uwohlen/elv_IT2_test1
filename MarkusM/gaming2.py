from re import S
from turtle import circle, width
import pygame as pg
import random as r
import sys, time
import os
from pygame.locals import *
import math as math

try:
    from PIL import Image, ImageDraw
except:
    sys.exit("PIL trengs for å kjøre spillet. pip (pip3 på mac) install pillow, eller pip -U install pillow --user")

pg.init() #starter pygame

window_width = 1080
window_height = 720
window = pg.display.set_mode([window_width,window_height],pg.RESIZABLE)
#window = pg.display.set_mode([window_width,window_height],FULLSCREEN)
pg.display.set_caption('gaming')
font = pg.font.Font("MarkusM/font_test/coolvetica rg.otf", 40)
font2 = pg.font.Font("MarkusM/font_test/coolvetica rg.otf", 80)
menyFont = pg.font.Font("MarkusM/font_test/MADE TOMMY Black_PERSONAL USE.otf",80)
timerFont = pg.font.Font("MarkusM/font_test/MADE TOMMY Regular_PERSONAL USE.otf",80)

gifList = []
keyIndex = 0

#acceptedKeys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
keyInit = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","æ","ø","å"]

for i in range(44):
    gifList.append(pg.image.load(f"MarkusM/gif_test/breaking-bad-money-{i}.png"))

#farger
black = (0,0,0)
red = (200,0,0)
green = (100,200,100)
grey = (100,100,100)
light_grey = (220,220,220)

#fps
clock = pg.time.Clock() 

#lyder
SoundEffectChannel = pg.mixer.Channel(1)
SoundEffectChannel2 = pg.mixer.Channel(2)
MusicChannel = pg.mixer.Channel(3)

"""
currentFps = 0
averageFps = 0
frames_counter = 0
typetest = []

def fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, True, (0,0,0))
	return fps_text
"""


windowFPS = 60 #hvor mange frames pr sekund som blir rendera

def typeGame():
    answerTime = 6
    typeMusic = pg.mixer.Sound(f"MarkusM/sounds/main_music.wav")
    typeMusic.set_volume(0.5)
    MusicChannel.play(typeMusic)

    counter = 0
    typetest = str()
    task = ["Kul","Hei","Onomatepoetikon","Iridocyclitis","Diabolical","Pneumonoultramicroscopicsilicovolcanoconiosis", "   "]    
    tasknr = 0
    timerPlayed = False
    sec = 0
    timer = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                try:
                    keys = pg.key.get_pressed()
                    if keys[K_LSHIFT]:
                        i = keyInit.index(pg.key.name(event.key))
                        typetest += keyInit[i].upper()

                    else:
                        i = keyInit.index(pg.key.name(event.key))
                        typetest += keyInit[i]
                        #print(typetest) #teste om stringen oppdaterer seg som den skal

                except:
                    pass
                if event.key == pg.K_RETURN:
                    pg.mixer.Sound.stop

                    if typetest == task[tasknr]:
                        tasknr +=1
                        typetest = str()
                        SoundEffectChannel.stop()
                        win = pg.mixer.Sound(f"MarkusM/sounds/win_{r.randint(0,2)}.wav")
                        SoundEffectChannel.play(win)
                        timerPlayed = False
                        sec = 0
                        timer = 0
                        #spill funny sound effect
                    else:
                        #spill funny sound effect
                        SoundEffectChannel.stop()
                        fail = pg.mixer.Sound(f"MarkusM/sounds/fail_{r.randint(0,2)}.wav")
                        SoundEffectChannel.play(fail)
                        pass

                if event.key == pg.K_BACKSPACE:
                    typetest = typetest[0:-1]

                    #hvis man holder i fler frames, sletter den fortere
                if event.key == pg.K_SPACE:
                    typetest = typetest + str(" ")
                
                if event.key ==pg.K_ESCAPE:
                    sys.exit()

            #finne hvilken som er trykket

        #if event.type == pg.KEYUP:
        #    pass
            #keyList[event.key].keyUp
                #finne hvilken som er trykket

    #frames_counter +=1
    #if frames_counter == 61 or frames_counter >= 61:
    #    frames_counter =0
    #if frames_counter <= 60 and frames_counter >=30:
    #    window.fill((135,206,235))
    #else:
    #    window.fill((0,0,0))
    #print(frames_counter)

    #if frames_counter == 44:
    #    frames_counter =0

        window.fill((255,255,255))
    #window.blit(gifList[frames_counter],(0,0))
    
    #frames_counter +=1

        
    #window.blit(font.render(str(frames_counter),True,(0,0,0)),(400,20))
    #if now > 0 and not now < 30:
    #    window.fill((0,0,0))
    #else:

    #window.blit(fps(),(20,20))

    #for i in range(len(typetest)):
    #    window.blit(font.render(str(typetest[i]),True,(0,0,0)),(10*i,200))

    #typerender
        taskRender = font.render(str(task[tasknr]),True,(0,0,0))
        taskRect = taskRender.get_rect(center=((window_width/2),(window_height/2)-200))
        window.blit(taskRender,taskRect)

        typeText = font.render(str(typetest),True,(0,0,0))
        typeRect = typeText.get_rect(center=(window_width/2,window_height/2))


        for i in range(len(typetest)):

            textprev = font.render(str(typetest[0:i]),True,(0,0,0)) #finne lengde av teksten før
            textPrevLength = textprev.get_width() #lagre lengden
            charPosx, charPosy = typeRect.midleft #lagre koordiatene til rektangelet

            try:
                if not typetest[i] == task[tasknr][i]:
                    charRender = font.render(str(typetest[i]),True,red)
                    window.blit(charRender,((charPosx+textPrevLength,charPosy)))
            
                else:
                    charRender = font.render(str(typetest[i]),True,green)
                    window.blit(charRender,((charPosx + textPrevLength),charPosy))
            except:
                charRender = font.render(str(typetest[i]),True,red)
                window.blit(charRender,((charPosx+textPrevLength,charPosy)))
        
    
    #timerender
        if timer > 300 and timerPlayed == False:
            SoundEffectChannel.stop()
            clock_tick = pg.mixer.Sound(f"MarkusM/sounds/clock_tick.wav")
            SoundEffectChannel2.play(clock_tick)
            timerPlayed = True

        if timer <360: #tegne sirkel når man har tid igjen

            pil_size = 450
            pil_image = Image.new("RGBA",(pil_size,pil_size))
            pil_draw = ImageDraw.Draw(pil_image)

            #pil_image2 = Image.new("RGBA",(pil_size,pil_size))
            #pil_draw2 = ImageDraw.Draw(pil_image2)

            pil_draw.pieslice((0,0,pil_size-1,pil_size-1),360,359-timer,fill=light_grey) #definere sirkel
            #pil_draw2.pieslice((0,0,pil_size-1,pil_size-1),0,360,fill=light_grey)

            circleMode = pil_image.mode
            circleSize = pil_image.size
            circleData = pil_image.tobytes()
            circleDraw = pg.image.fromstring(circleData,circleSize,circleMode) #gjøre om fra PIL til pygame

            #circleMode2 = pil_image2.mode
            #circleSize2 = pil_image2.size
            #circleData2 = pil_image2.tobytes()
            #circleDraw2 = pg.image.fromstring(circleData2,circleSize2,circleMode2) #gjøre om fra PIL til pygame

            circleDraw = pg.transform.rotozoom(circleDraw,90,1/3) #downscale for å få bedre kvalitet og rotere
            #circleDraw2 = pg.transform.rotozoom(circleDraw2,0,1/3)

            circlerect = circleDraw.get_rect(center=((window_width/2),(window_height/2)+200))
            #window.blit(circleDraw2,circlerect)
            window.blit(circleDraw,circlerect) #tegne sirkelen

            timerRender = timerFont.render(str(round((answerTime-sec),1)),True,green)
            timerRect = timerRender.get_rect(center=((window_width/2),(window_height/2)+200))
            window.blit(timerRender,timerRect) #tegne timer
        else:
            timerRender = timerFont.render(str(round((answerTime-sec),1)),True,red)
            timerRect = timerRender.get_rect(center=((window_width/2),(window_height/2)+200))
            window.blit(timerRender,timerRect) #tegne timer

        clock.tick(windowFPS) #Oppdaterer skjermen og teller hvilken frame vi er på
        pg.display.flip() 

        counter +=1
        sec += 1/windowFPS
        #print(counter)
        #if counter == windowFPS:
        #    sec +=1
        #    counter = 0
        if timer == 360 or timer > 360:
            gameFail()
            break
        timer += (360/windowFPS)/answerTime #for å kontrolerer tid

def menu():

    loop = True
    while loop:
        if MusicChannel.get_busy() == False:
            menuMusic = pg.mixer.Sound(f"MarkusM/sounds/MenuMusic.mp3")
            menuMusic.set_volume(0.5)
            MusicChannel.play(menuMusic)
            
        #quitButton = pg.draw.rect(window, (0, 255, 0), (200, 250, 70, 90))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                left,middle,right = pg.mouse.get_pressed()
                mousepos = pg.mouse.get_pos()
                if left:
                    if quitBox.collidepoint(mousepos):
                        sys.exit()
                    if startBox.collidepoint(mousepos):
                        loop = False
                

                
            if event.type == KEYDOWN:
                if event.key ==pg.K_ESCAPE:
                    sys.exit()
        window.fill((255,255,255))

        centerx,centery = findCenter() #finne senter av skjermen

        quitBox = pg.Rect(0,0,window_width/3,window_height/6) #definere rekangel
        quitBox.center = (centerx+window_width/4,centery) #posisjonere rektangel
        pg.draw.rect(window,light_grey,quitBox) #tegne rektangel
        
        quitText = menyFont.render(str("QUIT"),True,black) #definere tekst
        quitTextBox = quitText.get_rect() #definere hvor stor teksten er
        quitTextBox.center = quitBox.center #sentrere teksten i boksen
        window.blit(quitText,quitTextBox) #render

        startBox = pg.Rect(0,0,window_width/3,window_height/6) #definere rekangel
        startBox.center = (centerx-window_width/4,centery) #posisjonere rektangel
        pg.draw.rect(window,light_grey,startBox) #tegne rektangel

        startText = font2.render(str("START"),True,black) #definere tekst
        startTextBox = startText.get_rect() #definere hvor stor teksten er
        startTextBox.center = startBox.center #sentrere teksten i boksen
        window.blit(startText,startTextBox) #render

        #tittel
        title = font2.render(str("GAMING"),True,black) #definere tekst
        titleBox = title.get_rect(center=(window_width/2,(window_height/2)-(window_height/4)))
        window.blit(title,titleBox) #render


        #window.blit(quitBox,(centerPosx-90,centerPosy))
        #window.blit(quitButton, (0,0))

        
        


        pg.display.flip()


def findCenter():
    return window_width/2,window_height/2

def gjettHvor():
    while True:
        pg.display.flip()

def introduction():
    pass

class block:
    def __init__(self,length,centerposx,centerposy):
        self.width = length
        self.height = length
        self.centerposx = centerposx
        self.centerposy = centerposy
        self.rect = pg.Rect(0,0,self.width,self.height)

        
    def safeCollision(self):
        safeLine = pg.Rect(0,0,self.width,1)
        topCoords = self.rect.midtop
        safeLine.midtop = topCoords

        if pg.Rect.colliderect(player.rect,safeLine):
            return True
    
    def harmCollision(self):
        harmLine = pg.Rect(0,0,1,self.height/1.2)
        topCoords = self.rect.midleft
        harmLine.midleft = topCoords

        if pg.Rect.colliderect(harmLine,player.rect):
            return True

    def render(self,levelSpeed,counter):
        self.rect.center = (self.centerposx-(levelSpeed*counter),self.centerposy)

        pg.draw.rect(window,grey,self.rect)
print(math.tan(math.radians(30)))

class triangle:
    def __init__(self,size,centerposx,centerposy):
        self.size = size
        self.centerposx = centerposx
        self.centerposy = centerposy
        self.heightRatio = 1.4

    def draw(self,speed,counter):
        newCenterPosx = self.centerposx -(speed*counter)

        self.leftPoint = newCenterPosx-self.size,self.centerposy
        self.rightPoint = newCenterPosx+self.size,self.centerposy
        self.topPoint = newCenterPosx,self.centerposy-math.tan(math.radians(30))*(self.size*2*self.heightRatio)
        
        self.polygon = pg.draw.polygon(window,grey, ((self.topPoint),(self.leftPoint),(self.rightPoint)))
    
    def harmCollision(self):
        if pg.Rect.colliderect(self.polygon,player.rect): #dårlig collision
            return True

class border:
    def __init__(self,height,width):
        self.height = height
        self.width = width
        self.rect = pg.Rect(0,0,self.width,self.height)

    def render(self):
        global window_width
        global window_width

        self.rect.midbottom = (window_width/2,window_height)
        pg.draw.rect(window,black,self.rect)

    def safeCollision(self):
        global window_width
        global window_height
        safeline = pg.Rect(0,0,self.width,1)
        safeline.midbottom = (window_width/2,window_height-self.height)

        if pg.Rect.colliderect(player.rect,safeline):
            return True
        
def harmcolissionCheck():
    for i in range(len(blockList)):
        if blockList[i].harmCollision():
            return True
    for i in range(len(triangleList)):
        if triangleList[i].harmCollision():
            return True

def safeColissionCheck():
    for i in range(len(blockList)):
        if blockList[i].safeCollision():
            return True
    if lower_border.safeCollision():
        return True
    else:
        return False #ved collision problemer sjekk denne. Kan hende for-løkken ikke stopper etter return
    
    
class player:
    def __init__(self,length,borderHeight):
        global window_width
        global window_height

        self.momentum = 0
        self.length = length
        self.posx = window_width/2
        self.posy = window_height-borderHeight
        #self.safeRect = pg.Rect(0,0,self.length,self.length)

        self.rect = pg.Rect(0,0,self.length,self.length)


    def jump(self):
        self.momentum = 1.5

    def render(self):
        self.posy = self.posy-self.momentum
        self.rect.midbottom = (self.posx,self.posy)
        

        if not safeColissionCheck():
            self.momentum -=0.005
        else:
            self.momentum = 0
        
        pg.draw.rect(window,green,self.rect)
def gdGameOver():
    sys.exit()

borderHeight = 50
player = player(100,borderHeight) #bredde gd blokk
lower_border = border(borderHeight,window_width)
blockList = []
triangleList = []

lvl = """
           xxx^^
"""

x = 0
for char in lvl:
    if char == "x":
        blockList.append(block(100,x*100+1600,window_height-100))
    elif char == "^":
        triangleList.append(triangle(50,x*100+1600,window_height-50))
    x +=1

lvl = """
                x   
"""
x = 0
#          xxx^^
for char in lvl:
    if char == "x":
        blockList.append(block(100,x*100+1600,window_height-200))
    elif char == "^":
        triangleList.append(triangle(50,x*100+1600,window_height-150))
    x +=1

lvl = """
                   ^x
"""

x = 0
for char in lvl:
    if char == "x":
        blockList.append(block(100,x*100+1600,window_height-300))
    elif char == "^":
        triangleList.append(triangle(50,x*100+1600,window_height-250))
    x +=1

lvl = """
            x
"""
x = 0
#          xxx
for char in lvl:
    if char == "x":
        blockList.append(block(100,x*100+1600,window_height-400))
    elif char == "^":
        triangleList.append(triangle(50,x*100+1600,window_height-350))
    x +=1



triangle2 = triangle(50,window_width+200+1080,window_height-borderHeight)
block2 = block(100,window_width+1080,window_height-borderHeight-50)
block3 = block(100,window_width+100+1080,window_height-borderHeight-50)
blockList.append(block2)
blockList.append(block3)
triangleList.append(triangle2)
print(blockList[0].centerposy)
print(block2.centerposy)
print(blockList[0].centerposx)
print(block3.centerposx)
def gd():
    gdMusic = pg.mixer.Sound(f"MarkusM/sounds/gdMusic.mp3")
    gdMusic.set_volume(0.5)
    MusicChannel.play(gdMusic)
    levelSpeed = 0.5
    counter = 0
    background = pg.image.load("MarkusM/images/gdBackground.png")
    while True:
        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            
            if event.type == MOUSEBUTTONDOWN:
                left,middle,right = pg.mouse.get_pressed()
                if left:
                    if safeColissionCheck():
                        player.jump()
        
        window.fill((255,255,255))
        window.blit(background,(0,0))
        #render
        for i in range(len(blockList)):
            blockList[i].render(levelSpeed,counter)
        for i in range(len(triangleList)):
            triangleList[i].draw(levelSpeed,counter)
        lower_border.render()

        player.render()
        pg.display.flip()

        if harmcolissionCheck():
            gdGameOver()

        counter+=1

def gameFail(): 
    SoundEffectChannel.stop()
    fail = pg.mixer.Sound(f"MarkusM/sounds/fail_{r.randint(0,2)}.wav")
    SoundEffectChannel.play(fail)
    MusicChannel.stop()

while True: #displayLoop
    gd()
    #menu()
    #introduction()
    #typeGame()

    #time.sleep(2)

#lavere frame rate gir bedre tid. Endre til at man ganger teller med en mulitplier basert på framerate
#Lage en bakgrunn som beveger seg
#Hvis man klikker et par frames før, hopper karakteren alikavel. En countdown.
#Performance. Lage en løkke som sjekker om elementer er av skjermen, og velger å ikke blitte.

#https://www.cleverpdf.com/gif-to-png
#https://www.dafont.com/top.php