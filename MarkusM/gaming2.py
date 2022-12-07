import pygame as pg
import random as r
import sys, time
import os
from pygame.locals import *
import math as math

global spill
spill = None

#PIL trengs for å lage sirkel, så det trengs når man skal kjøre typegame()
try:
    from PIL import Image, ImageDraw
except:
    sys.exit("PIL trengs for å kjøre spillet. pip (pip3 på mac) install pillow, eller pip -U install pillow --user")

pg.init() #starter pygame

#definerer vinduet:
window_width = 1080
window_height = 720

#ulike moduser for å displaye pygame. For mac får man elendig ytelse uten FULLSCREEN
window = pg.display.set_mode([window_width,window_height],DOUBLEBUF)
#window = pg.display.set_mode([window_width,window_height],FULLSCREEN)
window.set_alpha(None) #måte for å prøve å øke fps
pg.display.set_caption('gaming')

#initiere fonts:
font = pg.font.Font("MarkusM/font_test/coolvetica rg.otf", 40)
font2 = pg.font.Font("MarkusM/font_test/coolvetica rg.otf", 80)
menyFont = pg.font.Font("MarkusM/font_test/MADE TOMMY Black_PERSONAL USE.otf",80)
timerFont = pg.font.Font("MarkusM/font_test/MADE TOMMY Regular_PERSONAL USE.otf",80)



keyIndex = 0

#initierer hvilke keys som blir brukt i typegame()    
keyInit = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","æ","ø","å"]

#metode for å imortere video/gif i pygame:
#gifList = []
#for i in range(44):
#    gifList.append(pg.image.load(f"MarkusM/gif_test/breaking-bad-money-{i}.png"))

#farger
black = (0,0,0)
red = (200,0,0)
green = (100,200,100)
grey = (100,100,100)
light_grey = (220,220,220)
gdred = (235, 88, 52)
gdwhite = (100,100,100)
triangleBlue = (1,28,116)

#fps
clock = pg.time.Clock() 

#Lager ulike kanaler, for å spille av ulike sound effects samtidig
SoundEffectChannel = pg.mixer.Channel(1)
SoundEffectChannel2 = pg.mixer.Channel(2)
MusicChannel = pg.mixer.Channel(3)

#ikke brukt lenger, men kan hende skal brukes i fremtiden
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

def findCenter(): #finne senter av skjermen
    return window_width/2,window_height/2

