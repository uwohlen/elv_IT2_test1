import pygame as pg
import math as ma

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1280
VINDU_HOYDE  = 720
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

print(type(vindu))

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fartx, farty, radius, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fart = fartx
    self.fart = farty
    self.radius = radius
    self.vindusobjekt = vindusobjekt
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, (255, 69, 0), (self.x, self.y), self.radius) 

  def flytt(self):
    """Metode for å flytte ballen"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.fartx = -self.fartx
    elif ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
      self.farty = -self.farty
    # Flytter ballen
    self.x += self.fartx
    self.y += self.farty

# Lager et Ball-objekt
ball = Ball(250, 250, 0.1, 20, vindu)

# Angir hvilken skrifttype og tekststørrelse vi vil bruke på tekst
font = pg.font.SysFont("Arial", 24)

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
    pg.draw.circle(vindu, (255, 100, 50), (645, 360), 150)
    # Tegner et rektangel
    pg.draw.rect(vindu, (0, 255, 0), (0, 520, 1280, 720))
    pg.draw.rect(vindu, (0, 255, 0), (0, 0, 1280, 200))
    # Tegner en ellipse
    '''pg.draw.ellipse(vindu, (0, 0, 255), (300, 250, 90, 60))'''
    # Tegner en linje
    '''pg.draw.line(vindu, (200, 0, 200), (400, 100), (420, 400), 5)'''

    # Lager en tekst i form av et bilde og legger til bildet i vinduet
    '''bilde = font.render("Heisann!", True, (50, 50, 50))
    vindu.blit(bilde, (400, 20))'''
    # Tegner og flytter ballen
    ball.tegn()
    ball.flytt()

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygamesscxdsjghghg
pg.quit()