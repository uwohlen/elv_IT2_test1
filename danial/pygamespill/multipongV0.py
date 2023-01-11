import pygame, sys

def ball_animation():
	global ball_speed_x, ball_speed_y
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= VINDU_HOYDE:
		ball_speed_y *= -1
	if ball.left <= 0 or ball.right >= VINDU_BREDDE:
		ball_speed_x *= -1

	if ball.colliderect(player_1) or ball.colliderect(player_2):
		ball_speed_x *= -1

# Spiller 1 animasjon
def player_1_animation():
	player_1.y += player_speed

	if player_1.top <= 0:
		player_1.top = 0
	if player_1.bottom >= VINDU_HOYDE:
		player_1.bottom = VINDU_HOYDE

# Spiller 2 animasjon

def player_2_animation():
	player_2.y += player_speed

	if player_2.top <= 0:
		player_2.top = 0
	if player_2.bottom >= VINDU_HOYDE:
		player_2.bottom = VINDU_HOYDE

#  Starter pygame og lager FPS
pygame.init()
clock = pygame.time.Clock()

# Opretter et vindu med innholdet vårt
VINDU_BREDDE = 1280
VINDU_HOYDE = 720
screen = pygame.display.set_mode((VINDU_BREDDE,VINDU_HOYDE))
pygame.display.set_caption('Pong')

# Farger
blue = (0,255,0)
red = (255,0,0)
grey = (200,200,200)
bg_color = pygame.Color('grey20')

# Spill Rektangler
ball = pygame.Rect(VINDU_BREDDE / 2 - 15, VINDU_HOYDE / 2 - 15, 30, 30)
player_1 = pygame.Rect(VINDU_BREDDE - 20, VINDU_HOYDE / 2 - 70, 10,140) 
player_2 = pygame.Rect(10, VINDU_HOYDE / 2 - 70, 10,140)

# Spill variabler
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player_speed -= 15
			if event.key == pygame.K_DOWN:
				player_speed += 15
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player_speed += 15
			if event.key == pygame.K_DOWN:
				player_speed -= 15
	
	# Spill funksjoner
	ball_animation()
	player_1_animation()
	player_2_animation()

	# Visuelle elementer
	screen.fill(bg_color)
	pygame.draw.rect(screen,  blue, player_1)
	pygame.draw.rect(screen, red, player_2)
	pygame.draw.ellipse(screen, grey, ball)
	pygame.draw.line(screen, grey, (VINDU_BREDDE / 2, 0),(VINDU_BREDDE / 2, VINDU_HOYDE))

	pygame.display.flip()
	clock.tick(60)