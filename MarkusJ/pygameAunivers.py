import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_w, K_s)

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1100
VINDU_HOYDE  = 750
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])


scoreLeft = 0
scoreRight = 0

font = pg.font.Font('freesansbold.ttf', 52)

text1 = font.render('', True,(255,255,255))
text2 = font.render('', True, (255,255,255))



textRect = text1.get_rect()
textRect2 = text2.get_rect()


# set the center of the rectangular object.
textRect.center = ((VINDU_BREDDE//2)-120, VINDU_HOYDE // 2)
textRect2.center = ((VINDU_BREDDE//2)+50, VINDU_HOYDE // 2)


class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fartx, farty, radius, farge, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fartx = fartx
    self.farty = farty
    self.radius = radius
    self.farge = farge
    self.vindusobjekt = vindusobjekt

  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 

  def flytt(self):
    """Metode for å flytte ballen"""
    # Sjekker om ballen er utenfor høyre/venstre kant



    if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
        self.farty = -self.farty





    # Flytter ballen
    self.x -= self.fartx
    self.y -= self.farty




class Ping:
    def __init__(self, x1, y1, x2, y2, fart, størrelse, farge, vindusobjekt):
     self.x1 = x1
     self.y1 = y1
     self.x2 = x2
     self.y2 = y2
     self.fart = fart
     self.størrelse = størrelse
     self.farge = farge
     self.vindusobjekt = vindusobjekt


    def tegn(self):
      pg.draw.line(self.vindusobjekt, self.farge, (self.x1, self.y1), (self.x2, self.y2), self.størrelse )
    
    def flytt(self, taster):
      if (self.y1 <= 0 or self.y2 >= self.vindusobjekt.get_height()):
        self.fart = 0

      if taster[K_w]:
        self.y1 -= self.fart
        self.y2 -= self.fart
      if taster[K_s]:
        self.y1 += self.fart
        self.y2 += self.fart


    def collision(self):
      if (self.y1 <= 0):
        self.fart = 0
        self.y1 = 1
        self.y2 = 151
        self.fart = 3

      elif (self.y2 >= self.vindusobjekt.get_height()):
        self.fart = 0
        self.y1 = 599
        self.y2 = 749
        self.fart = 3
    

class Pong:
    def __init__(self, x1, y1, x2, y2, fart, størrelse, farge, vindusobjekt):
     self.x1 = x1
     self.y1 = y1
     self.x2 = x2
     self.y2 = y2
     self.fart = fart
     self.størrelse = størrelse
     self.farge = farge
     self.vindusobjekt = vindusobjekt


    def tegn(self):
      pg.draw.line(self.vindusobjekt, self.farge, (self.x1, self.y1), (self.x2, self.y2), self.størrelse )
    
    def flytt(self, taster):

      if taster[K_UP]:
        self.y1 -= self.fart
        self.y2 -= self.fart
      if taster[K_DOWN]:
        self.y1 += self.fart
        self.y2 += self.fart


    def collision(self):
      if (self.y1 <= 0):
        self.fart = 0
        self.y1 = 1
        self.y2 = 151
        self.fart = 3

      elif (self.y2 >= self.vindusobjekt.get_height()):
        self.fart = 0
        self.y1 = 599
        self.y2 = 749
        self.fart = 3
    

class Splitter:
    def __init__(self, x1, y1, x2, y2, størrelse, farge, vindusobjekt):
     self.x1 = x1
     self.y1 = y1
     self.x2 = x2
     self.y2 = y2
     self.størrelse = størrelse
     self.farge = farge
     self.vindusobjekt = vindusobjekt


    def tegn(self):
      pg.draw.line(self.vindusobjekt, self.farge, (self.x1, self.y1), (self.x2, self.y2), self.størrelse )
    
    

    

# Lager objekter
ball = Ball(VINDU_BREDDE//2, VINDU_HOYDE//2, 1.5, 1.5, 20, (40,200,40), vindu)

ping = Ping(30,300,30,450,3,20,(40,40,200), vindu)

pong = Pong(1070,300,1070,450,3,20,(200,40,40), vindu)

splitter = Splitter(VINDU_BREDDE//2,0,VINDU_BREDDE//2,1100,10,(200,200,200), vindu)




# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    trykkede_taster = pg.key.get_pressed()



    vindu.fill((40, 40, 40))


 
    
    vindu.blit(text1, textRect)
    vindu.blit(text2, textRect)


    splitter.tegn()

    ball.tegn()
    ball.flytt()

    ping.tegn()
    ping.flytt(trykkede_taster)
    ping.collision()

    pong.tegn()
    pong.flytt(trykkede_taster)
    pong.collision()


    if ((ball.x - ball.radius) <= 40 and (ball.y - ball.radius) <= ping.y2 and (ball.y - ball.radius) >= ping.y1):
        ball.fartx = -ball.fartx
        ball.farty = +ball.farty

    elif ((ball.x + ball.radius) >= 1060 and (ball.y + ball.radius) <= pong.y2 and (ball.y + ball.radius) >= pong.y1):
        ball.farty = +ball.farty
        ball.fartx = -ball.fartx
    
    if ((ball.x - ball.radius) <= 0):
        scoreRight += 1
        ball.x = 550
        ball.y = 375
    
    elif ((ball.x + ball.radius) >= ball.vindusobjekt.get_width()):
        scoreLeft += 1
        ball.x = 550
        ball.y = 375
        

    score_text_left = font.render(str(scoreLeft), True, (255, 255, 255))
    vindu.blit(score_text_left, (275, 100))

    score_text_right = font.render(str(scoreRight), True, (255, 255, 255))
    vindu.blit(score_text_right, (775, 100))

    if ((ball.x - ball.radius) <= 0):
      vindu.blit(score_text_right, (775, 100))
    
    elif ((ball.x + ball.radius) >= 1100):
      vindu.blit(score_text_left, (275, 100))


    if scoreLeft == 10:
      ball.farty = 0
      ball.fartx = 0
      ball.x = VINDU_BREDDE // 2
      ball.y = VINDU_HOYDE // 2
      ball.radius = 0
      text1 = font.render('BLUE WON', True,(0,0,255))

    elif scoreRight == 10:
      text2 = font.render('RED WON', True,(255,0,0))
      ball.farty = 0
      ball.fartx = 0
      ball.radius = 0
      ball.x = VINDU_BREDDE // 2
      ball.y = VINDU_HOYDE // 2



  

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()


