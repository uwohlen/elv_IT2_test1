import pygame as pg
import math
import random as r
import sys
pg.init()

#skrift
font = pg.font.Font("MarkusM/font_test/coolvetica rg.otf", 40)
font2 = pg.font.Font("MarkusM/font_test/coolvetica rg.otf", 80)
shopfont = pg.font.Font("MarkusM/font_test/coolvetica rg.otf", 50)
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

global highScore
highScore = 0

global score
score = 0

clock = pg.time.Clock() 
windowFPS = 60

#720p
window_width = 500
window_height = 700

blocklist = []

#window = pg.display.set_mode([window_width,window_height],pg.FULLSCREEN)
window = pg.display.set_mode([window_width,window_height])
run = True

class settings:
    def __init__(self):
        self.meny = 1
        self.coins = 10000
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
        global run
        global score
        global highScore
        x,y = self.momentum
        self.posx = self.posx - x
        self.posy = self.posy - y

        if self.posx-(blockSize/2) < 0 or self.posx > window_width-(blockSize/2):
            self.momentum = -x,y
        if self.posy-(blockSize/2) < 0:
            self.momentum = x,-y
        if self.posy>window_height-(blockSize/2):
            run = False
            if score > highScore:
                highScore = score

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
            
        
        #gammel metode:
        #self.rect.centerx = x

    def render(self): #rendere blokken
        self.move()
        pg.draw.rect(window,self.color,self.rect)

        #teste hitbox
        """
        pg.draw.rect(window,(0,255,0),self.safebox)
        pg.draw.rect(window,(0,255,0),self.ysafebox1)
        pg.draw.rect(window,(0,255,0),self.ysafebox2)
        """
        

    def updateSafebox(self): #oppdatere hitbox
        self.safebox = pg.Rect(0,0,self.width-20,5)
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

global counter
counter = 0
timediff = 5
def main():
    global score
    global counter
    global blocklist
    global run

    counter = 0
    run = True
    blocklist = []
    addblock()
    score = 0

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
        
        if (counter % windowFPS*timediff)==0:
            score +=1

        #render:
        safecollision()
        player.render()
        counter+=1
        blockrender()

        title = font2.render(str(score),True,black) #definere tekst
        titleBox = title.get_rect(center=(window_width/2,(window_height/8)))
        window.blit(title,titleBox) #render

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

gridsize = 50

class gridElement:
    def __init__(self,size,pos,color):
        self.size = size
        self.xpos,self.ypos = pos
        self.padding = pg.Rect(0,0,size,size)
        self.rect = pg.Rect(0,0,size-10,size-10)
        self.rect.center = pos
        self.padding.center = pos
        self.color = color
        self.buy = False

        self.textureraw = pg.image.load("MarkusM/images/coinicon.png")
        #texture = pg.transform.scale(self.textureraw,(size-10,size-10))

        self.pretexture = pg.Surface((size-10,size-10)) #performance
        self.pretexture.blit(self.textureraw,self.rect)

    def render(self):
        #pg.draw.rect(window,black,self.padding)
        #pg.draw.rect(window,self.color,self.rect)

        #if self.buy == False:
        window.blit(self.pretexture,self.rect)


gridlist = []
colorlist = []

class shopcolor:
    def __init__(self,color,price):
        self.color = color
        self.price = price

colorlist.append(shopcolor(black,0))
colorlist.append(shopcolor(green,2000))
colorlist.append(shopcolor(light_grey,0))
colorlist.append(shopcolor(gdred,2000))

gridspace = 25
def grid(kol,rad):
    #definere hvordan gridden skal se ut
    linesize = (rad-1)*gridsize+((rad-1)*gridspace)
    clx = (window_width/2-linesize/2)
    clspace = gridsize+gridspace

    for a in range(kol):
        for i in range(rad):
            gridlist.append(gridElement(gridsize,(clx+i*clspace,window_height/2),colorlist[i].color))
            #print(clx+i*clspace)
    #gridlist.append(gridElement(gridsize,(window_width/2,window_height/2),green))
    #gridlist.append(gridElement(gridsize,(window_width/4,window_height/2),black))


grid(1,4)

def gridrender():
    for i in range(len(gridlist)):
        gridlist[i].render()

def gridhover():
    #vise info når musen går over
    pass
def gridinterract():
    #kjøpe hvis man har nok penger, hvis ikke rød tekst med du har ikke nok penger
    pass

#coin i shop
coinw = 50
coinrect = pg.Rect(0,0,coinw,coinw)
shopcoin = pg.image.load("MarkusM/images/coinicon.png")
shopcoin = pg.transform.scale(shopcoin, (coinw, coinw))
shopcoinPretexture = pg.Surface((coinw,coinw)) #BIG FPS. gikk fra 25 til 60 😃
shopcoinPretexture.blit(shopcoin,coinrect)

coinspace = 10


coinrect.center = (window_width/2,window_height/2-(window_height/4))

#testbox = menublock(80,"TEST",light_grey)
startbox = menublock(window_height/2-window_height/5,"START",light_grey)
quitbox = menublock(window_height/2+window_height/5,"QUIT",light_grey)
shopbox = menublock(window_height/2,"SHOP",light_grey)
backbox = menublock(window_height/2+window_height/5,"BACK",light_grey)

def menurender():
    global shopcoinPretexture
    global coinrect
    global newcoinrect

    if settings.meny == 1:
        startbox.render()
        quitbox.render()
        shopbox.render()


        #tittel
        title = font2.render(str("MULTIPONG"),True,black) #definere tekst
        titleBox = title.get_rect(center=(window_width/2,(window_height/8)))
        window.blit(title,titleBox) #render

        #highscore
        if highScore != 0:
            score = shopfont.render(str(f"HIGHSCORE: {highScore}"),True,black) #definere tekst
            scorebox = score.get_rect(center=(window_width/2,(window_height-window_height/7)))
            window.blit(score,scorebox) #render

    if settings.meny == 2:
        backbox.render()

        #tittel
        title = font2.render(str("SHOP"),True,black) #definere tekst
        titleBox = title.get_rect(center=(window_width/2,(window_height/8)))
        window.blit(title,titleBox) #render

        #render coins
        cointext = shopfont.render(str(settings.coins),True,black)
        cointextbox = cointext.get_rect()

        totalbox = pg.Rect(0,0,cointextbox.width+coinrect.width+(coinspace*2),cointextbox.height)
        totalbox.center = (window_width/2,window_height/2-(window_height/4))

        c,d = totalbox.midleft
        cointextbox.midleft = c+coinrect.width+coinspace,d
        coinrect.midleft = c,d
        window.blit(shopcoinPretexture,coinrect)
        window.blit(cointext,cointextbox)

        gridrender()


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

