import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import random as random
import sys, time
import os
from pygame.locals import *
from random import choice
from pygame import mixer

# Initialiserer/starter pygame

pg.init()



# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1280
VINDU_HOYDE  = 720
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
print(type(vindu))
# var.replace(([Colour you want to replace]), [Colour you want])

SoundEffectChannel = pg.mixer.Channel(1)
SoundEffectChannel2 = pg.mixer.Channel(2)
MusicChannel = pg.mixer.Channel(3)
MusicChannelGame = pg.mixer.Channel(4)

klokke = 0
clock = pg.time.Clock()
pongs = []
bakgrunnlist = []
bakgrunnlist2 = []
shop_bakgrunnlist = []
shop_bakgrunnlist2 = []
game_backgroundlist = []
game_backgroundlist2 = []
counter_meny = 0
counter_shop = 0
counter_game_background = 0

for i in range(113):
    bakgrunnlist.append(pg.image.load(f"Benjamin/pngs/multipong/bakgrunn_gif/images/waneella-pixel-art-{i}.png"))
for i in range(0,112):
    bakgrunnlist2.append(pg.transform.scale(bakgrunnlist[i], (VINDU_BREDDE, VINDU_HOYDE)))

for i in range(314):
    shop_bakgrunnlist.append(pg.image.load(f"Benjamin/pngs/multipong/shop_gif/images/pixel-sakura-{i}.png"))
for i in range(0,313):
    shop_bakgrunnlist2.append(pg.transform.scale(shop_bakgrunnlist[i], (VINDU_BREDDE, VINDU_HOYDE)))
    
gif_rate = 15
for i in range(0, 32):
  for o in range(1, gif_rate + 1):
    game_backgroundlist.append(pg.image.load(f"Benjamin/pngs/multipong/game_background_gif/images/tumblr_nr2569nqX01qze3hdo1_r2_500-{i}.png"))
for i in range(0,31 * gif_rate):
    game_backgroundlist2.append(pg.transform.scale(game_backgroundlist[i], (VINDU_BREDDE / 2, VINDU_HOYDE)))

start_bilde = pg.image.load('Benjamin/pngs/multipong/Start.png').convert_alpha()
shop_bilde = pg.image.load('Benjamin/pngs/multipong/Shop.png').convert_alpha()
exit_bilde = pg.image.load('Benjamin/pngs/multipong/Exit.png').convert_alpha()
back_bilde = pg.image.load('Benjamin/pngs/multipong/Back.png').convert_alpha()

sakura_bilde = pg.image.load('Benjamin/pngs/multipong/Sakura1.jpg').convert_alpha()

class Button():
  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.clicked = False

  def draw(self):
    action = False
    # Få posisjonen til musen
    pos = pg.mouse.get_pos()

    if self.rect.collidepoint(pos):
      if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
        action = True

    if pg.mouse.get_pressed()[0] == 0:
      self.clicked = False
    
    # tegne knappene
    vindu.blit(self.image, (self.rect.x, self.rect.y))
      
    return action

start_button = Button(100,200,start_bilde, 1)
shop_button = Button(700,200,shop_bilde, 1)
exit_button = Button(400,500,exit_bilde, 1)
back_button = Button(VINDU_BREDDE * (14.5/16), VINDU_HOYDE / 48, back_bilde, 0.75)

class Bilder:
  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.clicked = False
  
  def draw(self):
    vindu.blit(self.image, (self.rect.x, self.rect.y))


sakura_bilde1 = Bilder(0,0,pg.transform.flip(sakura_bilde, True, False), 0.352)
sakura_bilde2 = Bilder(560,0, sakura_bilde, 0.352)

class Arena:
  def __init__(self,x,y,bredde,høyde,farge):
    self.x = x
    self.y = y
    self.bredde = bredde
    self.høyde = høyde
    self.farge = farge
  def tegnarena(self):
    """Metode for å tegne arena"""
    pg.draw.rect(vindu, arena.farge, (arena.x, arena.y, arena.bredde, arena.høyde))

arena = Arena(VINDU_BREDDE / 4, 0,VINDU_BREDDE / 2, VINDU_HOYDE,(0,0,0))

    
class Pong:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fartx, farty, bredde, høyde, vindusobjekt, farge, passes, image):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fartx = fartx
    self.farty = farty
    self.bredde = bredde
    self.høyde = høyde
    self.vindusobjekt = vindusobjekt
    self.farge = farge
    self.passes = passes
    self.image = image
    rect = image.get_rect()
    rect.center = (x, y)