#Spill der man skal skrive inn ordet som kommer opp før man går tom for tid
def typeGame():
    answerTime = 6 #tid i sekunder man får til å svare
    typeMusic = pg.mixer.Sound(f"MarkusM/sounds/main_music.wav")
    typeMusic.set_volume(0.5) #volumkontroll
    MusicChannel.play(typeMusic) #spiller musikk (kahoot)

    #initierer variabler spesifikt til hver gjennomkjøring av spillet
    counter = 0 
    typetest = str()

    #oppgaver:
    #task = ["Kul","Hei","Onomatepoetikon","Iridocyclitis","Diabolical","Superoptikjempefantafenomenalistisk","Pneumonoultramicroscopicsilicovolcanoconiosis"]    
    task = ["kul","hei"]
    tasknr = 0
    timerPlayed = False
    sec = 0
    timer = 0

    run = True
    while run: #looper til man taper
        for event in pg.event.get():
            #events:
            if event.type == pg.QUIT: 
                sys.exit()
    
            #keypresses:
            if event.type == pg.KEYDOWN:
                try: 
                    keys = pg.key.get_pressed()
                    if keys[K_LSHIFT]: #store bokstaver
                        i = keyInit.index(pg.key.name(event.key))
                        typetest += keyInit[i].upper()

                    else:
                        i = keyInit.index(pg.key.name(event.key)) #små bokstaver
                        typetest += keyInit[i]
                        #print(typetest) #teste om stringen oppdaterer seg som den skal

                except:
                    pass
                if event.key == pg.K_RETURN: #submit svar
                    pg.mixer.Sound.stop

                    if typetest == task[tasknr]: #hvis det man har skrevet er riktig
                        tasknr +=1
                        typetest = str()
                        SoundEffectChannel.stop()
                        #spill funny sound effect
                        win = pg.mixer.Sound(f"MarkusM/sounds/win_{r.randint(0,2)}.wav")
                        SoundEffectChannel.play(win)
                        
                        #resette tid
                        timerPlayed = False
                        sec = 0
                        timer = 0
                        if tasknr==len(task):
                            run = False

                    else:
                        #spill funny sound effect
                        SoundEffectChannel.stop()
                        fail = pg.mixer.Sound(f"MarkusM/sounds/fail_{r.randint(0,2)}.wav")
                        SoundEffectChannel.play(fail)
                        pass

                if event.key == pg.K_BACKSPACE:
                    typetest = typetest[0:-1] #sletter

                    #hvis man holder i fler frames, sletter den fortere?
                if event.key == pg.K_SPACE: #mellomrom
                    typetest = typetest + str(" ")
                
                if event.key ==pg.K_ESCAPE: #avslutt med escape
                    sys.exit()

            #finne hvilken som er trykket
            """gammel metode"""

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
        print(run)
        if run == True:
            """ny metode"""
            window.fill((255,255,255)) #fulle skjermen med en hvit bakgrunn
        
            #vise oppgavetekst
            taskRender = font.render(str(task[tasknr]),True,(0,0,0))
            taskRect = taskRender.get_rect(center=((window_width/2),(window_height/2)-200))
            window.blit(taskRender,taskRect)

            #lagre en boks for å sentrere teskten man har skrevet inn
            typeText = font.render(str(typetest),True,(0,0,0))
            typeRect = typeText.get_rect(center=(window_width/2,window_height/2))


            for i in range(len(typetest)): #displaye teksten man har skrevet inn, med grønn som riktig og rød som feil

                textprev = font.render(str(typetest[0:i]),True,(0,0,0)) #finne lengde av teksten før
                textPrevLength = textprev.get_width() #lagre lengden
                charPosx, charPosy = typeRect.midleft #lagre koordiatene til rektangelet

                try: 
                    if not typetest[i] == task[tasknr][i]: #hvis riktig
                        charRender = font.render(str(typetest[i]),True,red)
                        window.blit(charRender,((charPosx+textPrevLength,charPosy)))
            
                    else: #hvis feil
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
            #bruke PIL
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
        #Oppdaterer skjermen og teller hvilken frame vi er på
        clock.tick(windowFPS)
        pg.display.flip() 

        #inkrimentere tellere
        counter +=1
        sec += 1/windowFPS

        #print(counter)
        #if counter == windowFPS:
        #    sec +=1
        #    counter = 0

        #hvis tiden er ute
        if timer == 360 or timer > 360:
            gameFail()
            break
        timer += (360/windowFPS)/answerTime #for å kontrolerer tid

class menublock:
    def __init__(self,pos,text,color):
        self.posx,posy = pos
        self.rect = pg.Rect(0,0,window_width/3+window_width/8,window_height/6)
        self.color = color
        self.rect.center = pos
        self.text = font2.render(str(text),True,black) #definere tekst
        self.textBox = self.text.get_rect() #definere hvor stor teksten er
        self.textBox.center = self.rect.center #sentrere teksten i boksen

    def render(self):
        #rendere boks
        pg.draw.rect(window,self.color,self.rect)

        #rendere tekst
        window.blit(self.text,self.textBox) #render
 
class settings: #lagre en mengde globale verdier
    def __init__(self):
        self.meny = 1
settings = settings()
centerx,centery = findCenter()
startoffset = -window_height/6

