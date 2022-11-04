import pygame as pg

# Initialiserer/starter pygame
pg.init()

#Oppretter et vindu der innholdet blir "tegnet"
window_surface = pg.display.set_mode((800, 600))

print(type(window_surface))

FPS = 60 # frames per second setting
fpsClock = pg.time.Clock()

# Angir hvilken skrifttype og skriftstørrelse som skal brukes på teksten
font = pg.font.SysFont("dejavuserif", 30)

class Ball:
    # Klasse for å representere en ball
    def __init__(self, x, y, radius, farge, vindusobjekt):
        # Konstruktør
        self.x = x
        self.y = y
        self.radius = radius
        self.farge = farge
        self.vindusobjekt = vindusobjekt
  
    def tegn(self):
        # Metode for å tegne ballen
        pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 

class Spiller(Ball):
  #Klasse for å representere et hinder
  def __init__(self, x, y, radius, farge, vindusobjekt, xFart, yFart):
    super().__init__(x, y, radius, farge, vindusobjekt)
    self.xFart = xFart
    self.yFart = yFart

  def flytt(self):
    #Metode for å flytte hinderet
    # Sjekker om hinderet er utenfor høyre/venstre kant
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.xFart = -self.xFart
    
    # Sjekker om hinderet er utenfor øvre/nedre kant
    if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
      self.yFart = -self.yFart

    # Flytter hinderet
    self.x += self.xFart
    self.y += self.yFart

# Lager et Hinder-objekt
spiller = Spiller(150, 250, 20, (0, 0, 255), window_surface, 5.0, 5.0)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:
    
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
            
    # Farger bakgrunnen svart
    window_surface.fill((0, 0, 0))
    
    text = font.render("Abacus", True, (255, 255, 255))
    window_surface.blit(text, (100, 100))
    
    # Tegner og flytter ballen
    spiller.tegn()
    spiller.flytt()
    
    # Oppdaterer alt innholdet på vinduet
    pg.display.flip()
    
    # FPS
    fpsClock.tick(FPS)
    
# Avslutter pygame
pg.quit()