base_icon = pg.image.load(f"Benjamin/pngs/multipong/base_icon.png").convert()
base_icon = pg.transform.scale(base_icon, (45, 45))

def lage():
    if klokke % 3000 == 0:
      pongs.append(Pong(random.randint(560,720),random.randint(100,200),(choice([i for i in range(-8,8) if i not in [-3,-2,-1,0,1,2,3]])/10) * 2,(choice([i for i in range(4,8) if i not in [0]])/10) * 2,45,45,vindu, (random.randint(0,255),random.randint(0,255),random.randint(0,255)),0, base_icon))


def tegn():
    global klokke
    """Metode for å tegne kvadratene"""
    for i in range(0,len(pongs)):
      vindu.blit(pongs[i].image, (pongs[i].x, pongs[i].y))
    pg.draw.rect(plate.vindusobjekt, plate.farge, (plate.x, plate.y, plate.bredde, plate.høyde))

def nytt_spill():
    global pongs
    global klokke
    pongs = []
    plate.x = VINDU_BREDDE / 2 - plate.bredde / 2
    klokke = 0

class Plate:
  def __init__(self, x, y, fartx, farty, bredde, høyde, vindusobjekt, farge):
    self.x = x
    self.y = y
    self.fartx = fartx
    self.farty = farty
    self.bredde = bredde
    self.høyde = høyde
    self.vindusobjekt = vindusobjekt
    self.farge = farge

plate = Plate(560,650,1 * 2,0,160,10,vindu,(255,255,255))
hastighet = 2

