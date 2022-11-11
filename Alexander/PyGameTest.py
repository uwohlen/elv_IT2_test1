import pygame as pg


pg.init()

height = 500
width = 500

wind = pg.display.set_mode([height, width])
font = pg.font.SysFont("Arial", 12)
clock = pg.time.Clock()


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


balls = [ball(250, 200, 10, [2.5, 3.2], wind), ball(250, 250, 10, [1.5, 2.2], wind)]
box = pg.Rect(200, 450, 100, 15)
v = 5
cont = True
counter = 0
while cont:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cont = False
    
    keys = pg.key.get_pressed()
    
    if keys[pg.K_LEFT]:
        box.move_ip(-v, 0)
    if keys[pg.K_RIGHT]:
        box.move_ip(v, 0)
        
    for ball in balls:
        if box.collidepoint(ball.x, ball.y + ball.r):
            ball.v[1] = -ball.v[1]
        ball.move()
        ball.draw()
    
    
    wind.fill((255, 255, 255))
    pg.draw.rect(wind, 0, box)
    pg.display.flip() # update window
    counter += 1
    clock.tick(60)




pg.quit()