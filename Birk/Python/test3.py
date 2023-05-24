import pygame
import random

# Definerer konstanter
WIDTH = 800
HEIGHT = 600
FPS = 60
PLAYER_SPEED = 5
ENEMY_SPEED = 3

# Initialiserer pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Definerer klasser
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED

        # Begrens spillerens bevegelse innenfor skjermen
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.dx = random.choice([-1, 1]) * ENEMY_SPEED
        self.dy = random.choice([-1, 1]) * ENEMY_SPEED

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Sjekker om fienden har nådd kanten av skjermen og snur bevegelsesretning
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx *= -1
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.dy *= -1

# Oppretter spritegrupper
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Oppretter spiller og fiender
player = Player()
all_sprites.add(player)

for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Oppdaterer spillverdenen
    all_sprites.update()

    # Sjekker om spilleren kolliderer med fiender
    if pygame.sprite.spritecollide(player, enemies, True):
        print("Du ble truffet av en fiende!")

    # Tegner spillverdenen
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
