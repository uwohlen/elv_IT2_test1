import pygame as pg
from pygame.locals import (K_LEFT, K_RIGHT)
import math as m

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])


class Hinder():
  """Klasse for å representere et hinder"""
  def __init__(self, x, y, radius, farge, vindusobjekt, xFart, yFart):
    self.x = x
    self.y = y
    self.radius = radius
    self.farge = farge
    self.vindusobjekt = vindusobjekt
    self.xFart = xFart
    self.yFart = yFart

  def flytt(self):
    """Metode for å flytte hinderet"""
    # Sjekker om hinderet er utenfor høyre/venstre kant
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.xFart = -self.xFart
    
    # Sjekker om hinderet er utenfor øvre/nedre kant
    if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
      self.yFart = -self.yFart

    # Flytter hinderet
    self.x += self.xFart
    self.y += self.yFart

  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 


class Spiller():
  """Klasse for å representere en spiller"""
  def __init__(self, x, y, lengde, farge, vindusobjekt, fart):
      self.x = x
      self.y = y
      self.lengde = lengde
      self.farge = farge
      self.vindusobjekt = vindusobjekt
      self.fart = fart

  def flytt(self, taster):
    """Metode for å flytte spilleren"""
    
    if taster[K_LEFT]:
      self.x -= self.fart
    if taster[K_RIGHT]:
      self.x += self.fart

  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.line(self.vindusobjekt, self.farge, (self.x, self.y), (self.x+self.lengde, self.y)) 

# Lager et Spiller-objekt
spiller = Spiller(200, 470, 100, (255, 69, 0), vindu, 0.1)
# Lager et Hinder-objekt
hinder = Hinder(150, 250, 20, (0, 0, 255), vindu, 0.08, 0.12)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Henter en ordbok med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))

    # Tegner og flytter spiller og hinder
    spiller.tegn()
    spiller.flytt(trykkede_taster)
    hinder.tegn()
    hinder.flytt()


    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()