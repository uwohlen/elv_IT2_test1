import pygame as pg
import random as rnd

class Player:
    def __init__(self, x, y, w, h, v, wind, RGB):
        self.v = v
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.wind = wind
        self.RGB = RGB
        self.health = 5
        self.collect = 1
        
    def draw(self):
        pg.draw.rect(self.wind, self.RGB, (self.x, self.y, self.w, self.h))
        pg.display.update()
        
    def move(self):
        keys = pg.key.get_pressed()
        tmpx = self.x
        tmpy = self.y
            
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
                
        player = pg.Rect(tmpx, self.y, self.w, self.h)
        if player.collidelist(walls) == -1:
            self.x = tmpx
        
        player = pg.Rect(self.x, tmpy, self.w, self.h)
        if player.collidelist(walls) == -1:    
            self.y = tmpy

        
    def resource(self, resources):
        player = pg.Rect(self.x, self.y, self.w, self.h)
        keys = pg.key.get_pressed()
        try:
            if player.collidelist(resources) != -1 and keys[pg.K_e] and self.collect == 1:
                resources.clear()
                if rnd.randint(0, 2) == 0:
                    self.health -= 1
                else:
                    self.health += 1
            
            elif player.collidelist(resources) != -1 and self.collect == 0:
                resources.clear()
                if rnd.randint(0, 2) == 0:
                    self.health -= 1
                else:
                    self.health += 1
        except:
            return 0
        
class Monster:
    def __init__(self, x, y, wind):
        self.health = 5
        self.rect = pg.Rect(x, y, 20, 20)
        self.wind = wind
        self.alive = 1
        
    def draw(self):
        pg.draw.rect(self.wind, (0, 255, 0), self.rect)
        pg.display.update()
        
    def attack(self, player):
        keys = pg.key.get_pressed()
        p = pg.Rect(player.x, player.y, player.w, player.h)
        if p.colliderect(self.rect) != -1 and keys[pg.K_q]:
            if player.health >= self.health:
                player.health -= self.health
                self.alive = 0
                return 1
            else:
                return 0



pg.init()
font = pg.font.SysFont("Arial", 20)

height = 420
width = 420

v0 = 2

board = [
    1, 'p', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1,
    1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1,
    1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1,
    1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1,
    1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1,
    1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1,
    1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 'm', 1, 0, 1, 0, 1, 0, 1, 1,
    1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1,
    1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1,
    1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1,
    1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1,
    1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1,
    1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1,
    1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
    ]


def create_resources():
    resource = []
    for x in range(0, 4):
        resource.append(pg.Rect(rnd.randint(1, 20) * 20, rnd.randint(1, 20) * 20, 20, 20))
    nocoll = 0
    while nocoll == 0:
        nocoll = 1
        for i in range(len(resource)):
            if resource[i].collidelist(walls) != -1 and resource[i].collidelist(resource) != -1 and resource[i].colliderect(monster.rect) != -1:
                nocoll = 0
                resource[i] = pg.Rect(rnd.randint(0, 21) * 20, rnd.randint(0, 21) * 20, 20, 20)
    return resource    

wind = pg.display.set_mode([height, width])
clock = pg.time.Clock()


walls = []
for i in range(0, len(board)):
    if board[i] == 1:
        walls.append(pg.Rect((i % 21) * 20, (i // 21) * 20, 20, 20))
    if board[i] == 'm':
        monster = Monster((i % 21) * 20, (i // 21) * 20, wind)
    if board[i] == 'p':
            p1x = (i % 21) * 20
            p1y = (i // 21) * 20
        
def new_player():
    for i in range(0, len(board)):
        if board[i] == 'p':
            p1 = Player((i % 21) * 20, (i // 21) * 20, 20, 20, v0, wind, (255, 0, 0))
    return p1
p1 = new_player()


resources = create_resources()
cont = True
while cont:
    
    if len(resources) == 0:
        resources = create_resources()
    
    clock.tick(60)
    
            
    wind.fill((255, 255, 255))
    
    for rect in walls:
        pg.draw.rect(wind, (0, 0, 0), rect)
    for res in resources:
        pg.draw.rect(wind, (255, 255, 0), res)

        
    p1.move()
    p1.resource(resources)
    if monster.alive == 1:
        monster.draw()
        tmp = monster.attack(p1)
    if tmp == 0:
        p1 = new_player()
    if monster.alive == 0:
        p1.collect = 0
    
    img = font.render(f"Strength: {p1.health}", True, (255, 0, 0))
    wind.blit(img, (320, 0))

    
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cont = False
    
    if p1.x == p1x and p1.y == p1y and monster.alive == 0:
        print("You Win!!!")
        cont = False
    
    if p1.health <= 0 and monster.alive == 0:
        print("Oh no, both you and the monster died!!!")
        cont = False
    elif p1.health <= 0:
        print("Oh no, you died!!!")
        cont = False    
    
    p1.draw()
    
   
            
    

pg.quit()