#definere menyelementer
startbox = menublock((centerx-window_width/4,centery),"START",light_grey)
quitbox = menublock((centerx+window_width/4,centery),"QUIT",light_grey)
backbox = menublock((centerx,centery+window_height/4),"BACK",light_grey)
hardbox = menublock((centerx,centery+window_height/6+startoffset+window_height/20),"HARD MODE",red)
geobox = menublock((centerx+window_width/4,centery+startoffset),"BLOCK JUMP",light_grey)
typbox = menublock((centerx-window_width/4,centery+startoffset),"TYPING",light_grey)
continueBox = menublock((centerx,centery),"BACK",green)

def menurender(): #rendre elementer i menyen
    if settings.meny == 1: #avslutte eller gå videre
        startbox.render()
        quitbox.render()

        #tittel
        title = font2.render(str("GAMING"),True,black) #definere tekst
        titleBox = title.get_rect(center=(window_width/2,(window_height/8)))
        window.blit(title,titleBox) #render

    if settings.meny == 2: #for å velge spillmodus
        backbox.render()
        typbox.render()
        geobox.render()
        hardbox.render()

        #tittel
        title = font2.render(str("START"),True,black) #definere tekst
        titleBox = title.get_rect(center=(window_width/2,(window_height/8)))
        window.blit(title,titleBox) #render

def menuIntererract(mousepos): #finne om musen trykker på en boks
    global spill
    if settings.meny == 1: #i meny 1
        if quitbox.rect.collidepoint(mousepos):
            sys.exit()

        if startbox.rect.collidepoint(mousepos):
            settings.meny = 2

    elif settings.meny == 2: #i meny 2
        if backbox.rect.collidepoint(mousepos):
            settings.meny = 1
        
        #starte spill
        if typbox.rect.collidepoint(mousepos):
            spill = True
            typeGame()
            if spill:
                winScreen()

                #prøve igjen hvis man taper
        if geobox.rect.collidepoint(mousepos):
            spill = True
            gd()
            if spill:
                winScreen()

                #prøve igjen hvis man taper
        if hardbox.rect.collidepoint(mousepos):
            spill = True
            gd()
            if spill:
                typeGame()
            if spill:
                winScreen()
                
def menu(): #menyloop
    global loop
    loop = True
    
    while loop:
        if MusicChannel.get_busy() == False: #lyder
            menuMusic = pg.mixer.Sound(f"MarkusM/sounds/MenuMusic.mp3")
            menuMusic.set_volume(0.5)
            MusicChannel.play(menuMusic)
            
        for event in pg.event.get(): #events
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

def introduction(): #lages senere?
    pass

def winScreen():
    show = True
    while show: #vise at man har vunnet og går tilbake til meny
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                left,middle,right = pg.mouse.get_pressed()
                mousepos = pg.mouse.get_pos()
                if left:
                    if continueBox.rect.collidepoint(mousepos):
                        show = False

    
        window.fill((255,255,255))
        continueBox.render()

        #tittel
        title = font2.render(str("DU VANT!!!!"),True,black) #definere tekst
        titleBox = title.get_rect(center=(window_width/2,(window_height/8)))
        window.blit(title,titleBox) #render
        
        pg.display.flip()
#geometry dash
class block: #blokk
    def __init__(self,length,centerposx,centerposy):
        self.width = length
        self.height = length
        self.centerposx = centerposx
        self.centerposy = centerposy
        self.rect = pg.Rect(0,0,self.width,self.height)
        texture = pg.image.load("MarkusM/images/gdBlock.png") #load texture

        self.preTexture = pg.Surface((self.width,self.height)) #performance ved å prerendere texture
        self.preTexture.blit(texture,self.rect)
        
    def safeCollision(self): #hoppekollision mellom spiller og blokk
        safeLine = pg.Rect(0,0,self.width,4)
        topCoords = self.rect.midtop
        safeLine.midtop = topCoords

        if pg.Rect.colliderect(player.rect,self.rect):
            x,y = self.rect.midtop #finner yposisjonen og spillerpoisjonen lik den. Dette er for å unngå at man kan sette seg fast inne i en blokk
            player.posy = y+1
            return True

    def harmCollision(self): #for å finne hvor man dør når man treffer en blokk
        harmLine = pg.Rect(0,0,1,self.height/1.5)   
        lower_harmLime = pg.Rect(0,0,self.width,1)
        topCoords = self.rect.midleft
        lowCoords = self.rect.midbottom
        harmLine.midleft = topCoords
        lower_harmLime.midbottom = lowCoords

        #returnerer sant hvis man kolliderer
        if pg.Rect.colliderect(harmLine,player.rect) or pg.Rect.colliderect(lower_harmLime,player.rect):
            return True
    
    def render(self,levelSpeed,counter): #metode for å rendere blokken på skjermen
        self.rect.center = (self.centerposx-(levelSpeed*counter),self.centerposy)
        x,y = self.rect.center

        if x > -self.width and x < window_width+self.width: #ikke rendere utenfor skjermen
            window.blit(self.preTexture,self.rect)

