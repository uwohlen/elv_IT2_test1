import pygame
import math as m
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)


vindu_bredde= 800
vindu_hoyde= 800 

pygame.init()

vindu= pygame.display.set_mode([vindu_bredde,vindu_hoyde])

font = pygame.font.SysFont("Sora", 24)

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()
    


class Ball:
    def __init__(self,x,y,radius,farge,vindusobjekt):
        self.x=x
        self.y=y
        self.radius=radius
        self.farge=farge
        self.vindusobjekt=vindusobjekt

    def tegn(self):
        pygame.draw.circle(self.vindusobjekt,self.farge,(self.x,self.y),self.radius)


class Hinder(Ball):
    def __init__(self, x, y, radius, farge, vindusobjekt,xFart,yFart):
        super().__init__(x, y, radius, farge, vindusobjekt)
        self.xFart=xFart
        self.yFart=yFart

    def flytt(self):
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
            self.xFart = -self.xFart
        if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
            self.yFart = -self.yFart

        

        self.x += self.xFart
        self.y += self.yFart


class Spiller:
    def __init__(self,x1,y1,x2,y2,farge,vindusobjekt,fart,tykkelse):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.farge=farge
        self.vindusobjekt=vindusobjekt
        self.fart=fart
        self.tykkelse=tykkelse
    
    def tegn(self):
        pygame.draw.line(self.vindusobjekt,self.farge,(self.x1,self.y1),(self.x2,self.y2),self.tykkelse)

    def flytt(self,taster):
        if taster[K_LEFT]:
            if self.x1<=0:
                self.x1=0
                self.x2=200
            else:
                self.x1 -= self.fart
                self.x2 -= self.fart
        if taster[K_RIGHT]:
            if self.x1>=600:
                self.x1=600
                self.x2=800
            else:
                self.x1 += self.fart
                self.x2 += self.fart
    


        

hinder1 = Hinder(100, 100, 20, (0, 0, 255), vindu, 3.5, 4.5)
hinder2=Hinder(100, 100, 20, (0, 0, 255), vindu, 3, 5.5)



spiller1=Spiller(300,600,500,600,(255,255,255),vindu,10,15)

fortsett=True

while fortsett:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fortsett = False



    trykkede_taster= pygame.key.get_pressed()

    vindu.fill((65, 39, 94))

    hinder1.tegn()
    hinder1.flytt()
    spiller1.tegn()
    spiller1.flytt(trykkede_taster)

    hinder2.tegn()
    hinder2.flytt()

    if hinder1.x>=spiller1.x1 and hinder1.x<=spiller1.x2 and hinder1.y+20>=spiller1.y1:
        hinder1.yFart = -hinder1.yFart


    if hinder2.x>=spiller1.x1 and hinder2.x<=spiller1.x2 and hinder2.y+20>=spiller1.y1:
        hinder2.yFart = -hinder2.yFart


    if hinder1.y>700:
        fortsett = False
    if hinder2.y>700:
        fortsett = False

   # print(finnavstand(spiller1,hinder1))
    print(spiller1.x1,spiller1.x2,"     ", hinder1.x,hinder1.y)
    pygame.display.flip()
    fpsClock.tick(FPS)

pygame.quit()
 