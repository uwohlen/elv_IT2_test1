import pygame as pg
import math

pg.init()

height = 500
width = 500

wind = pg.display.set_mode([height, width])
font = pg.font.SysFont("Arial", 12)

class ball():
    def __init__(self, x, y, r, v, window):
        self.x = x
        self.y = y
        self.r = r
        self.v = v
        self.window = window
        
    def draw(self):
        pg.draw.circle(self.window, (255, 0, 0), (self.x, self.y), self.r)
    
    def move(self):
        if (self.x - self.r) <= 0 or (self.x + self.r) >= self.window.get_width():
            self.v[0] = -self.v[0]
        if (self.y - self.r) <= 0 or (self.y + self.r) >= self.window.get_height():
            self.v[1] = -self.v[1]
        
        self.x += self.v[0]
        self.y += self.v[1]

def collision(ball1, ball2):
    dist = math.sqrt((ball1.x - ball2.x) ** 2 + (ball1.y - ball2.y) ** 2)
    if (dist - (ball1.r + ball2.r)) <= 0

ball = ball(250, 250, 20, [0.1, 0.12], wind)

cont = True
while cont:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cont = False
    
    wind.fill((255, 255, 255))
    ball.draw()
    pg.display.flip() # update window
    ball.move()




pg.quit()