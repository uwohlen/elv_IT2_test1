import pygame as pg
import random as rnd

pg.init()

height = 420
width = 420

v0 = 2


wind = pg.display.set_mode([height, width])
clock = pg.time.Clock()

nektar = [pg.Rect(240, 240, 20, 20)]

class Player:
    def __init__(self, x, y, w, h, v, wind, RGB):
        self.v = v
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.wind = wind
        self.RGB = RGB
        
    def draw(self):
        pg.draw.rect(self.wind, self.RGB, (self.x, self.y, self.w, self.h))
        pg.display.update()
        
    def move(self):
        keys = pg.key.get_pressed()
        tmpx = self.x
        tmpy = self.y
        if self.key == 0:
            if self.x > 0:
                if keys[pg.K_LEFT]:
                    tmpx -= self.v
            if self.x < width - self.w:
                if keys[pg.K_RIGHT]:
                    tmpx += self.v   
            if self.y > 0:
                if keys[pg.K_UP]:
                    tmpy -= self.v
            if self.y < height - self.h:
                if keys[pg.K_DOWN]:
                    tmpy += self.v
        else:
            
            if self.x > 0:
                if keys[pg.K_a]:
                    tmpx -= self.v
            if self.x < width - self.w:
                if keys[pg.K_d]:
                    tmpx += self.v
            if self.y > 0:
                if keys[pg.K_w]:
                    tmpy -= self.v
            if self.y < height - self.h:    
                if keys[pg.K_s]:
                    tmpy += self.v
        player = pg.Rect(tmpx, tmpy, self.w, self.h)
        if player.collidelist(walls) == -1:
            self.x = tmpx
            self.y = tmpy
        self.nektar()
        
    def nektar(self):
        player = pg.Rect(self.x, self.y, self.w, self.h)
        try:
            if player.colliderect(nektar[0]):
                nektar.pop()
                self.v = v0
        except:
            return 0
    
cont = True
counter = 0
p1 = Player(0, 0, 20, 20, v0, wind, (255, 0, 0))
while cont:
    
    clock.tick(60)
    counter += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cont = False
            
    wind.fill((255, 255, 255))

    for nekt in nektar:
        pg.draw.rect(wind, (255, 255, 0), nekt)
    p1.move()
    p1.draw()

    
    if len(nektar) == 0 and counter % 600 == 0:
        tmp = pg.Rect(rnd.randint(0, width - 20), rnd.randint(0, height - 20), 20, 20)
        nektar.append(tmp)
            
    pl1 = pg.Rect(p1.x, p1.y, p1.w, p1.h)
    
    if pl1.colliderect(pl2):
        print("END GAME!!!")
        pg.quit()
    
pg.quit()