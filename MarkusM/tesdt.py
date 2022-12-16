#print("😄")
import pygame as pg
import pylab
import math 
import sys

#simpuleringsalternativer
startPoint = True
string = True

window_width = 500
window_height = 500
pg.init() #starter pygame
window = pg.display.set_mode([window_width,window_height])
font = pg.font.Font("MarkusM/font_test/coolvetica rg.otf", 30)

clock = pg.time.Clock() 

black = (0,0,0)
red = (150,20,20)
grey = (100,100,100)

windowFPS = 60

global g
g = 9.81 #m/s^2

global timeStep
timeStep = 0.01

global stringpos
strinpos = 0 #positiv retning nedover 

global stringLen
stringLen = 1.3 #lengden på tråen i m

global stringF
stringF = 0,0

def fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, True, (0,0,0))
	return fps_text


class barbie():
    def __init__(self,m,pos,v):
        self.m = m
        self.pos = pos
        self.v = v
        self.a = (0,0)
        self.f = (0,0)

        size = window_width/10
        self.rect = pg.Rect(0,0,size,size)

    def updatePos(self):
        vx,vy = self.v
        x,y = self.pos

        self.pos = x-(vx*timeStep),y-(vy*timeStep)

    def updateV(self):
        vx,vy = self.v
        ax,ay = self.a

        self.v = vx-(ax*timeStep),vy-(ay*timeStep)
    
    def updateA(self):
        self.f = (0,g)

        self.f = self.f[0],self.f[1]-(math.cos(math.radians(lodd.vinkel)))
        print(self.f)
        self.a = self.f[0],self.f[1]

    def render(self):
        x,y = self.pos
        self.rect.center = (x,y)
        pg.draw.rect(window,black,self.rect)

class lodd():
    def __init__(self,m,pos,v):
        self.m = m
        self.pos = pos
        self.v = v
        self.a = (0,0)
        self.f = (0,0)
        self.vinkel = 0

        size = window_width/15
        self.rect = pg.Rect(0,0,size,size)

    def updatePos(self):
        vx,vy = self.v
        x,y = self.pos
        self.pos = x-(vx*timeStep),y-(vy*timeStep)

    def updateV(self):
        vx,vy = self.v
        ax,ay = self.a

        self.v = vx-(ax*timeStep),vy-(ay*timeStep)
    
    def updateA(self):
        self.f = (0,g)
        xpos,ypos = self.pos
        self.vinkel = math.degrees(math.atan(-(ypos-(window_height/2))/(xpos-(window_height/2))))

        if self.pos[0]<window_width/2:
            self.vinkel = 180 + self.vinkel
        self.vinkel = self.vinkel%360


        #bryr meg bare om y-retningen foreløpig
        bx = barb.pos[0]
        bx = bx-window_height/2
        v = math.sqrt(abs((lodd.v[0]**2)+(lodd.v[1]**2)))

        #v=v/self.m
        totf = barb.f[1]
        yf = math.sin(math.radians(self.vinkel))*totf
        xf = math.cos(math.radians(self.vinkel))*totf


        #self.f = self.f[0]-xf,self.f[1]-yf

        if self.pos[0]>window_width/2:
            self.f = self.f[0]-xf,self.f[1]-yf
        else:
            self.f = self.f[0]-xf,-(self.f[1]-yf)
        
        self.a = self.f[0],self.f[1]

    def render(self):
        x,y = self.pos
        self.rect.center = (x,y)
        pg.draw.rect(window,black,self.rect)

def helpLines():
    if startPoint:
        pointrect = pg.Rect(0,0,25,25)
        pointrect.center = (window_width/2,window_height/2)
        pg.draw.rect(window,red,pointrect)

    if string:
        x1,y1 = barb.rect.center
        x2,y2 = lodd.rect.center
        pg.draw.line(window,grey,(x1,y1),(window_width/2,window_height/2),5)
        pg.draw.line(window,grey,(x2,y2),(window_width/2,window_height/2),5)

def render():
    lodd.render()
    barb.render()
    helpLines()

#barbie
bpos = window_width/2,window_height/2+100
barb = barbie(1400,(bpos),(0,0))

#lodd
lpos = window_width/2+100,window_height/2
lodd = lodd(100,(lpos),(0,0))

print(lodd.a)

def update():
    #akselerasjon, fart og til slutt posisjon
    lodd.updateA() #sentripetal
    barb.updateA()
    
    lodd.updateV()
    barb.updateV()
    
    lodd.updatePos()
    barb.updatePos()
counter = 3
run = True
while run: 
    for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key ==pg.K_ESCAPE:
                    sys.exit()
                
    #oppdatere alt
    window.fill((255,255,255))

    counter+=1

    if counter ==4:
        x,y = lodd.pos
        n = str(round(x,2))+" , "+str(round(y,2))
        postext = font.render((n),True,(0,0,0))
        posRect = postext.get_rect(center=((window_width/2),50))

        vx,vy = lodd.v
        n = str(round(vx,2))+" , "+str(round(vy,2))
        vtext = font.render((n),True,(0,0,0))
        vRect = vtext.get_rect(center=((window_width/2),100))

        n = str("Vinkel: ")+str(lodd.vinkel)
        vintext = font.render((n),True,(0,0,0))
        vinRect = vintext.get_rect(center=((window_width/2),150))

        counter = 0
    
    window.blit(postext,(posRect))
    window.blit(vtext,(vRect))
    window.blit(vintext,(vinRect))

    fpsText = fps()
    fpsrect = fpsText.get_rect()
    window.blit(fpsText,(fpsrect))

    update()
    render()
    pg.display.flip()

    clock.tick(windowFPS)
    #lagre nye verdier for posisjonen til barbie og lodd


