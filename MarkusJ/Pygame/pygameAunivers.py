# importerer pygame modulen som pg
import pygame as pg

#importerer de ulike tastene fra tastaturet
from pygame.locals import (K_UP, K_DOWN, K_w, K_s)


# starter pygame
pg.init()


# lager et vindu med bredde 1100 og høyde 750
VINDU_BREDDE = 1100
VINDU_HOYDE  = 750
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])


# setter begge scorene til 0
scoreLeft = 0
scoreRight = 0

# lager et font objekt
font = pg.font.Font('freesansbold.ttf', 52)


# lager tekst objekter
text1 = font.render('', True,(255,255,255))
text2 = font.render('', True, (255,255,255))



# Clager rektangler hvor teksten skal plasserers
textRect = text1.get_rect()
textRect2 = text2.get_rect()


# sentrerer teksten i rektangelene
textRect.center = ((VINDU_BREDDE//2)-120, VINDU_HOYDE // 2)
textRect2.center = ((VINDU_BREDDE//2)+50, VINDU_HOYDE // 2)




# lager en ball klasse med x-positsjonen ,y-posisjonen, farten i x rettning, farten i y rettning, radius, farge, og vinduet som brukes
class Ball:
  def __init__(self, x, y, fartx, farty, radius, farge, vindusobjekt):

    self.x = x
    self.y = y
    self.fartx = fartx
    self.farty = farty
    self.radius = radius
    self.farge = farge
    self.vindusobjekt = vindusobjekt

  #tegner sirkelen
  def tegn(self):
    pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 

  #funksjon for å flytte ballen
  def flytt(self):

    if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
        self.farty = -self.farty




# Moving the ball in the x and y direction.
    self.x -= self.fartx
    self.y -= self.farty




#lager en klasse med navn Ping. klassen inneholder x1,y1,x2,y2, fart, størrelse, farge og vinduet som brukes
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


# funksjon for å tegne den ene rekkerten
    def tegn(self):
      pg.draw.line(self.vindusobjekt, self.farge, (self.x1, self.y1), (self.x2, self.y2), self.størrelse )
    
#funksjon for å flytte den ene rekkerten
    def flytt(self, taster):
      if (self.y1 <= 0 or self.y2 >= self.vindusobjekt.get_height()):
        self.fart = 0

#hvis tasten "w" blir holdt ned så endrer rekkerten rettning
      if taster[K_w]:
        self.y1 -= self.fart
        self.y2 -= self.fart
#hvis tasten "s" blir holdt ned så endrer rekkerten rettning
      if taster[K_s]:
        self.y1 += self.fart
        self.y2 += self.fart

#funksjon som sjekker om rekkertens kant treffer kanten på vinduet
    def collision(self):
      if (self.y1 <= 0):
        self.fart = 0
        self.y1 = 1
        self.y2 = 151
        self.fart = 3
#funksjon som sjekker om rekkertens kant treffer kanten på vinduet
      elif (self.y2 >= self.vindusobjekt.get_height()):
        self.fart = 0
        self.y1 = 599
        self.y2 = 749
        self.fart = 3
    
#lager en klasse med navn Pong. klassen inneholder x1,y1,x2,y2, fart, størrelse, farge og vinduet som brukes
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


# funksjon for å tegne den ene rekkerten
    def tegn(self):
      pg.draw.line(self.vindusobjekt, self.farge, (self.x1, self.y1), (self.x2, self.y2), self.størrelse )
    

# funksjon for å flytte den ene rekkerten
    def flytt(self, taster):
#hvis pil opp tasten blir holdt ned så endrer rekkerten rettning
      if taster[K_UP]:
        self.y1 -= self.fart
        self.y2 -= self.fart
#hvis pil ned tasten blir holdt ned så endrer rekkerten rettning
      if taster[K_DOWN]:
        self.y1 += self.fart
        self.y2 += self.fart


#funksjon som sjekker om rekkertens kant treffer kanten på vinduet
    def collision(self):
      if (self.y1 <= 0):
        self.fart = 0
        self.y1 = 1
        self.y2 = 151
        self.fart = 3

#funksjon som sjekker om rekkertens kant treffer kanten på vinduet
      elif (self.y2 >= self.vindusobjekt.get_height()):
        self.fart = 0
        self.y1 = 599
        self.y2 = 749
        self.fart = 3
    
#en klasse for spiltteren i midten av sjermen
class Splitter:
    def __init__(self, x1, y1, x2, y2, størrelse, farge, vindusobjekt):
     self.x1 = x1
     self.y1 = y1
     self.x2 = x2
     self.y2 = y2
     self.størrelse = størrelse
     self.farge = farge
     self.vindusobjekt = vindusobjekt

#tegner linjen
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



#setter fargen på vinduet 
    vindu.fill((40, 40, 40))


 
    
#en metode for å skrive ut tekst på vidusobjektet
    vindu.blit(text1, textRect)
    vindu.blit(text2, textRect)

#kjører alle funksjonene
    splitter.tegn()

    ball.tegn()
    ball.flytt()

    ping.tegn()
    ping.flytt(trykkede_taster)
    ping.collision()

    pong.tegn()
    pong.flytt(trykkede_taster)
    pong.collision()


#sjekker om ballen treffer rekkerten til venstre
    if ((ball.x - ball.radius) <= 40 and (ball.y - ball.radius) <= ping.y2 and (ball.y - ball.radius) >= ping.y1):
        ball.fartx = -ball.fartx
        ball.farty = +ball.farty
#sjekker om ballen treffer rekkerten til høyre
    elif ((ball.x + ball.radius) >= 1060 and (ball.y + ball.radius) <= pong.y2 and (ball.y + ball.radius) >= pong.y1):
        ball.farty = +ball.farty
        ball.fartx = -ball.fartx

#setter ballen til midten når ballen har truffet venstre side av skjermen
    if ((ball.x - ball.radius) <= 0):
        scoreRight += 1
        ball.x = 550
        ball.y = 375

#setter ballen til midten når ballen har truffet høyre side av skjermen
    elif ((ball.x + ball.radius) >= ball.vindusobjekt.get_width()):
        scoreLeft += 1
        ball.x = 550
        ball.y = 375
        

#rendrer textene på skjermen
    score_text_left = font.render(str(scoreLeft), True, (255, 255, 255))
    vindu.blit(score_text_left, (275, 100))

    score_text_right = font.render(str(scoreRight), True, (255, 255, 255))
    vindu.blit(score_text_right, (775, 100))



#plusser høyre poengene med 1 hver gang ballen treffer den venstre siden av skjermen  
    if ((ball.x - ball.radius) <= 0):
      vindu.blit(score_text_right, (775, 100))
#plusser venstre poengene med 1 hver gang ballen treffer den høyre siden av skjermen 
    elif ((ball.x + ball.radius) >= 1100):
      vindu.blit(score_text_left, (275, 100))

#hvis poengene på venstre side er lik 10 så vinner venstre spiller
    if scoreLeft == 10:
      ball.farty = 0
      ball.fartx = 0
      ball.x = VINDU_BREDDE // 2
      ball.y = VINDU_HOYDE // 2
      ball.radius = 0
      text1 = font.render('BLUE WON', True,(0,0,255))
#hvis poengene på høyre side er lik 10 så vinner høyre side
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


