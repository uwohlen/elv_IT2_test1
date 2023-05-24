import pygame
import random

# Definerer konstanter
WIDTH = 800
HEIGHT = 600
FPS = 60
PLAYER_SPEED = 5
ENEMY_SPEED = 3
BULLET_SPEED = 8

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
        self.rect.center = (WIDTH // 2, HEIGHT - 50)
        self.speed = PLAYER_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Begrens spillerens bevegelse innenfor skjermen
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.randint(1, ENEMY_SPEED)

    def update(self):
        self.rect.y += self.speed

        # Sjekker om fienden har nådd bunnen av skjermen
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randint(1, ENEMY_SPEED)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed

        # Fjerner kulen når den forsvinner fra skjermen
        if self.rect.bottom < 0:
            self.kill()

# Oppretter spritegrupper
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# Oppretter spiller
player = Player()
all_sprites.add(player)

# Oppretter fiender på tilfeldige posisjoner
for _ in range(8):
    x = random.randrange(WIDTH)
    y = random.randrange(-100, -40)
    enemy = Enemy(x, y)
    all_sprites.add(enemy)
    enemies.add(enemy)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Oppdaterer spillverdenen
    all_sprites.update()

    # Sjekker om kuler treffer fiender
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        x = random.randrange(WIDTH)
        y = random.randrange(-100, -40)
        enemy = Enemy(x, y)
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Sjekker om fiender treffer spilleren
    if pygame.sprite.spritecollide(player, enemies, False):
        running = False

    # Tegner spillverdenen
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
