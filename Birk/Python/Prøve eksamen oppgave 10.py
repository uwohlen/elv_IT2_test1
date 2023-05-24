## Importerer relevante kodebiblioteker

import pygame, sys, random, math


## Generell oppsett

pygame.init() # starter pygame
clock = pygame.time.Clock() # bestemmer oppdateringsfrekvensen


## Hovedvindu oppsett

screen_width = 1280
screen_heigth = 720
screen = pygame.display.set_mode((screen_width, screen_heigth)) # størrelse på hovedvinduet
pygame.display.set_caption('Spill') # tittel på hovedvinduet


## Spill variabler

sides = ["top", "bottom", "left", "right"]
weights = [screen_width, screen_width, screen_heigth, screen_heigth]
poeng = 0
newPoeng = 0


## Player bevegelse

def player_animation():
    global player_speed_x, player_speed_y
    player.x += player_speed_x # bestemmer hvor fort player beveger seg i x-aksen
    player.y += player_speed_y # bestemmer hvor fort player beveger seg i y-aksen
    
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_heigth:
        player.bottom = screen_heigth
    if player.left <= 0:
        player.left = 0
    if player.right >= screen_width:
        player.right = screen_width
    
    ##if player.colliderect(player) or player.colliderect(player):
    
## Item kollisjon    

def item_collision():
    global item, poeng
    if item.colliderect(player):
        item_spawn()
        poeng += 1
    
    
## Item spawn posisjon
    
def item_spawn():
    item.x = random.randint(0, screen_width - 30) # item spawner på en tilfeldig x-posisjon
    item.y = random.randint(0, screen_heigth - 30) # item spawner på en tilfeldig y-posisjon


## Projectile bevegelse

def projectile_animation():
    global projectile_speed_x, projectile_speed_y, sides, weights, poeng, newPoeng
    projectile.x += projectile_speed_x # bestemmer hvor fort projectile beveger seg i x-aksen
    projectile.y += projectile_speed_y # bestemmer hvor fort projectile beveger seg i y-aksen
    
    side = random.choices(sides, weights)[0]
    
    if poeng > newPoeng:
        newPoeng += 1
        if side == "top":
            projectile.x = random.randint(0, screen_width - 30)
            projectile.y = 0
            projectile_speed_x = random.randint(-1, 1) * poeng
            projectile_speed_y = (poeng*1.1)
        elif side == "bottom":
            projectile.x = random.randint(0, screen_width - 30)
            projectile.y = screen_heigth - 6
            projectile_speed_x = random.randint(-1, 1) * poeng
            projectile_speed_y = -(poeng*1.1)
        elif side == "left":
            projectile.x = 0
            projectile.y = random.randint(0, screen_heigth - 30)
            projectile_speed_x = (poeng*1.1)
            projectile_speed_y = random.randint(-1, 1) * poeng
        elif side == "right":
            projectile.x = screen_width - 37
            projectile.y = random.randint(0, screen_heigth - 30)
            projectile_speed_x = -(poeng*1.1)
            projectile_speed_y = random.randint(-1, 1) * poeng
    
    if projectile.colliderect(player):
        pygame.quit()
        sys.exit()


## Spill objekter

player = pygame.Rect(screen_width / 2 - 15, screen_heigth / 2 - 15, 30, 30) # spillerfigur
item = pygame.Rect(random.randint(0, screen_width - 30), random.randint(0, screen_heigth - 30), 30, 30) # ressurs
projectile = pygame.Rect(0, 0, 6, 6) # prosjektil


## Farger

bg_color = pygame.Color('grey12') # bakgrunnsfarge
light_grey = (200, 200, 200) # farge på player
yellow = (255, 255, 0) # farge på item
red = (255, 0, 0) # farge på projectile


## Hastighet

player_speed_x = 0 # spillerens hastighet i x-aksen
player_speed_y = 0 # spillerens hastighet i y-aksen
projectile_speed_x = 0 # prosjektilets hastighet i x-aksen
projectile_speed_y = 0 # prosjektilets hastighet i y-aksen


## Spill løkke

while True:
    ## Håneterer input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # avslutter pygame
            sys.exit() # avslutter programmet

        # Bevegelse input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed_y += 4 # når pil-ned holdes inne, beveger player seg nedover
            if event.key == pygame.K_UP:
                player_speed_y -= 4
            if event.key == pygame.K_RIGHT:
                player_speed_x += 4 # når pil-høyre holdes inne, beveger player seg mot høyre
            if event.key == pygame.K_LEFT:
                player_speed_x -= 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed_y -= 4
            if event.key == pygame.K_UP:
                player_speed_y += 4
            if event.key == pygame.K_RIGHT:
                player_speed_x -= 4 
            if event.key == pygame.K_LEFT:
                player_speed_x += 4
        
    # Spill funksjoner
    player_animation()
    item_collision()
    
    # Visuelle elementer
    screen.fill(bg_color) # fyller vinduet med bakgrunnsfargen
    pygame.draw.rect(screen, light_grey, player) # tegner spiller-pad
    pygame.draw.ellipse(screen, yellow, item) # tegner item
    if poeng >= 1:
        projectile_animation()
        for i in range(poeng):
            pygame.draw.ellipse(screen, red, projectile)
    
    # Oppdaterer vinduet
    pygame.display.update()
    clock.tick(60) # oppdaterer vinduet 60 ganger i sekundet