def flytt():
    global klokke
    global spill
    global hastighet
    """Metode for å flytte kvadratene"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    for i in range(0,len(pongs)):
        if ((pongs[i].x) <= arena.x) or ((pongs[i].x + pongs[i].bredde) >= arena.x + arena.bredde):
          pongs[i].fartx = -pongs[i].fartx
        elif pongs[i].passes > 0 and ((pongs[i].y) <= arena.y):
          pongs[i].passes +=1
          pongs[i].farty = -pongs[i].farty
        elif ((pongs[i].y + pongs[i].høyde) >= arena.høyde):
          nytt_spill()
          spill = False
          meny()
        elif plate.x < (pongs[i].x) < (plate.x + plate.bredde) and (plate.y - 1) < (pongs[i].y + pongs[i].høyde) < (plate.y + 1) or plate.x < (pongs[i].x + pongs[i].bredde) < (plate.x + plate.bredde) and (plate.y - 1) < (pongs[i].y + pongs[i].høyde) < (plate.y + 1):
          pongs[i].farty = -pongs[i].farty
          if pongs[i].fartx > 0:
            pongs[i].fartx = ((random.randint(1,6) / 10) + pongs[i].fartx)
          elif pongs[i].fartx >= 1.2 * hastighet:
            pongs[i].fartx = 0.6 * hastighet
          elif pongs[i].fartx >= 0:
            pongs[i].fartx = -((random.randint(1,6) / 10) + pongs[i].fartx)
          elif pongs[i].fartx <= -1.2 * hastighet:
            pongs[i].fartx = -0.6 * hastighet
          pongs[i].passes += 1
          if SoundEffectChannel.get_busy() == False:
            lyd_effekt1 = pg.mixer.Sound("Benjamin/Lyd/Explosion meme - Sound Effect.mp3")
            lyd_effekt1.set_volume(0.5)
            SoundEffectChannel.play(lyd_effekt1)
          if SoundEffectChannel.get_busy() == True:
            lyd_effekt1 = pg.mixer.Sound("Benjamin/Lyd/Explosion meme - Sound Effect.mp3")
            lyd_effekt1.set_volume(0.5)
            SoundEffectChannel2.play(lyd_effekt1)
        elif (pongs[i].y -3) < (plate.y + (plate.høyde / 2)) < (pongs[i].y + pongs[i].høyde + 3) and (pongs[i].x + pongs[i].bredde - 3) < plate.x < (pongs[i].x + pongs[i].bredde + 3):
          pongs[i].fartx = -plate.fartx - (0.1 * hastighet)
        elif (pongs[i].y -3) < (plate.y + (plate.høyde / 2)) < (pongs[i].y + pongs[i].høyde + 3) and (pongs[i].x - 3) < (plate.x + plate.bredde) < (pongs[i].x + 3):
          pongs[i].fartx = plate.fartx + (0.1 * hastighet)
          pongs[i].passes += 1
        pongs[i].x += pongs[i].fartx
        pongs[i].y += pongs[i].farty

def bounce():
    global klokke
    for i in range(-1,len(pongs)):
      for o in range(-1,i) and range(i+1, len(pongs)):
        if pongs[o].x < (pongs[i].x) < (pongs[o].x + pongs[o].bredde) and (pongs[o].y - 1) < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + 1) or pongs[o].x < (pongs[i].x + pongs[i].bredde) < (pongs[o].x + pongs[o].bredde) and (pongs[o].y - 1) < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + 1):
          pongs[i].farty,pongs[o].farty = -pongs[i].farty,-pongs[o].farty
          pongs[i].passes += 1
          pongs[o].passes += 1
        if pongs[o].x < (pongs[i].x) < (pongs[o].x + pongs[o].bredde) and (pongs[o].y + pongs[o].høyde - 1) < (pongs[i].y) < (pongs[o].y + pongs[o].høyde + 1) or pongs[o].x < (pongs[i].x + pongs[i].bredde) < (pongs[o].x + pongs[o].bredde) and (pongs[o].y + pongs[o].høyde - 1) < (pongs[i].y) < (pongs[o].y + pongs[o].høyde + 1):
          pongs[i].farty,pongs[o].farty = -pongs[i].farty,-pongs[o].farty
          pongs[i].passes += 1
          pongs[o].passes += 1
        if pongs[o].y < (pongs[i].y) < (pongs[o].y + pongs[o].høyde) and (pongs[o].x - 1) < (pongs[i].x + pongs[i].bredde) < (pongs[o].x + 1) or pongs[o].y < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + pongs[o].høyde) and (pongs[o].x - 1) < (pongs[i].x + pongs[i].bredde) < (pongs[o].x + 1):
          pongs[i].fartx,pongs[o].fartx = -pongs[i].fartx,-pongs[o].fartx
          pongs[i].passes += 1
          pongs[o].passes += 1
        if pongs[o].y < (pongs[i].y) < (pongs[o].y + pongs[o].høyde) and (pongs[o].x + pongs[o].bredde - 1) < (pongs[i].x) < (pongs[o].x + pongs[o].bredde + 1) or pongs[o].y < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + pongs[o].høyde) and (pongs[o].x + pongs[o].bredde - 1) < (pongs[i].x) < (pongs[o].x + pongs[o].bredde + 1):
          pongs[i].fartx,pongs[o].fartx = -pongs[i].fartx,-pongs[o].fartx
          pongs[i].passes += 1
          pongs[o].passes += 1

def plate_bevegelse():
  trykkede_taster = pg.key.get_pressed()
  if trykkede_taster[K_LEFT]:
    plate.x -= plate.fartx
    if plate.x <= arena.x:
      plate.x += plate.fartx
  if trykkede_taster[K_RIGHT]:
    plate.x += plate.fartx
    if (plate.x + plate.bredde) > (arena.x + arena.bredde):
      plate.x -= plate.fartx
  if trykkede_taster[K_UP]:
    sys.exit()

def poeng(klokke):
  poeng = int(klokke / 100)
  return str(poeng)


# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.Font("Benjamin/Fonts/pixel-font.ttf", 48) 

def game():
  global klokke
  global counter_game_background
  global gif_rate
  spill = True
  MusicChannel.fadeout(3000)
  while spill:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        sys.exit()
    if MusicChannelGame.get_busy() == False:
            game_musikk = pg.mixer.Sound("Benjamin/Lyd/DJ Striden - Level One.mp3")
            game_musikk.set_volume(0.5)
            MusicChannelGame.play(game_musikk)
    plate_bevegelse()
    vindu.fill((120, 120, 120))
    sakura_bilde2.draw()
    sakura_bilde1.draw()
    arena.tegnarena()
    vindu.blit(game_backgroundlist2[counter_game_background],(VINDU_BREDDE / 4, 0))
    counter_game_background += 1
    if counter_game_background == 31 * gif_rate:
      counter_game_background = 0
    s = pg.Surface((VINDU_BREDDE / 2,VINDU_HOYDE))  # the size of your rect
    s.set_alpha(64)                # alpha level
    s.fill((255, 255, 255))           # this fills the entire surface
    vindu.blit(s, (VINDU_BREDDE / 4, 0))           # (0,0) are the top-left coordinates
    bilde1 = font.render(poeng(klokke), True, (100, 100, 100))
    bilde_rect1 = bilde1.get_rect(center=(VINDU_BREDDE/1.98, VINDU_HOYDE/7.85))
    vindu.blit(bilde1, (bilde_rect1))
    bilde = font.render(poeng(klokke), True, (255, 255, 255))
    bilde_rect = bilde.get_rect(center=(VINDU_BREDDE/2, VINDU_HOYDE/8))
    vindu.blit(bilde, (bilde_rect))
    lage()
    tegn()
    '''bounce()'''
    flytt()
    klokke += 1
    clock.tick(1000)
    pg.display.flip()
  # Oppdaterer alt innholdet i vinduet
    
def shop():
  global klokke
  global counter_shop
  sjappe = True
  while sjappe:
    for event in pg.event.get():
      if event.type == pg.QUIT:
        sys.exit()
    vindu.blit(shop_bakgrunnlist2[counter_shop],(0, 0))
    counter_shop += 1
    if counter_shop == 313:
      counter_shop = 0
    if back_button.draw():
        meny()
    s = pg.Surface((VINDU_BREDDE * (6/8),VINDU_HOYDE * (14/16)))  # the size of your rect
    s.set_alpha(128)                # alpha level
    s.fill((255, 255, 255))           # this fills the entire surface
    vindu.blit(s, (VINDU_BREDDE * (1/8), VINDU_HOYDE * (1/16)))           # (0,0) are the top-left coordinates
    bilde_shop = font.render('SHOP', True, (0, 0, 0))
    bilde_rect_shop = bilde_shop.get_rect(center=(VINDU_BREDDE/1.98, VINDU_HOYDE/9.6))
    vindu.blit(bilde_shop, (bilde_rect_shop))
    
    bilde_shop1 = font.render('SHOP', True, (255, 255, 255))
    bilde_rect_shop1 = bilde_shop1.get_rect(center=(VINDU_BREDDE/2, VINDU_HOYDE/10))
    vindu.blit(bilde_shop1, (bilde_rect_shop1))
    
    bilde_shop2 = font.render('OUT OF STOCK', True, (0, 0, 0))
    bilde_rect_shop2 = bilde_shop2.get_rect(center=(VINDU_BREDDE/1.98, VINDU_HOYDE/1.98))
    vindu.blit(bilde_shop2, (bilde_rect_shop2))
    
    bilde_shop3 = font.render('OUT OF STOCK', True, (255, 255, 255))
    bilde_rect_shop3 = bilde_shop3.get_rect(center=(VINDU_BREDDE/2, VINDU_HOYDE/2))
    vindu.blit(bilde_shop3, (bilde_rect_shop3))
    
    clock.tick(30)
    pg.display.flip()


def meny():
  global counter_meny
  fortsett = True
  MusicChannelGame.fadeout(1500)
  SoundEffectChannel.fadeout(100)
  while fortsett:
    if MusicChannel.get_busy() == False:
            meny_musikk = pg.mixer.Sound("Benjamin/Lyd/Daft Punk - Veridis Quo.mp3")
            meny_musikk.set_volume(0.5)
            MusicChannel.play(meny_musikk)
            
            
      # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
      if event.type == pg.QUIT:
        sys.exit()
    
    

    clock.tick(30)
    vindu.blit(bakgrunnlist2[counter_meny],(0, 0))
    counter_meny += 1
    if counter_meny == 112:
        counter_meny = 0

    if shop_button.draw():
        shop()

    if exit_button.draw():
        sys.exit()

    if start_button.draw():
      game()
    
    pg.display.flip()

while True:
  meny()

# Avslutter pygame
pg.quit()

#https://www.veed.io/convert/mp3-to-wav?utm_campaign=YouTube+Description+Tim&utm_medium=How+to+Convert+MP3+to+WAV+Free+Online+Video+Converter&utm_source=YouTube
#https://yt2mp3.info/?l=en