class triangle: #lage trekant
    def __init__(self,size,centerposx,centerposy):
        self.size = size
        self.centerposx = centerposx
        self.centerposy = centerposy
        self.heightRatio = 1.4

    def draw(self,speed,counter): #tegner en trekant
        newCenterPosx = self.centerposx -(speed*counter)
        if newCenterPosx > -self.size and newCenterPosx < window_width+self.size: #ikke rendere utenfor skjermen

            #finne alle punktene
            self.leftPoint = newCenterPosx-self.size,self.centerposy
            self.rightPoint = newCenterPosx+self.size,self.centerposy
            self.topPoint = newCenterPosx,self.centerposy-math.tan(math.radians(30))*(self.size*2*self.heightRatio)
        
            self.polygon = pg.draw.polygon(window,triangleBlue, ((self.topPoint),(self.leftPoint),(self.rightPoint)))
            self.storedMid = newCenterPosx

            #pg.draw.line(window,gdwhite,self.leftPoint,self.rightPoint)
            #pg.draw.line(window,gdwhite,self.leftPoint,self.topPoint)
            #pg.draw.line(window,gdwhite,self.topPoint,self.rightPoint)

        else:
            self.polygon = None
    
    def harmCollision(self): #kollisjon som fører til tap av spillet
        if not self.polygon == None:

            collideRect = pg.Rect(0,0,self.size/2,1.4*self.size)
            collideRect.midbottom = (self.storedMid,self.centerposy)
            if pg.Rect.colliderect(collideRect,player.rect): #bedre collision
                return True

class border: #lage "gulv"
    def __init__(self,height,width):
        self.texture = pg.image.load("MarkusM/images/gdBorder3.png")

        self.height = height
        self.width = width
        self.rect = pg.Rect(0,0,self.width,self.height)

        self.rect1 = pg.Rect(0,0,self.width,self.height) #kan ikke skrive self.rect = self.rect2 fordi python
        self.rect2 = pg.Rect(0,0,self.width,self.height)

        self.preTexture = pg.Surface((self.width,self.height)) #BIG FPS. gikk fra 25 til 60 😃
        self.preTexture.blit(self.texture,self.rect)
        print(self.preTexture.get_size())
        print(self.rect1.size)
        self.rect1.bottomright = (window_width, window_height)
        self.rect2.bottomright = (window_width*2, window_height)

        self.rect1coords = self.rect1.bottomright
        self.rect2coords = self.rect2.bottomright


    def render(self,speed): #rendere gulvet
        global window_width
        global window_width
        #pg.draw.rect(window,gdred,self.rect)

        #må bevege seg, og rendre ny texture etter. Import counter og levelspeed
        #lage metode for å bare rendre texures som er i frame. 

        #lager to "gulv", for å rendre dem separat
        x1,y1 = self.rect1coords
        x1 = x1-speed
        if x1 <=0:
            x1 = window_width*2
        self.rect1coords = (x1,y1)
        self.rect1.bottomright = (self.rect1coords)

        x2,y2 = self.rect2coords
        x2 = x2-speed
        if x2 <=0:
            x2 = window_width*2
        self.rect2coords = (x2,y2)
        self.rect2.bottomright = (self.rect2coords)

        window.blit(self.preTexture,self.rect1)
        window.blit(self.preTexture,self.rect2)

    def safeCollision(self): #hoppe
        #global window_width
        #global window_height
        #safeline = pg.Rect(0,0,self.width,1)
        #safeline.midbottom = (window_width/2,window_height-self.height)

        if pg.Rect.colliderect(player.rect,self.rect1) or pg.Rect.colliderect(player.rect,self.rect2):
            x,y = self.rect1.midtop
            player.posy = y+1
            return True
                
