from turtle import circle
import pygame as pg
import random as r
import sys, time
import os
from pygame.locals import *

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
font = pg.font.SysFont("MarkusM/font_test/coolvetica rg.otf", 40)
font2 = pg.font.SysFont("MarkusM/font_test/coolvetica rg.otf", 80)

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


windowFPS = 30 #hvor mange frames pr sekund som blir rendera

def typeGame():
    typeMusic = pg.mixer.Sound(f"MarkusM/sounds/main_music.wav")
    typeMusic.set_volume(0.5)
    MusicChannel.play(typeMusic)

    counter = 0
    typetest = str()
    task = ["Kul","Hei","Onomatepoetikon"," ","Iridocyclitis","Diabolical","Pneumonoultramicroscopicsilicovolcanoconiosis"]    
    tasknr = 0

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

            timerRender = font2.render(str(round(((360/windowFPS)-sec),1)),True,green)
            timerRect = timerRender.get_rect(center=((window_width/2),(window_height/2)+200))
            window.blit(timerRender,timerRect) #tegne timer


        clock.tick(windowFPS) #Oppdaterer skjermen og teller hvilken frame vi er på
        pg.display.flip() 

        timer +=1 #for å kontrolerer tid

        counter +=1
        sec += 1/windowFPS
        #print(counter)
        #if counter == windowFPS:
        #    sec +=1
        #    counter = 0
        if timer == 360:
            gameFail()
            break

def menu():

    loop = True
    while loop:
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
        
        quitText = font2.render(str("QUIT"),True,black) #definere tekst
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

def gd():
    while True:
        pg.display.flip()

def gameFail():
    SoundEffectChannel.stop()
    fail = pg.mixer.Sound(f"MarkusM/sounds/fail_{r.randint(0,2)}.wav")
    SoundEffectChannel.play(fail)
    MusicChannel.stop()

while True: #displayLoop
    menu()
    introduction()
    typeGame()
    time.sleep(2)

#lavere frame rate gir bedre tid. Endre til at man ganger teller med en mulitplier basert på framerate

#https://www.cleverpdf.com/gif-to-png
#https://www.dafont.com/top.php