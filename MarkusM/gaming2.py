from operator import indexOf
import pygame as pg
import random as r
import sys, time
import os
from pygame.locals import *

pg.init() #starter pygame

window_width = 1080
window_height = 720
window = pg.display.set_mode([window_width,window_height],pg.RESIZABLE)
pg.display.set_caption('gaming')
font = pg.font.SysFont("Arial", 24)

gifList = []
keyIndex = 0

#acceptedKeys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def keyCheck():
    if keyList.count(str(id)) == True:
        return True
def findKeyID():
    return True

    

class key:
    def __init__(self,key,pressed):
        self.key = key
        self.pressed = pressed

    def keyPress(self):
        self.pressed = True

    def keyUp(self):
        self.pressed = False

keyInit = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","æ","ø","å"]
keyList = []
#SpecialKeys = ["Return","Backspace"]

for i in range(len(keyInit)):
    keyList.append(key(keyInit[i],False))

for i in range(44):
    gifList.append(pg.image.load(f"MarkusM/gif_test/breaking-bad-money-{i}.png"))



#fps
clock = pg.time.Clock() 
"""
currentFps = 0
averageFps = 0
frames_counter = 0
typetest = []
keypressed = False

def fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, True, (0,0,0))
	return fps_text


"""
typetest = str()

while True: #displayLoop

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        
        if event.type == pg.KEYDOWN:
            try:
                i = keyInit.index(pg.key.name(event.key))
                typetest += keyList[i].key
                print(typetest)

            except:
                pass
            if event.key == pg.K_RETURN:
                typetest = str()

            if event.key == pg.K_BACKSPACE:
                typetest = typetest[0:-1]
            if event.key == pg.K_SPACE:
                typetest = typetest + str(" ")
            
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
    window.blit(font.render(str(typetest),True,(0,0,0)),(20,200)) 



    clock.tick(24)
    pg.display.flip()

    

#https://www.cleverpdf.com/gif-to-png