def harmcolissionCheck(): #sjekker alle kollisjoner som gjør at man taper spiller
    for i in range(len(blockList)):
        if blockList[i].harmCollision():
            return True
    for i in range(len(triangleList)):
        if triangleList[i].harmCollision():
            return True

def safeColissionCheck(): #sjekker alle kollisjoner som gjør at man kan hoppe
    for i in range(len(blockList)):
        if blockList[i].safeCollision():
            return True
    if lower_border.safeCollision():
        return True
    else:
        return False #ved collision problemer sjekk denne. Kan hende for-løkken ikke stopper etter return
    
class Player: #definere spiller
    def __init__(self,length,borderHeight):
        global window_width
        global window_height

        self.momentum = 0
        self.length = length
        self.posx = window_width/2 #egentlig meningsløs siden vi bruker en konstant x-verdi
        self.posy = window_height-borderHeight
        #self.safeRect = pg.Rect(0,0,self.length,self.length)
        self.rect = 0
        self.rect = pg.Rect(0,0,self.length,self.length)

        #texture til spiller
        playerIconRaw = pg.image.load("MarkusM/images/gdPlayer.png") 
        playerIcon = pg.transform.scale(playerIconRaw,(100,100))
        self.preTexture = pg.Surface((self.length,self.length)) #performance
        self.preTexture.blit(playerIcon,self.rect)

    
    def jump(self): #hoppe
        self.momentum = 15

    def render(self): #rendre spiller
        self.posy = self.posy-self.momentum
        self.rect.midbottom = (self.posx,self.posy)
        

        if not safeColissionCheck(): #falle
            self.momentum -=0.6
        else:
            self.momentum = 0
            self.posy = self.posy-self.momentum
            if harmcolissionCheck():
                pass
            else:
                self.rect.midbottom = (self.posx,self.posy)

        window.blit(self.preTexture,self.rect)

def gdGameOver(): #hvis man taper spillet
    SoundEffectChannel.stop()
    fail = pg.mixer.Sound(f"MarkusM/sounds/fail_{r.randint(0,2)}.wav")
    SoundEffectChannel.play(fail)
    MusicChannel.stop()
    global spill
    spill = False

def gdWin(): #hvis man vinner
    pass
    #play gd win sound
    #proceed

#initiere spiller og border
borderHeight = 50
player = Player(100,borderHeight) #bredde gd blokk
lower_border = border(borderHeight,window_width)
print(player.rect)
blockList = []
triangleList = []


#level layout
x,y = 0,0
lvl="""
            x          x                                                                      ^                     xx^^^^                       ^                          xxxx^^^^
                   ^x^^           xx   x                                                      x                xx     xxxxxxx    x          ^x^                  x^^^^^x^^^^x
                x  xxxx  ^    xx                                                    ^       xxx           xx                              x^xxx              x
           xxx^^        ^xxx    ^^^^^^^^^^^^          ^     ^^       x^^^         xxx^^x             xx     ^^^^^            ^^^^^^^^^^x  xxxxx^^xx^^^^xxx^^^^^^^^    ^^^^^^^^^          w 

"""

