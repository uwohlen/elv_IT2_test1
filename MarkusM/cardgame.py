import pygame as pg
import random as r
import sys, time
import os
from pygame.locals import *
import math as math

pg.init()

#720p
window_width = 1280
window_height = 720 

#1080p
#window_width = 1920
#window_height = 1080



#window = pg.display.set_mode([window_width,window_height],pg.RESIZABLE,DOUBLEBUF)
window = pg.display.set_mode([window_width,window_height],FULLSCREEN)
window.set_alpha(None)

clock = pg.time.Clock() 

global cardSize
cardwidth = 200
cardheight = 300

cardSize = (cardwidth,cardheight)


windowFPS = 60 #hvor mange frames pr sekund som blir rendera

#farger
black = (0,0,0)
red = (200,0,0)
green = (100,200,100)
grey = (100,100,100)
light_grey = (220,220,220)
gdred = (235, 88, 52)
gdwhite = (100,100,100)
triangleBlue = (1,28,116)


class card():
    def __init__(self,cost,damage):
        self.cost = cost
        self.damage = damage
        self.width,self.height = cardSize
        self.posx = window_width/2
        self.posy = window_height/2
        self.mouseOffset = (0,0)

        self.rect = pg.Rect(0,0,self.width,self.height)
        self.rect.center = (self.posx,self.posy)

    def render(self):
        self.rect.center = (self.posx,self.posy)
        pg.draw.rect(window,grey,self.rect)

    def move(self):
        x,y = pg.mouse.get_pos()
        ox,oy = self.mouseOffset
        self.posx = x+ox
        self.posy = y+oy
        delta = 1.2

        if ox>delta/2+1:
            ox = ox/delta
        elif ox<-(delta+1):
            ox = ox/delta
        else:
            ox = 0
        if oy>delta/2+1:
            oy = oy/delta
        elif oy<-(delta+1):
            oy = oy/delta
        else:
            oy = 0
        self.mouseOffset = (ox,oy)
        #print(self.posx,self.posy)
    
    def moveFinished(self):
        #finne posisjon kortet kan bevege seg til, og flytte det den hvis den er nærme nok. Eller fytte tilbake til hånd
        pass
    def mouseOffsetCheck(self):
        x,y = pg.mouse.get_pos()
        if self.rect.collidepoint((x,y)):
            self.mouseOffset = (self.posx-x,self.posy-y)
            print(self.mouseOffset)
            global cardSelected
            cardSelected = 1
        else:
            cardSelected = None
        #definere differansen mellom posisjonen musen startet, og hvor den flyttet til. Ellers vil den hoppe til senter av musen.


card1 = card(0,0)
global cardSelected
cardSelected = None

#class player():
##    def __init__(self,hp):
#        self.hp = hp
 #       self.deck = []

def cardInterract():
    
    #for elements in kortlist. Lagre verdi
    card1.mouseOffsetCheck()

def cardMove():
    #beveger det listeelementet som ble beveg i cardInterract
    if cardSelected == 1:
        card1.move()

def mouseHover():
    #hvis mus ligger over kort, forstørre kortet. Både for hånd og for kort på bordet
    #Hvis ett kort er higligha allerede, ikke higlight flere kort
    pass

class cardSlot:
    def __init__(self,centerposx,centerposy):
        self.centerposx = centerposx
        self.centerposy = centerposy
        self.vacant = None

        self.rect = pg.Rect(0,0,card1.width,card1.height)
        self.rect.center = (centerposx,centerposy)


    def render(self):
        #kun for testing. I spillet burde slottet være usynlig
        pg.draw.rect(window,red,self.rect)

    def dropCheck(self):
        if self.vacant == None:
            x,y = pg.mouse.get_pos()
            if self.rect.collidepoint((x,y)):
                card1.posx = self.centerposx
                card1.posy = self.centerposy
                #self.vacant = True

slotAmount = 4 #hvor mange slots som skal være på skjermen
slotList = []

mellom = 100

slotRect = pg.Rect(0,0,(slotAmount-1)*mellom+(cardwidth*slotAmount),cardheight)
slotRect.center = (window_width/2,window_height/2)
x,y = slotRect.midleft
for i in range(slotAmount):
    slotList.append(cardSlot(x+(mellom*(i))+(cardwidth*(i)+(cardwidth/2)),window_height/2))

x,y = 0,0
def dropCheck():
    for i in range(len(slotList)):
        slotList[i].dropCheck()

def slotRender():
    for i in range(len(slotList)):
        slotList[i].render()

def cardGame():
    run = True
    while run:
        window.fill((255,255,255))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key ==pg.K_ESCAPE:
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                left,middle,right = pg.mouse.get_pressed()
                if left:
                    cardInterract()

            if event.type == MOUSEBUTTONUP:
                #Regne ut nærmeste sted kortet kan gå
                dropCheck()
                pass

        left,middle,right = pg.mouse.get_pressed()
        if left:
            cardMove()
        pg.draw.rect(window,black,slotRect)
        slotRender()
        card1.render()
        pg.display.flip()
        clock.tick(windowFPS)
for i in range(len(slotList)):
    print(slotList[i].centerposx)

cardGame()