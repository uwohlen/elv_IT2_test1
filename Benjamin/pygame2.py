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
  def __init__(self, x, y, fartx, farty, radius, vindusobjekt, farge):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fartx = fartx
    self.farty = farty
    self.radius = radius
    self.vindusobjekt = vindusobjekt
    self.farge = farge
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(ball.vindusobjekt, ball.farge, (ball.x, ball.y), ball.radius)
    pg.draw.circle(ball2.vindusobjekt, ball2.farge, (ball2.x, ball2.y), ball2.radius)
    pg.draw.circle(ball3.vindusobjekt, ball3.farge, (ball3.x, ball3.y), ball3.radius)

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
ball = Ball(250, 250, 0.1, 0.1, 20, vindu, (0,0,0))
ball2 = Ball(360, 360, 0.1, 0, 20, vindu, (0,0,0))
ball3 = Ball(360, 360, 0, 0.1, 20, vindu, (0,0,0))

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
    '''pg.draw.circle(vindu, (255, 100, 50), (645, 360), 150)'''
    # Tegner et rektangel
    pg.draw.rect(vindu, (255, 0, 0), (0, 0, 1280, 270))
    pg.draw.rect(vindu, (255, 0, 0), (0, 450, 1280, 720))
    pg.draw.rect(vindu, (255, 255, 255), (270, 0, 180, 720))
    pg.draw.rect(vindu, (0, 0, 255), (0, 315, 1280, 90))
    pg.draw.rect(vindu, (0, 0, 255), (315, 0, 90, 720))
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