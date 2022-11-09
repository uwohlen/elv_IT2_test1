import pygame as pg
import math
import random as r
import sys
pg.init()

#skrift
font = pg.font.Font("MarkusM/font_test/coolvetica rg.otf", 40)
font2 = pg.font.Font("MarkusM/font_test/coolvetica rg.otf", 80)
menyFont = pg.font.Font("MarkusM/font_test/MADE TOMMY Black_PERSONAL USE.otf",80)
timerFont = pg.font.Font("MarkusM/font_test/MADE TOMMY Regular_PERSONAL USE.otf",80)
pg.display.set_caption('gaming')

#farger
black = (0,0,0)
red = (200,0,0)
green = (100,200,100)
grey = (100,100,100)
light_grey = (220,220,220)
gdred = (235, 88, 52)
gdwhite = (100,100,100)
triangleBlue = (1,28,116)

#lyder
SoundEffectChannel = pg.mixer.Channel(1)
SoundEffectChannel2 = pg.mixer.Channel(2)
MusicChannel = pg.mixer.Channel(3)

highScore = 0

clock = pg.time.Clock() 
windowFPS = 60

#720p
window_width = 500
window_height = 700

blocklist = []

window = pg.display.set_mode([window_width,window_height])
run = True

class settings:
    def __init__(self):
        self.meny = 1
settings = settings()



global blockSize
blockSize = 100

global playerSize #størrelse av spiller-blokken
playerSize = (150,32)

def findCenter(): #finne center av skjermen
    return window_width/2,window_height/2

class block:
    def __init__(self,startpos):
        self.rect = pg.Rect(0,0,blockSize,blockSize)

        self.posx,self.posy = startpos
        self.momentum = 0,0

        self.momentum = (r.randint(4,8),r.randint(4,8))

        self.rect.center = (startpos)

        self.color = (r.randint(50,200),r.randint(50,200),r.randint(50,200))
        self.xcounter = 0
        self.ycounter = 0

    def posupdate(self): #oppdater posisjon til blokken
        
        x,y = self.momentum
        self.posx = self.posx - x
        self.posy = self.posy - y

        if self.posx-(blockSize/2) < 0 or self.posx > window_width-(blockSize/2):
            self.momentum = -x,y
        if self.posy-(blockSize/2) < 0 or self.posy > window_height-(blockSize/2):
            self.momentum = x,-y

        #legge til random?
        
        self.rect.center = (self.posx,self.posy)

    def render(self): #rendre blokker
        self.posupdate()
        pg.draw.rect(window,self.color,self.rect)

    def count(self): #oppdatere counter
        if self.ycounter >=1:
            self.ycounter -=1
        if self.xcounter >=1:
            self.xcounter -=1


def blockrender(): #funksjon for å rendere alle blokker på skjermen
    for i in range(len(blocklist)):
        blocklist[i].render()

def updateCounter(): #oppdatere counter
    for i in range(len(blocklist)):
        blocklist[i].count()

def addblock(): #funksjon for å blokk
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
        self.momentum = 5


    def move(self): #bevege spiller-blokken
        x,y = pg.mouse.get_pos()
        distlimit = 100

        #ved større avstander
        if abs(self.rect.centerx-x) > distlimit:

            if self.rect.centerx-x > self.momentum:
                self.rect.centerx -= self.momentum
            
            elif self.rect.centerx-x < self.momentum:
                self.rect.centerx += self.momentum

        #sakker farten når man nærmer seg 0
        elif abs(self.rect.centerx-x) > self.momentum/4:
            self.rect.centerx -= (self.rect.centerx-x)/12 

        elif abs(self.rect.centerx-x) <= self.momentum/4: #for verdier nærme nok, hopper blokken til musen
            self.rect.centerx = x
            
        

        #sakke fart når man nærmer seg musen
        
        #gammel metode:
        #self.rect.centerx = x

    def render(self): #rendere blokken
        self.move()
        pg.draw.rect(window,self.color,self.rect)

        #teste hitbox
        pg.draw.rect(window,(0,255,0),self.safebox)
        pg.draw.rect(window,(0,255,0),self.ysafebox1)
        pg.draw.rect(window,(0,255,0),self.ysafebox2)
        

    def updateSafebox(self): #oppdatere hitbox
        self.safebox = pg.Rect(0,0,self.width-10,5)
        self.safebox.midtop = self.rect.midtop

        self.ysafebox1 = pg.Rect(0,0,5,self.height-10)
        self.ysafebox2 = pg.Rect(0,0,5,self.height-10)
        self.ysafebox1.midleft = self.rect.midleft
        self.ysafebox2.midright = self.rect.midright

