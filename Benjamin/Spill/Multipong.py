import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as ma

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1280
VINDU_HOYDE  = 720
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

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
    """Metode for å tegne kvadratene"""
    pg.draw.rect(pong1.vindusobjekt, pong1.farge, (pong1.x, pong1.y, pong1.bredde, pong1.bredde))
    pg.draw.rect(plate.vindusobjekt, plate.farge, (plate.x, plate.y, plate.bredde, plate.høyde))


  def flytt(self):
    """Metode for å flytte kvadratene"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((pong1.x) <= arena.x) or ((pong1.x + pong1.bredde) >= arena.x + arena.bredde):
      pong1.fartx = -pong1.fartx
    elif ((pong1.y) <= arena.y) or ((pong1.y + pong1.bredde) >= arena.høyde):
      pong1.farty = -pong1.farty
    elif plate.x < (pong1.x) < (plate.x + plate.bredde) and (plate.y - 1) < (pong1.y + pong1.høyde) < (plate.y + 1) or plate.x < (pong1.x + pong1.bredde) < (plate.x + plate.bredde) and (plate.y - 1) < (pong1.y + pong1.høyde) < (plate.y + 1):
      pong1.farty = -pong1.farty
    # Flytter pong1en
    pong1.x += pong1.fartx
    pong1.y += pong1.farty


pong1 = Pong(540, 540, 0.3, 0.3, 45, 45, vindu, (255,255,255))
pong2 = Pong(360, 360, 0.5, 0, 20,0, vindu, (0,0,0))
pong3 = Pong(360, 360, 0, 0.5, 20,0, vindu, (0,0,0))
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


    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygameas
pg.quit()