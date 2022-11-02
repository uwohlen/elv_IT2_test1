import pygame as pg

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 1280
VINDU_HOYDE  = 720
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

print(type(vindu))

class Arena:
  def __init__(self,x,y,bredde,høyde,farge):
    self.x = x
    self.y = y
    self.bredde = bredde
    self.høyde = høyde
    self.farge = farge
  def tegnarena(self):
    """Metode for å tegne arena"""
    pg.draw.rect(pong1.vindusobjekt, arena.farge, (arena.x, arena.y, arena.bredde, arena.bredde))

arena = Arena(360,0,560,720,(120,120,120))

    
class Pong:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fartx, farty, bredde, vindusobjekt, farge):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fartx = fartx
    self.farty = farty
    self.bredde = bredde
    self.vindusobjekt = vindusobjekt
    self.farge = farge
  
  def tegn(self):
    """Metode for å tegne kvadratene"""
    pg.draw.rect(pong1.vindusobjekt, pong1.farge, (pong1.x, pong1.y, pong1.bredde, pong1.bredde))

  def flytt(self):
    """Metode for å flytte kvadratene"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((pong1.x) <= arena.x) or ((pong1.x + pong1.bredde) >= arena.x + arena.bredde):
      pong1.fartx = -pong1.fartx
    elif ((pong1.y) <= arena.y) or ((pong1.y + pong1.bredde) >= arena.høyde):
      pong1.farty = -pong1.farty
    # Flytter pong1en
    pong1.x += pong1.fartx
    pong1.y += pong1.farty
    if ((pong2.x - pong2.bredde) <= arena.x) or ((pong2.x + pong2.bredde) >= arena.x + arena.bredde):
      pong2.fartx = -pong2.fartx
    elif ((pong2.y - pong2.bredde) <= arena.y) or ((pong2.y + pong2.bredde) >= arena.y + arena.høyde):
      pong2.farty = -pong2.farty
    # Flytter ballen
    pong2.x += pong2.fartx
    pong2.y += pong2.farty
    if ((pong3.x - pong3.bredde) <= 0) or ((pong3.x + pong3.bredde) >= pong3.vindusobjekt.get_width()):
      pong3.fartx = -pong3.fartx
    elif ((pong3.y - pong3.bredde) <= 0) or ((pong3.y + pong3.bredde) >= pong3.vindusobjekt.get_height()):
      pong3.farty = -pong3.farty
    # Flytter ballen
    pong3.x += pong3.fartx
    pong3.y += pong3.farty

pong1 = Pong(540, 540, 0.1, 0.1, 45, vindu, (255,255,255))
pong2 = Pong(360, 360, 0.5, 0, 20, vindu, (0,0,0))
pong3 = Pong(360, 360, 0, 0.5, 20, vindu, (0,0,0))

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
    vindu.fill((120, 120, 120))

    # Tegner et rektangel
    pg.draw.rect(vindu, (0, 0, 0), (360, 0, 560, 1280))
    pong1.tegn()
    pong1.flytt()


    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()