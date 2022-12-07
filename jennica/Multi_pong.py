import pygame as pg
import pygame, sys
from pygame.locals import (K_LEFT, K_RIGHT)
import math as m
import random

pg.init()


VINDU_BREDDE = 500
VINDU_HOYDE = 600
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

score = 0
highscore = 0

font1 = pygame.font.Font('freesansbold.ttf', 52)
font2 = pygame.font.Font('freesansbold.ttf', 20)
tekst1 = font1.render('Game Over', True, (255, 255, 255))
tekst2 = font2.render('Quit Game', True, (255, 255, 255))



class Ball:
  # klasse for å representere en ball
  def __init__(self, x, y, xFart, yFart, lengde, bredde, vindusobjekt):
    # konstruktør
    self.x = x
    self.y = y
    self.xFart = xFart
    self.yFart = yFart
    self.lengde = lengde
    self.bredde = bredde
    self.vindusobjekt = vindusobjekt
  
  def tegn(self):
    # metode for å tegne ballen
    pg.draw.rect(self.vindusobjekt, (255, 69, 0), (self.x, self.y), self.lengde, self.bredde) 

  def flytt(self):
    global slutt
    # metode for å flytte ballen
    # Sjekker om ballen er utenfor høyre/venstre kant
    if (self.x <= 0) or ((self.x + self.lengde) >= self.vindusobjekt.get_width()):
      self.xFart = -self.xFart
    
    # Sjekker om ballen er utenfor øvre/nedre kant
    if (self.y <= 0):
        self.yFart = -self.yFart

    if ((self.y + self.bredde) >= self.vindusobjekt.get_height()):
        slutt=True
    # Flytter ballen
    self.x += self.xFart
    self.y += self.yFart

  def tegn(self):
        pg.draw.rect(vindu, (92, 172, 238), (self.x, self.y, self.lengde, self.bredde))


def ny_ball(nyBall):
    baller = Ball(random.randint(0, 470), 150, 1, 1, 30, 30, vindu)
    nyBall .append(baller)


class Blokk:
    def __init__(self, x, y, fart, bredde, lengde, vindusobjekt):
        self.x = x
        self.y = y
        self.fart = fart
        self.bredde = bredde
        self.lengde = lengde
        self.vindusobjekt = vindusobjekt

    def flytt(self, taster):
        if ((self.x) < 0):
            if taster[K_RIGHT]:
                self.x += self.fart
        elif (self.x + self.bredde) > self.vindusobjekt.get_width():
            if taster[K_LEFT]:
                self.x -= self.fart
        
        else:
            if taster[K_LEFT]:
                self.x -= self.fart
            if taster[K_RIGHT]:
                self.x += self.fart

    def tegn(self):
        pg.draw.rect(vindu, (154, 50, 205), (self.x, self.y, self.bredde, self.lengde))


    def kollisjon(self, ball):
        global slutt
        for ball in baller:
            if (ball.x>self.x) and \
                (ball.x+ball.lengde<self.x+self.bredde) and \
                (ball.y+ball.lengde>self.y) and \
                (ball.y+ball.lengde<self.y+self.lengde):
                ball.yFart = -ball.yFart
                ball.y = self.y -ball.bredde
                ny_ball(baller)
                global score
                if not slutt:
                    score += 1
                



baller = []
ball = Ball(150, 250, 1, 1, 30, 30, vindu)
blokk = Blokk(170, 550, 4, 150, 30, vindu)
ny_ball(baller)

slutt =False
fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False    
            pg.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 100 <= mouse[0] <= 220 and 300<= mouse[1] <= 340 and slutt:
                    pg.quit()
            elif vindu.get_width()-(80+120) <= mouse[0] <= vindu.get_width()-(80+120)+120 and 300<= mouse[1] <= 340 and slutt:
                baller = []
                ball = Ball(150, 250, 1, 1, 30, 30, vindu)
                score = 0
                ny_ball(baller)
                slutt = False



    trykkede_taster = pg.key.get_pressed()

    mouse = pygame.mouse.get_pos()

    vindu.fill((31, 31, 31))
    score_text_ingame = font2.render('din score: ' + str(score), True, (255, 255, 255))
    vindu.blit(score_text_ingame, (20, 20))

    blokk.tegn()
    blokk.flytt(trykkede_taster)
    blokk.kollisjon(baller)
    for ball in baller:
        ball.tegn()
        ball.flytt()
    if slutt:
        vindu.fill((0, 0, 0))
        vindu.blit(tekst1, (100, 200))
        pg.draw.rect(vindu, (131,139,139),[100, 300, 120 , 40])

        vindu.blit(tekst2 , (107, 314))
        score_text = font2.render('din score: ' + str(score), True, (255, 255, 255))
        vindu.blit(score_text, (110, 160))

        pg.draw.rect(vindu, (131,139,139),[vindu.get_width()-(80+120), 300, 120 , 40])
        score_text_2 = font2.render('Restart', True, (255, 255, 255))
        vindu.blit(score_text_2, (vindu.get_width()-(80+120)+10, 314))

    pg.display.flip()

pg.quit()


