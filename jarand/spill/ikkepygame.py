import random
import math
import pygame as pg
from pygame.locals import *
import sys

#initsialisere pygame
pg.init()

WINDOW_WIDTH = 800
WINDOW_LENGTH = 600

window = pg.display.set_mode([WINDOW_WIDTH,WINDOW_LENGTH])
font = pg.font.SysFont("Arial", 24)

def sirkel(x):
    for i in range(x):
        pg.draw.circle(window,(255, 0, 0),(random.randint(0,WINDOW_WIDTH),random.randint(0,WINDOW_LENGTH)),10)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
vegg = False
tak = False
x = 0
y = 0
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
           
    # Farger bakgrunnen hvit
    window.fill((255, 255, 255))

    sirkel(50)

    # Tegner et rektangel
    pg.draw.rect(window, (0, 255, 0), (200, 250, 70, 90))

    # Tegner en ellipse
    pg.draw.ellipse(window, (0, 0, 255), (x, y, 90, 60))
    

    # Tegner en linje
    pg.draw.line(window, (200, 0, 200), (400, 100), (420, 400), 5)

    # Lager en tekst i form av et bilde og legger til bildet i vinduet
    bilde = font.render("GAMER!", True, (15, 15, 15))
    window.blit(bilde, (400, 20))

    pg.display.flip()
    if vegg == False:
        x += 0.2
        if x > WINDOW_WIDTH-90:
            vegg = True
    else:
        x -= 0.2
        if x < 0:
            vegg = False
    
    if tak == False:
        y += 0.4
        if y > WINDOW_LENGTH-50:
            tak = True
    else:
        y -= 0.4
        if y < 0:
            tak = False
    
pg.quit()
sys.exit()
    