def safecollision(): #kollisjon mellom spiller og kube
    player.updateSafebox()

    #cooldown for å hindre at en blokk kan sprette flere ganger på rad
    #fikser ikke problemet, men orker ikke å finne en bedre måte å gjøre det på
    cd = 120

    #metode for å sjekke om det skjer en kollisjon, og dermed reversere momentum til blokk
    for i in range(len(blocklist)):
        updateCounter()
        if blocklist[i].ycounter == 0:
            if pg.Rect.colliderect(player.safebox,blocklist[i].rect):
                a,b = blocklist[i].momentum
                blocklist[i].momentum = a,-b
                blocklist[i].ycounter = cd
        if blocklist[i].xcounter ==0:
            if pg.Rect.colliderect(player.ysafebox1,blocklist[i].rect) or pg.Rect.colliderect(player.ysafebox2,blocklist[i].rect):
                a,b = blocklist[i].momentum
                blocklist[i].momentum = -a,b
            
                blocklist[i].xcounter = cd

player = player() #initiere spiller

addblock() #legge til en blokk
global counter
counter = 0
timediff = 5
def main():
    global counter

    while run:
        window.fill((255,255,255)) #bakgrunn
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key ==pg.K_ESCAPE: #exit ved bruk av escape, siden man ikke kan avslutte på vanlig måte
                    sys.exit()
    
        if counter > windowFPS*timediff: #legge til blokk etter en stund i sekunder
            addblock()
            counter = -1

        #render:
        safecollision()
        player.render()
        counter+=1
        blockrender()

        clock.tick(windowFPS) #holde frame rate til 60
        pg.display.flip() #oppdatere skjermen

class menublock:
    def __init__(self,posy,text,color):
        self.posy = posy
        self.rect = pg.Rect(0,0,window_width/1.5,window_height/8)
        self.color = color
        self.rect.center = window_width/2,posy
        self.text = font2.render(str(text),True,black) #definere tekst
        self.textBox = self.text.get_rect() #definere hvor stor teksten er
        self.textBox.center = self.rect.center #sentrere teksten i boksen

    def render(self):
        #rendere boks
        pg.draw.rect(window,self.color,self.rect)

        #rendere tekst
        window.blit(self.text,self.textBox) #render

#testbox = menublock(80,"TEST",light_grey)
startbox = menublock(window_height/2-window_height/5,"START",light_grey)
quitbox = menublock(window_height/2+window_height/5,"QUIT",light_grey)
shopbox = menublock(window_height/2,"SHOP",light_grey)
backbox = menublock(window_height/2+window_height/5,"BACK",light_grey)

def menurender():
    if settings.meny == 1:
        startbox.render()
        quitbox.render()
        shopbox.render()

        #tittel
        title = font2.render(str("GAMING"),True,black) #definere tekst
        titleBox = title.get_rect(center=(window_width/2,(window_height/8)))
        window.blit(title,titleBox) #render

    if settings.meny == 2:
        backbox.render()

        #tittel
        title = font2.render(str("SHOP"),True,black) #definere tekst
        titleBox = title.get_rect(center=(window_width/2,(window_height/8)))
        window.blit(title,titleBox) #render


def menuIntererract(mousepos):
    if settings.meny == 1:
        if quitbox.rect.collidepoint(mousepos):
            sys.exit()
        if startbox.rect.collidepoint(mousepos):
            global loop
            loop = False
        if shopbox.rect.collidepoint(mousepos):
            settings.meny = 2

    elif settings.meny == 2:
        if backbox.rect.collidepoint(mousepos):
            settings.meny = 1
        

def menu():
    global loop
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
            if event.type == pg.MOUSEBUTTONDOWN:
                left,middle,right = pg.mouse.get_pressed()
                mousepos = pg.mouse.get_pos()
                if left:
                    menuIntererract(mousepos)
        
            if event.type == pg.KEYDOWN:
                if event.key ==pg.K_ESCAPE:
                    sys.exit()
        window.fill((255,255,255))
        menurender()

        pg.display.flip()

while True: #spillLoop
    menu()
    main()

#endre fra et system der blokken er på musen, til at den går mot musen. Slik unngår man kollisjon? Annulere momentum hvis toucher blokk. nymomentum = gammel/2? Da vil den alltid gå mot musen. 

