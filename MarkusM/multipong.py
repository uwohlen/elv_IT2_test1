import pygame as pg
import math
import random as r
import sys

highScore = 0

clock = pg.time.Clock() 
windowFPS = 60

#720p
window_width = 500
window_height = 700

blocklist = []

pg.init()

window = pg.display.set_mode([window_width,window_height])
run = True

global blockSize
blockSize = 100

global playerSize

playerSize = (150,32)

class block:
    def __init__(self,startpos):
        self.rect = pg.Rect(0,0,blockSize,blockSize)

        self.posx,self.posy = startpos
        self.momentum = 0,0

        self.momentum = (r.randint(1,5),r.randint(1,5))

        self.rect.center = (startpos)

        self.color = (r.randint(50,200),r.randint(50,200),r.randint(50,200))
        self.xcounter = 0
        self.ycounter = 0

    def posupdate(self):
        
        x,y = self.momentum
        self.posx = self.posx - x
        self.posy = self.posy - y

        if self.posx-(blockSize/2) < 0 or self.posx > window_width-(blockSize/2):
            self.momentum = -x,y
        if self.posy-(blockSize/2) < 0 or self.posy > window_height-(blockSize/2):
            self.momentum = x,-y

        #legge til random
        
        self.rect.center = (self.posx,self.posy)

    def render(self):
        self.posupdate()
        pg.draw.rect(window,self.color,self.rect)

    def count(self):
        if self.ycounter >=1:
            self.ycounter -=1
        if self.xcounter >=1:
            self.xcounter -=1


def blockrender():
    for i in range(len(blocklist)):
        blocklist[i].render()

def updateCounter():
    for i in range(len(blocklist)):
        blocklist[i].count()

def addblock():
    blocklist.append(block((window_width/2,window_height/2)))


class player():
    def __init__(self):
        self.width,self.height = playerSize
        self.rect = pg.Rect(0,0,self.width,self.height)
        self.color = (0,0,0)
        self.posy = window_height-window_height/4
        self.posx = 0
        self.rect.center = self.posx,self.posy

        self.updateSafebox()

    def move(self):
        x,y = pg.mouse.get_pos()
        self.rect.centerx = x
        
    def render(self):
        self.move()
        pg.draw.rect(window,self.color,self.rect)
        pg.draw.rect(window,(0,255,0),self.safebox)
        pg.draw.rect(window,(0,255,0),self.ysafebox1)
        pg.draw.rect(window,(0,255,0),self.ysafebox2)
        

    def updateSafebox(self):
        self.safebox = pg.Rect(0,0,self.width-10,5)
        self.safebox.midtop = self.rect.midtop

        self.ysafebox1 = pg.Rect(0,0,5,self.height-10)
        self.ysafebox2 = pg.Rect(0,0,5,self.height-10)
        self.ysafebox1.midleft = self.rect.midleft
        self.ysafebox2.midright = self.rect.midright

def safecollision():
    player.updateSafebox()
    for i in range(len(blocklist)):
        updateCounter()
        if blocklist[i].ycounter == 0:
            if pg.Rect.colliderect(player.safebox,blocklist[i].rect):
                a,b = blocklist[i].momentum
                blocklist[i].momentum = a,-b
                blocklist[i].ycounter = 60
        if blocklist[i].xcounter ==0:
            if pg.Rect.colliderect(player.ysafebox1,blocklist[i].rect) or pg.Rect.colliderect(player.ysafebox2,blocklist[i].rect):
                a,b = blocklist[i].momentum
                blocklist[i].momentum = -a,b
            
                blocklist[i].xcounter = 60






player = player()

addblock()

counter = 0
timediff = 5

while run:
    window.fill((255,255,255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key ==pg.K_ESCAPE:
                sys.exit()
    
    if counter > windowFPS*timediff:
        addblock()
        counter = -1

    safecollision()
    player.render()
    counter+=1
    blockrender()

    clock.tick(windowFPS)
    pg.display.flip()