#metode for å splitte opp en tekst string til en level
win = 0
lvl = lvl.split("\n")
lvl.reverse()
for line in lvl: #sjekker hver linje
    for char in line: #sjekker hver karakter
        if char == "x": #lage blokk
            blockList.append(block(100,x*100+2000,window_height-100*y+100))
        elif char == "^": #lage trekant
            triangleList.append(triangle(50,x*100+2000,window_height-100*y+150))
        elif char == "w": #lage win
            win = x*100+2000
        x +=1
    x,y = 0,y+1

#testverdier/startverdier
triangle2 = triangle(50,window_width+200+1080,window_height-borderHeight)
block2 = block(100,window_width+1080,window_height-borderHeight-50)
block3 = block(100,window_width+100+1080,window_height-borderHeight-50)
blockList.append(block2)
blockList.append(block3)
triangleList.append(triangle2)

def gdWin():
    #geometry dash win sound effect
    #animasjon?
    MusicChannel.stop()

def gd():#definere hvordan spillet oppfører seg
    lower_border.rect1counter = 0
    lower_border.rect2counter = 0
    jumpBuffer = 0

    #lyder
    gdMusic = pg.mixer.Sound(f"MarkusM/sounds/gdMusic.mp3")
    gdMusic.set_volume(0.5)
    MusicChannel.play(gdMusic)

    levelSpeed = 8 #ganges med 0,008/0,6 for å finne jump velocity
    counter = 0
    renderCounter = 0

    #bakgrunnsbilde
    backgroundRect = pg.Rect(0,0,window_width,window_height)
    background = pg.image.load("MarkusM/images/gdBackground.png")
    backgrundRender = pg.Surface((window_width,window_height)) #performance
    backgrundRender.blit(background,backgroundRect)
    run = True
    while run:
        
        #events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            #hopp
            if event.type == MOUSEBUTTONDOWN:
                left,middle,right = pg.mouse.get_pressed()
                if left:
                    jumpBuffer = 15 #hvis man trykker, hopper karakteren med en gang den treffer gulvet. Gjør at hopping føles bedre og blir lettere

        if safeColissionCheck() and jumpBuffer > 0:
            player.jump()
        
        if jumpBuffer > 0:
            jumpBuffer -=1 #oppdatere buffer
        
        #window.fill((255,255,255))

        #render

        if renderCounter == 0: #rendere alt hver fjerde frame. Gjøres for å oppdatere fysikken oftere, men forsatt få god ytelse
            window.blit(backgrundRender,(0,0))
            for i in range(len(blockList)):
                blockList[i].render(levelSpeed,counter)
            for i in range(len(triangleList)):
                triangleList[i].draw(levelSpeed,counter)
            lower_border.render(levelSpeed)
            player.render()
            pg.display.flip()
            counter+=1
            if harmcolissionCheck():
                gdGameOver()
                run = False
        #vinne
        if win <= levelSpeed*counter:
            gdWin()
            run = False
        #oppdatere deller
        if renderCounter == 1:
            renderCounter = -1
        renderCounter +=1

        clock.tick(windowFPS*4) #fysikkhastigheten
        #clock.tick(60)


def gameFail(): #fail
    SoundEffectChannel.stop()
    fail = pg.mixer.Sound(f"MarkusM/sounds/fail_{r.randint(0,2)}.wav")
    SoundEffectChannel.play(fail)
    MusicChannel.stop()
    global spill
    spill = False

while True: #game loop
    menu()
    
    #testing:
    #gd()
    #introduction()
    #typeGame()
    #cardGame()

    #time.sleep(2)

#! kommenter ut enten typegame eller gd for spill. introduction eller cardgame gjør ikke noe


#lavere frame rate gir bedre tid. Endre til at man ganger teller med en mulitplier basert på framerate
#Performance. Lage en løkke som sjekker om elementer er av skjermen, og velger å ikke blitte.
#endre resolution til 1280x720 eller 1920x1080

#lage metode for å velge hvilket spill man vil spille

#hard mode (man må få til begge for å vinne)

#https://www.cleverpdf.com/gif-to-png
#https://www.dafont.com/top.php