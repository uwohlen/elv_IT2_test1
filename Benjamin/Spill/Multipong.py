import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as ma

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1280
VINDU_HOYDE  = 720
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
klokke = 0
print(type(vindu))

class Arena:
  def __init__(self,x,y,bredde,høyde,farge):
    self.x = x
    self.y = y
    self.bredde = bredde
    self.høyde = høyde
    self.farge = farge
  def tegnarena(self):
    """Metode for å tegne arena"""
    pg.draw.rect(pong1.vindusobjekt, arena.farge, (arena.x, arena.y, arena.bredde, arena.bredde))

arena = Arena(360,0,560,720,(120,120,120))

    
class Pong:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fartx, farty, bredde, høyde, vindusobjekt, farge):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fartx = fartx
    self.farty = farty
    self.bredde = bredde
    self.høyde = høyde
    self.vindusobjekt = vindusobjekt
    self.farge = farge
  
  def tegn(self):
    global klokke
    """Metode for å tegne kvadratene"""
    pg.draw.rect(pong1.vindusobjekt, pong1.farge, (pong1.x, pong1.y, pong1.bredde, pong1.bredde))
    if klokke > 10000:
      pg.draw.rect(pong2.vindusobjekt, pong2.farge, (pong2.x, pong2.y, pong2.bredde, pong2.bredde))
    if klokke > 20000:
      pg.draw.rect(pong3.vindusobjekt, pong3.farge, (pong3.x, pong3.y, pong3.bredde, pong3.bredde))
    pg.draw.rect(plate.vindusobjekt, plate.farge, (plate.x, plate.y, plate.bredde, plate.høyde))


  def flytt(self):
    global fortsett
    global klokke
    """Metode for å flytte kvadratene"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((pong1.x) <= arena.x) or ((pong1.x + pong1.bredde) >= arena.x + arena.bredde):
      pong1.fartx = -pong1.fartx
    elif ((pong1.y) <= arena.y):
      pong1.farty = -pong1.farty
    elif ((pong1.y + pong1.høyde) >= arena.høyde):
      fortsett = False
    elif plate.x < (pong1.x) < (plate.x + plate.bredde) and (plate.y - 1) < (pong1.y + pong1.høyde) < (plate.y + 1) or plate.x < (pong1.x + pong1.bredde) < (plate.x + plate.bredde) and (plate.y - 1) < (pong1.y + pong1.høyde) < (plate.y + 1):
      pong1.farty = -pong1.farty
    # Flytter pong1en
    pong1.x += pong1.fartx
    pong1.y += pong1.farty
    # pong2
    if klokke > 10000:
      if ((pong2.x) <= arena.x) or ((pong2.x + pong2.bredde) >= arena.x + arena.bredde):
        pong2.fartx = -pong2.fartx
      elif ((pong2.y) <= arena.y):
        pong2.farty = -pong2.farty
      elif ((pong2.y + pong2.høyde) >= arena.høyde):
        fortsett = False
      elif plate.x < (pong2.x) < (plate.x + plate.bredde) and (plate.y - 1) < (pong2.y + pong2.høyde) < (plate.y + 1) or plate.x < (pong2.x + pong2.bredde) < (plate.x + plate.bredde) and (plate.y - 1) < (pong2.y + pong2.høyde) < (plate.y + 1):
        pong2.farty = -pong2.farty
      # Flytter pong1en
      pong2.x += pong2.fartx
      pong2.y += pong2.farty
    # pong3
    if klokke > 20000:
      if ((pong3.x) <= arena.x) or ((pong3.x + pong3.bredde) >= arena.x + arena.bredde):
        pong3.fartx = -pong3.fartx
      elif ((pong3.y) <= arena.y):
        pong3.farty = -pong3.farty
      elif ((pong3.y + pong3.høyde) >= arena.høyde):
        fortsett = False
      elif plate.x < (pong3.x) < (plate.x + plate.bredde) and (plate.y - 1) < (pong3.y + pong3.høyde) < (plate.y + 1) or plate.x < (pong3.x + pong3.bredde) < (plate.x + plate.bredde) and (plate.y - 1) < (pong3.y + pong3.høyde) < (plate.y + 1):
        pong3.farty = -pong3.farty
      # Flytter pong1en
      pong3.x += pong3.fartx
      pong3.y += pong3.farty


pong1 = Pong(540, 540, 0.3, 0.3, 45, 45, vindu, (255,255,255))
pong2 = Pong(618, 338, 0.3, 0.3, 45,45, vindu, (255,0,0))
pong3 = Pong(618, 338, -0.3, -0.3, 45,45, vindu, (0,255,0))
plate = Pong(595,650,0.4,0,90,10,vindu,(255,255,255))
platebox = Pong(685,650,0.4,0,0,0,vindu,(255,255,255))

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24) 

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Henter en ordbok med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()

    # Farger bakgrunnen hvit
    vindu.fill((120, 120, 120))

    # Tegner et rektangel
    pg.draw.rect(vindu, (0, 0, 0), (360, 0, 560, 1280))

    # styrer platen
    if trykkede_taster[K_LEFT]:
      if plate.x < arena.x:
        plate.x += plate.fartx
      plate.x -= plate.fartx
    if trykkede_taster[K_RIGHT]:
      if (plate.x + plate.bredde) > (arena.x + arena.bredde):
        plate.x -= plate.fartx
      plate.x += plate.fartx
    pong1.tegn()
    pong1.flytt()

    klokke += 1
    print(klokke)


    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygameas
pg.quit()