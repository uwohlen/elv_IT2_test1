import pygame as pg
import random as rnd

pg.init()

height = 500
width = 500

wind = pg.display.set_mode([height, width])
font = pg.font.SysFont("Arial", 16)
clock = pg.time.Clock()


class ball:
    # definer variablene til ballene
    def __init__(self, x, y, r, v, window):
        self.x = x
        self.y = y
        self.r = r
        self.v = v
        self.window = window
        
    # tegne ballen i vinduen hvr x og y variablene plasserer den
    def draw(self):
        pg.draw.circle(self.window, (255, 0, 0), (self.x, self.y), self.r)
    
    # flytte ballen et hvis mengde per frame og da inverter farten når den treffer en vegg
    def move(self):
        if (self.x - self.r) <= 0 or (self.x + self.r) >= self.window.get_width():
            self.v[0] = -self.v[0]
        if (self.y - self.r) <= 0 or (self.y + self.r) >= self.window.get_height():
            self.v[1] = -self.v[1]
        
        self.x += self.v[0]
        self.y += self.v[1]
        
vx = 2.5
vy = 2.5


balls = [ball(250, 200, 10, [2.5, 3.2], wind)]
# definer spilleren som en Rect klasse fra pygame
box = pg.Rect(200, 450, 100, 15)
v = 10
cont = True
counter = 0
score = 0
while cont:
    
    # lukke vinuden hvis spilleren trykker på kryssen
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cont = False
    
    # få tastaturknappene som er presset
    keys = pg.key.get_pressed()
    
    # flytt spilleren venstre eller høyre basert på pilknappene
    if keys[pg.K_LEFT]:
        box.move_ip(-v, 0)
    if keys[pg.K_RIGHT]:
        box.move_ip(v, 0)
        
    # lag en ny frame
    wind.fill((255, 255, 255))
        
    # regne ut om noen av ballene har truffet spilleren
    for singleball in balls:
        if box.collidepoint(singleball.x, singleball.y + singleball.r):
            singleball.v[1] = -singleball.v[1]
            score += 1
        # hvis en ball har gått forbi spilleren, slutt spillet
        if singleball.y + singleball.r >= wind.get_height():
            cont = False
            break
        # flytt ballene
        singleball.move()
        # tegn ballene
        singleball.draw()
        
    # skriv ut poengsummen til høyre hjørnet
    img = font.render(str(score), True, 0)
    wind.blit(img, (470, 20))
        
    
    # tegn spilleren
    pg.draw.rect(wind, 0, box)
    # oppdater vinduen med den nye framen
    pg.display.flip()
    counter += 1
    clock.tick(60)

    # nytt ball blir laget etter hvis antall tid
    if counter % 360 == 0:
        newball = ball(rnd.randint(10, 490), rnd.randint(10, 250), 10, [rnd.choice([1, -1]) * 2.5, 3.2], wind)
        balls.append(newball)


pg.quit()