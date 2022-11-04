import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
from math import *
import random as random
import sys, time
import os
from pygame.locals import *
from random import choice

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
    pg.draw.rect(vindu, arena.farge, (arena.x, arena.y, arena.bredde, arena.bredde))

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

  def lage(self):
    global ping
    if klokke % 1000 == 0:
      pongs.append(Pong(random.randint(560,720),random.randint(100,250),choice([i for i in range(-8,8) if i not in [0]])/10,choice([i for i in range(-8,8) if i not in [0]])/10,45,45,vindu, (random.randint(0,255),random.randint(0,255),random.randint(0,255))))
  
  def tegn(self):
    global klokke
    """Metode for å tegne kvadratene"""
    for i in range(0,len(pongs)):
      pg.draw.rect(pongs[i].vindusobjekt, pongs[i].farge, (pongs[i].x, pongs[i].y, pongs[i].bredde, pongs[i].bredde))
      pg.draw.rect(plate.vindusobjekt, plate.farge, (plate.x, plate.y, plate.bredde, plate.høyde))


  def flytt(self):
    global fortsett
    global klokke
    clock.tick(1500)
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
          pongs[i].fartx = ((random.randint(1,6) / 10) + pongs[i].fartx)
        elif (pongs[i].y -3) < (plate.y + (plate.høyde / 2)) < (pongs[i].y + pongs[i].høyde + 3) and (pongs[i].x + pongs[i].bredde - 3) < plate.x < (pongs[i].x + pongs[i].bredde + 3):
          pongs[i].fartx = -1
        elif (pongs[i].y -3) < (plate.y + (plate.høyde / 2)) < (pongs[i].y + pongs[i].høyde + 3) and (pongs[i].x - 3) < (plate.x + plate.bredde) < (pongs[i].x + 3):
          pongs[i].fartx = 1
        pongs[i].x += pongs[i].fartx
        pongs[i].y += pongs[i].farty

  def bounce(self):
    global klokke
    clock.tick(1500)
    for i in range(0,len(pongs)):
      for o in range(0,len(pongs)):
        if pongs[o].x < (pongs[i].x) < (pongs[o].x + pongs[o].bredde) and (pongs[o].y - 1) < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + 1) or pongs[o].x < (pongs[i].x + pongs[i].bredde) < (pongs[o].x + pongs[o].bredde) and (pongs[o].y - 1) < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + 1):
          pongs[i].farty,pongs[o].farty = -pongs[i].farty,-pongs[o].farty
          pongs[i].fartx,pongs[o].fartx = -pongs[i].fartx,-pongs[o].fartx
        elif pongs[o].x < (pongs[i].x) < (pongs[o].x + pongs[o].bredde) and (pongs[o].y + pongs[o].høyde - 1) < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + pongs[o].høyde + 1) or pongs[o].x < (pongs[i].x + pongs[i].bredde) < (pongs[o].x + pongs[o].bredde) and (pongs[o].y + pongs[o].høyde - 1) < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + pongs[o].høyde + 1):
          pongs[i].farty,pongs[o].farty = -pongs[i].farty,-pongs[o].farty
          pongs[i].fartx,pongs[o].fartx = -pongs[i].fartx,-pongs[o].fartx
        elif pongs[o].y < (pongs[i].y) < (pongs[o].y + pongs[o].høyde) and (pongs[o].y - 1) < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + 1) or pongs[o].y < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + pongs[o].høyde) and (pongs[o].y - 1) < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + 1):
          pongs[i].farty,pongs[o].farty = -pongs[i].farty,-pongs[o].farty
          pongs[i].farty,pongs[o].farty = -pongs[i].farty,-pongs[o].farty
        elif pongs[o].y < (pongs[i].y) < (pongs[o].y + pongs[o].høyde) and (pongs[o].y + pongs[o].høyde - 1) < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + pongs[o].høyde + 1) or pongs[o].y < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + pongs[o].høyde) and (pongs[o].y + pongs[o].høyde - 1) < (pongs[i].y + pongs[i].høyde) < (pongs[o].y + pongs[o].høyde + 1):
          pongs[i].farty,pongs[o].farty = -pongs[i].farty,-pongs[o].farty
          pongs[i].farty,pongs[o].farty = -pongs[i].farty,-pongs[o].farty  


plate = Pong(0,650,0.8,0,1600,10,vindu,(255,255,255))


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
    plate.lage()
    plate.tegn()
    plate.bounce()
    plate.flytt()

    klokke += 1
    print(klokke)
    '''if klokke == 10000:
      pongs.append(pong2)
    if klokke == 20000:
      pongs.append(pong3)'''
    clock.tick(1000)

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygameas
pg.quit()