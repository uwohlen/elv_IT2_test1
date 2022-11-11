import pygame as pg
import math as ma
import random as r
import sys, time
import os
from pygame.locals import *

# Initialiserer/starter pygame
pg.init()
gifList = []
gifList2 = []
counter = 0
clock = pg.time.Clock()
# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1280
VINDU_HOYDE  = 720
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

print(type(vindu))
for i in range(2):
    gifList.append(pg.image.load(f"Benjamin/pngs/måneskin/måneskin-{i}.png"))
for i in range(-1,1):
    gifList2.append(pg.transform.scale(gifList[i], (1280, 720)))

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    clock.tick(2)
    vindu.blit(gifList2[counter],(0, 0))
    counter += 1
    if counter == 2:
        counter = 0
    print(counter)
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygamesscxdsjghghg
pg.quit()

#https://www.cleverpdf.com/gif-to-png
#https://www.dafont.com/top.php