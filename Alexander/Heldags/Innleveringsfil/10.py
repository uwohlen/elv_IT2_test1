import pygame as pg


tile = 30

class Player:
    def __init__(self, x, y, w, h, RGB, v = 4):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.RGB = RGB
        self.v = v
        
    def draw(self):
        r = 7
        pg.draw.rect(wind, self.RGB, (self.x, self.y, self.w, self.h))
        pg.draw.circle(wind, self.RGB, (self.x + 0.5 * self.w, self.y - r * 0.7), r)
        pg.display.update()
        
    def floor(self, rects, lift):
        for rect in rects:
            if self.y + tile >= rect.y and self.y + tile <= rect.y + tile and self.x + tile >= rect.x and self.x + tile <= rect.x + tile and lift == 0:
                return 1
        return 0
    
    def fall(self, lift):
        if self.floor(walls, lift) == 0:
            self.y += 0.1
        
    def move(self, lift):
        keys = pg.key.get_pressed()
        tmpx = self.x
        tmpy = self.y
        if self.x > 0:
            if keys[pg.K_LEFT]:
                tmpx -= self.v
        if self.x < width - self.w:
            if keys[pg.K_RIGHT]:
                tmpx += self.v   
        player = pg.Rect(tmpx, tmpy, self.w, self.h)
        if player.collidelist(walls) == -1 and lift == 0:
            self.x = tmpx
            self.y = tmpy
            
            
class Boss(Player):
    def __init__(self, x, y, w, h, RGB, v = 4):
        super().__init__(x, y, w, h, RGB, v = 4)
        
    def push(self, player):
        if player.y >= self.y and player.y <= self.y + tile:
            if player.x + tile >= self.x and player.x + tile <= self.x + tile:
                self.x = player.x + tile
            if player.x - tile <= self.x and player.x + tile >= self.x + tile:
                self.x = player.x - tile
       
class Resource:
    def __init__(self, x, y, w, h, RGB, v = 2):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.RGB = RGB
        self.v = v
        
    def draw(self):
        pg.draw.rect(wind, self.RGB, (self.x, self.y, self.w, self.h))
        pg.display.update()
        
class Lift:
    def __init__(self, x, y, w, h, RGB, v = 2):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.RGB = RGB
        self.v = v
        
    def draw(self):
        pg.draw.rect(wind, self.RGB, (self.x, self.y, self.w, self.h), width = 1)
        pg.display.update()
    
    def lift(self, player, stop):
        if player.x >= self.x and player.x <= self.x + tile + 5 and player.y >= self.y and player.y <= self.y + tile + 5:
            if self.y == stop + 5:
                return 1
            else:
                self.y -= self.v
                player.y = self.y
            return 1
        return 0

        
board = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 's', 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'x', 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 'r', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    1, 0, 'p', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'l', 0, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
    
    ]

walls = []
resources = []
for i in range(0, len(board)):
    if board[i] == 1:
        walls.append(pg.Rect((i % 21) * tile, (i // 21) * tile, tile, tile))
    if board[i] == 'x':
        boss = Boss((i % 21) * tile, (i // 21) * tile, tile, tile, "blue")
    if board[i] == 'p':
        player = Player((i % 21) * tile, (i // 21) * tile, tile, tile, "red")
    if board[i] == 'l':
        lift = Lift((i % 21) * tile + 5, (i // 21) * tile - 5, tile + 5, tile + 5, "red")
    if board[i] == 's':
        stop = (i // 21) * tile
    if board[i] == 'r':
        resources.append(Resource((i % 21) * tile + 5, (i // 21) * tile - 5, tile + 5, tile + 5, "yellow"))
        
        
height = 630
width = 630

pg.init()

wind = pg.display.set_mode([height, width])
clock = pg.time.Clock()

cont = True


while cont:
    
    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cont = False
    wind.fill((255, 255, 255))
            
    for rect in walls:
        pg.draw.rect(wind, (0, 0, 0), rect)
            
    for resource in resources:
        resource.draw()
    lif = lift.lift(player, stop)
    player.move(lif)
    boss.push(player)
    for x in range(20):
        player.fall(lif)
        boss.fall(0)
    boss.draw()
    player.draw()
    lift.draw()
    pg.display.update()
    
    if boss.y >= 540:
        print("You Winn!!!")
        cont = False
            
            
pg.quit()
            