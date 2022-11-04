import os, sys, time, random, pygame, pylab, pandas

import pygame as pg

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1366
VINDU_HOYDE  = 768
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

print(type(vindu))

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 30)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen hvit
    vindu.fill((255, 255, 255))

    # Tegner en sirkel
    pg.draw.circle(vindu, (255, 50, 2), (200, 250), 90)
    # Tegner et rektangel
    pg.draw.rect(vindu, (0, 255, 0), (200, 250, 70, 90))
    # Tegner en ellipse
    pg.draw.ellipse(vindu, (0, 0, 255), (300, 250, 90, 60))
    # Tegner en linje
    pg.draw.line(vindu, (90, 10, 150), (200, 100), (420, 400), 5)

    # Lager en tekst i form av et bilde og legger til bildet i vinduet
    bilde = font.render("buger king!", True, (100, 50, 50))
    vindu.blit(bilde, (400, 90))

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()