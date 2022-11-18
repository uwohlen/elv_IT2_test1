import pygame as pg
import math as m
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, xfart, yfart, lengde, høyde, vindusobjekt , R = 255,G = 69,B = 0):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.xfart = xfart
    self.yfart = yfart
    self.lengde = lengde
    self.høyde = høyde
    self.vindusobjekt = vindusobjekt
    self.R = R
    self.G = G
    self.B = B
  
  def tegn(self):
    """Metode for å tegne rektangel"""
    pg.draw.rect(self.vindusobjekt, (self.R, self.G, self.B), (self.x, self.y, self.lengde, self.høyde)) 

  def flytt_x(self):
    """Metode for å flytte rektangel"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((self.x - self.lengde) <= 0) or ((self.x + self.lengde) >= self.vindusobjekt.get_width()):
      self.xfart = -self.xfart
      # Flytter ballen
    self.x += self.xfart

  def flytt_y(self):
    "flytte ballen opp"
    if ((self.y - self.høyde) <= 0) or ((self.y + self.høyde) >= self.vindusobjekt.get_height()):
      self.yfart = -self.yfart
    self.y +=self.yfart

# Lager et Ball-objekt
ball1 = Ball(350, 450, 0, 0, 50, 20, vindu)
ball2 = Ball(300, 200, 1, 1, 20, 20, vindu)
ball3 = Ball(100, 200, 1, 1, 20, 20, vindu)


# def finn_avstand(obj1, obj2):
#   xAvstand2 = (obj1.x - obj2.x)**2  # x-avstand i andre
#   yAvstand2 = (obj1.y - obj2.y)**2  # y-avstand i andre
#   avstand = m.sqrt(xAvstand2 + yAvstand2)
#   if avstand <= obj1.lengde + obj2.lengde:
#     obj1.yfart = -obj1.yfart
#     obj1.xfart = -obj1.xfart
#     obj2.yfart = -obj2.yfart
#     obj2.xfart = -obj2.xfart
#   return avstand

def finn_avstand(obj1, obj2):
  xavstand = (obj1.x - obj2.x)
  yavstand = (obj1.y-obj2.y)


# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:
    pg.time.Clock().tick(120)
    #finn_avstand(ball1, ball2)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    
    
    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235 ))

    # Tegner og flytter ballen
    ball1.tegn()
    ball1.flytt_x()
    ball1.flytt_y()

    ball2.tegn()
    ball2.flytt_x()
    ball2.flytt_y()

    # ball3.tegn()
    # ball3.flytt_x()
    # ball3.flytt_y()

    # Kollisjon
    player_top = ball1.y
    player_side_right = ball1.x
    player_side_left = -ball1.x
    player_position = ball1.x + ball1.y
    ball_bottom = ball2.y + ball2.høyde
    ball_side_left = ball2.x
    ball_side_right = -ball2.x
    ball_position = ball2.x + ball2.y

    if player_top <= ball_bottom and player_side_right <= ball_side_left:
      ball2.yfart = -ball2.yfart
    # elif player_top <= ball_bottom and player_side_right <= ball_side_right:
    #   ball2.yfart = -ball2.yfart
    
    # if ball2.y < ball1.y + ball1.høyde and \
    #             ball2.høyde + ball2.y > ball1.y:
    #         if ball2.x < ball1.x + ball1.width and \
    #                 ball2.x + ball2.width > ball1.x:
    
     #Bevegelse
    trykkede_taster = pg.key.get_pressed()

    if trykkede_taster[K_RIGHT]:
      ball1.x = ball1.x + 2
    if trykkede_taster[K_LEFT]:
      ball1.x = ball1.x - 2
      
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()