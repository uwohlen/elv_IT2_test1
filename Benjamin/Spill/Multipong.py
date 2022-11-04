import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as ma
import random as random
import sys, time
import os
from pygame.locals import *

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1280
VINDU_HOYDE  = 720
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])
print(type(vindu))

klokke = 0
clock = pg.time.Clock()
pongs = []

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
    for i in range(0,len(pongs)):
      pg.draw.rect(pongs[i].vindusobjekt, pongs[i].farge, (pongs[i].x, pongs[i].y, pongs[i].bredde, pongs[i].bredde))
      pg.draw.rect(plate.vindusobjekt, plate.farge, (plate.x, plate.y, plate.bredde, plate.høyde))


  def flytt(self):
    global fortsett
    global klokke
    """Metode for å flytte kvadratene"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    for i in range(0,len(pongs)):
        if ((pongs[i].x) <= arena.x) or ((pongs[i].x + pongs[i].bredde) >= arena.x + arena.bredde):
          pongs[i].fartx = -pongs[i].fartx
        elif ((pongs[i].y) <= arena.y):
          pongs[i].farty = -pongs[i].farty
        elif ((pongs[i].y + pongs[i].høyde) >= arena.høyde):
          fortsett = False
        elif plate.x < (pongs[i].x) < (plate.x + plate.bredde) and (plate.y - 1) < (pongs[i].y + pongs[i].høyde) < (plate.y + 1) or plate.x < (pongs[i].x + pongs[i].bredde) < (plate.x + plate.bredde) and (plate.y - 1) < (pongs[i].y + pongs[i].høyde) < (plate.y + 1):
          pongs[i].farty = -pongs[i].farty
          pongs[i].fartx = random.randint(1,6) / 10 + pongs[i].fartx
        elif pongs[i].y < (plate.y + plate.høyde / 2) < (pongs[i].y + pongs[i].høyde) and (pongs[i].x + pongs[i].bredde - 1) < plate.x < (pongs[i].x + pongs[i].bredde + 1):
          pongs[i].farty = -pongs[i].farty
          pongs[i].fartx = -(random.randint(1,6) / 10 + pongs[i].fartx)
          plate.x += 10*plate.fartx
        elif pongs[i].y < (plate.y + plate.høyde / 2) < (pongs[i].y + pongs[i].høyde) and (pongs[i].x - 1) < (plate.x + plate.bredde) < (pongs[i].x + 1):
          pongs[i].farty = -pongs[i].farty
          pongs[i].fartx = -(random.randint(1,6) / 10 + pongs[i].fartx)
          plate.x -= 10*plate.fartx
        # Flytter pong1en
        pongs[i].x += pongs[i].fartx
        pongs[i].y += pongs[i].farty


pong1 = Pong(540, 540, 0.3, 0.3, 45, 45, vindu, (255,255,255))
pong2 = Pong(618, 338, 0.3, 0.3, 45,45, vindu, (255,0,0))
pong3 = Pong(618, 338, -0.3, -0.3, 45,45, vindu, (0,255,0))
plate = Pong(595,650,0.8,0,90,10,vindu,(255,255,255))
platebox = Pong(685,650,0.4,0,0,0,vindu,(255,255,255))

pongs.append(pong1)

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
    if klokke == 10000:
      pongs.append(pong2)
    if klokke == 20000:
      pongs.append(pong3)


    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygameas
pg.quit()