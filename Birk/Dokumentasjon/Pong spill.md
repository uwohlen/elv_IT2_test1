# Pong spill
#### Forfatter: `Birk Oskar Aarvold Ihle`
#### Opprettet: `16.11.2022`
#### Oppdatert: `07.12.2022`
#### Etiketter: `Python` `Pygame` `Pong`

## Innhold

* [Importerer relevante kodebiblioteker](#importerer-relevante-kodebiblioteker)
* [Ball bevegelse oppførsel](#ball-bevegelse-oppførsel)
* [Spiller-pad bevegelse](#spiller-pad-bevegelse)
* [Motstander-pad bevelse](#motstander-pad-bevelse)
* [Ball start posisjon](#ball-start-posisjon)
* [Generell oppsett](#generell-oppsett)
* [Hovedvindu oppsett](#hovedvindu-oppsett)
* [Spill rektangler](#spill-rektangler)
* [Farger](#farger)
* [Hastighet](#hastighet)
* [Spill løkke](#spill-løkke)

## Importerer relevante kodebiblioteker

```python
import pygame, sys, random
```

## Ball bevegelse oppførsel

```python
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x # bestemmer hvor fort ballen beveger seg i x-aksen
    ball.y += ball_speed_y # bestemmer hvor fort ballen beveger seg i y-aksen
    
    if ball.top <= 0 or ball.bottom >= screen_heigth:
        ball_speed_y *= -1 # ballen beveger seg i motsatt retning i y-aksen når den treffer toppen eller bunnen
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart() # ballen går til start posisjonen når den treffer venstre eller høyre side
        
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1 # ballen beveger seg i motsatt retning i x-aksen når den treffer spiller-pad eller motstander-pad
```

## Spiller-pad bevegelse

```python	
def player_animation():
    player.y += player_speed # bestemmer hvor fort spiller-pad beveger seg i y-aksen
    
    if player.top <= 0:
        player.top = 0 # spiller-pad stopper når den treffer toppen
    if player.bottom >= screen_heigth:
        player.bottom = screen_heigth # spiller-pad stopper når den treffer bunnen
```
        
## Motstander-pad bevelse

```python	
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed # dersom toppen av motstander-pad er under ballen, beveger den seg oppover
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed # dersom bunnen av motstander-pad er over ballen, beveger den seg nedover
    
    if opponent.top <= 0:
        opponent.top = 0 # motstander-pad stopper når den treffer toppen
    if opponent.bottom >= screen_heigth:
        opponent.bottom = screen_heigth # motstander-pad stopper når den treffer bunnen
```
        
## Ball start posisjon

```python
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_heigth / 2) # ballen går til midten av banen
    ball_speed_y *= random.choice((1, -1)) # ballen beveger seg i en tilfeldig retning i y-aksen
    ball_speed_x *= random.choice((1, -1)) # ballen beveger seg i en tilfeldig retning i x-aksen
```

## Generell oppsett
    
```python
pygame.init() # starter pygame
clock = pygame.time.Clock() # bestemmer oppdateringsfrekvensen
```

## Hovedvindu oppsett

```python
screen_width = 1280
screen_heigth = 720
screen = pygame.display.set_mode((screen_width, screen_heigth)) # størrelse på hovedvinduet
pygame.display.set_caption('Pong') # tittel på hovedvinduet
```

## Spill rektangler

```python
ball = pygame.Rect(screen_width / 2 - 15, screen_heigth / 2 - 15, 30, 30) # størrelse på ballen
player = pygame.Rect(screen_width - 20, screen_heigth / 2 - 70, 10, 140) # størrelse på spiller-pad
opponent = pygame.Rect(10, screen_heigth / 2 - 70, 10, 140) # størrelse på motstander-pad
```

## Farger

```python
bg_color = pygame.Color('grey12') # bakgrunnsfarge
light_grey = (200, 200, 200) # farge på midtlinjen
```

## Hastighet

```python
ball_speed_x = 7 * random.choice((1, -1)) # bestemmer hvilken retning ballen beveger seg i x-aksen
ball_speed_y = 7 * random.choice((1, -1)) # bestemme hvilken retning ballen beveger seg i y-aksen
player_speed = 0 # hastighet på spiller-pad i y-aksen når den ikke beveger seg
opponent_speed = 7 # bestemmer hvor fort motstander-pad beveger seg i y-aksen
```

## Spill løkke

```python
while True:
    # Håndterer input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # avslutter pygame
            sys.exit() # avslutter programmet
        # Bevegelse input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7 # når pil-ned holdes inne, beveger spiller-pad seg nedover
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7 # når pil-opp holdes inne, beveger spiller-pad seg oppover
            if event.key == pygame.K_UP:
                player_speed += 7
    
    # Spill funksjoner
    ball_animation()
    player_animation()
    opponent_ai()
            
    # Visuelle elementer
    screen.fill(bg_color) # fyller vinduet med bakgrunnsfargen
    pygame.draw.rect(screen, light_grey, player) # tegner spiller-pad
    pygame.draw.rect(screen, light_grey, opponent) # tegner motstander-pad
    pygame.draw.ellipse(screen, light_grey, ball) # tegner ballen
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_heigth)) # tegner midtlinjen
            
    # Oppdaterer vinduet
    pygame.display.update()
    clock.tick(60)
```