from sqlite3 import Timestamp
from telnetlib import XASCII
import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE)
import random
pg.init()

w = 600
h = 700
d = pg.display.set_mode([w,h])
clock = pg.time.Clock()
teller=0


baller = []
class Ball:
    def __init__(self, x, y, fart_x, fart_y, radius, vindusobjekt):
        self.x=x
        self.y=y
        self.fart_x=fart_x
        self.fart_y=fart_y
        self.radius = radius
        self.vindusobjekt= vindusobjekt
    def tegn(self):
        pg.draw.circle(d,(32,178,170),(self.x,self.y),self.radius)

    def flytt(self):
        global slutt
        if ((self.x-self.radius)<=0) or ((self.x+self.radius)>self.vindusobjekt.get_width()):
            self.fart_x = -self.fart_x
        if (self.y<=0):
            self.fart_y = -self.fart_y
        if (self.y-self.radius>=self.vindusobjekt.get_height()):
            slutt=True
        self.x+=self.fart_x
        self.y+=self.fart_y


treff = 0
class Blokk:
    def __init__(self,display,x,y,bredde,lengde,fart):
        self.display = display
        self.x = x
        self.y = y
        self.bredde = bredde
        self.lengde = lengde
        self.fart = fart

    def tegn(self):
        pg.draw.rect(self.display,(232, 129, 19),(self.x,self.y,self.bredde,self.lengde))
    
    def flytt(self):
        tast = pg.key.get_pressed()
        if tast[K_LEFT]:
            self.x -= self.fart
            if self.x<0:
                self.x = 0
        if tast[K_RIGHT]:
            self.x += self.fart
            if (self.x+self.bredde) > self.display.get_width():
                self.x = self.display.get_width()-self.bredde   

    def kmb(self, baller):
        global treff
        for ball in baller:
            if (ball.x>self.x) and \
                (ball.x<self.x+self.bredde) and \
                (ball.y+ball.radius>self.y) and \
                (ball.y+ball.radius<self.y+self.lengde):
                ball.fart_y = -ball.fart_y
                ball.y = self.y-ball.radius
                treff+=1

                if treff%3==0:
                    if len(baller)-1<treff//3:
                        baller.append(Ball(250,250,random.randint(1,6),-4,30,d))
            

         
baller.append(Ball(250,250,random.randint(1,6),-4,30,d))
blokk = Blokk(d,200,600,150,15,5)

font = pg.font.SysFont('Comic Sans MS', 30)

slutt = False
fortsett = True
highscore = 0
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    d.fill((0,0,0))
    clock.tick(60)
    blokk.tegn()
    blokk.flytt()
    for i in baller:
        i.tegn()
        i.flytt()
    blokk.kmb(baller)
    print(treff)
    if not slutt:
        teller+=1
    tekst=str(teller)
    teksten = font.render(tekst, False, (255,255,255))
    d.blit(teksten,(30,30))
    tekst_highscore_spill = font.render('din highscore er: ' + str(highscore), False, (255,255,255))
    d.blit(tekst_highscore_spill,(30,70))
    if slutt:
        d.fill((0,0,0))
        nytekst = font.render('du tapte', False, (255,255,255))
        d.blit(nytekst,(30,30))
        tekst_restart = font.render("trykk 'space' for å restarte", False, (255,255,255))
        d.blit(tekst_restart,(30,70))
        if teller>=highscore:
            highscore = teller
        tekst_highscore = font.render('din highscore er: ' + str(highscore), False, (255,255,255))
        d.blit(tekst_highscore,(30,110))
        tast = pg.key.get_pressed()
        if tast[K_SPACE]:
            teller = 0
            baller.clear()
            baller.append(Ball(250,250,random.randint(1,6),-4,30,d))
            blokk.x=200
            blokk.y=600
            treff = 0
            slutt=False
    pg.display.flip()
pg.quit()
