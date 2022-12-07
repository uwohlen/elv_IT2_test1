import pygame, sys, random

# Ball movement behaviour
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= screen_heigth:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
        
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

# Player-pad movement
def player_animation():
    player.y += player_speed
    
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_heigth:
        player.bottom = screen_heigth
        
# Opponent-pad movement
def opponent_ai():
    if opponent.top < ball.y:
            opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_heigth:
        opponent.bottom = screen_heigth
        
# Ball starting position
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_heigth / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

# General setup
pygame.init()
clock = pygame.time.Clock()

# Setting up the main window
screen_width = 1280 # 1366 (skole pc)
screen_heigth = 720 # 768 (skole pc)
screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption('Pong')

# Game rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_heigth / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_heigth / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_heigth / 2 - 70, 10, 140)

# Colors
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Speed
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

# Game loop
while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Movement input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    
    ball_animation()
    player_animation()
    opponent_ai()
            
    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_heigth))
            
    # Updating the window
    pygame.display.update()
    clock.tick(60)
