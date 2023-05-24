import pygame
import random

# Definer spillebrettets størrelse
BOARD_WIDTH = 800
BOARD_HEIGHT = 600

# Definer farger
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (BOARD_WIDTH // 2, BOARD_HEIGHT // 2)

    def update(self, pressed_keys):
        # Beveg spilleren basert på tastetrykk
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Begrens spilleren til å være innenfor spillebrettet
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > BOARD_WIDTH:
            self.rect.right = BOARD_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > BOARD_HEIGHT:
            self.rect.bottom = BOARD_HEIGHT

class Resource(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, BOARD_WIDTH), random.randint(0, BOARD_HEIGHT))

class Projectile(pygame.sprite.Sprite):
    def __init__(self, speed_x, speed_y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.choice([0, BOARD_WIDTH])
        self.rect.y = random.randint(0, BOARD_HEIGHT)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        # Beveg prosjektilet
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Sjekk om prosjektilet har forlatt spillebrettet
        if self.rect.left > BOARD_WIDTH or self.rect.right < 0 or self.rect.top > BOARD_HEIGHT or self.rect.bottom < 0:
            self.kill()

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
        self.all_sprites = pygame.sprite.Group()
        self.resources = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.score = 0
        self.projectile_speed = 1

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pressed_keys = pygame.key.get_pressed()
            self.player.update(pressed_keys)

            if len(self.resources) == 0:
                self.score += 1
                self.projectile_speed += 1
                self.create_resource()
                self.create_projectiles()

            self.update_projectiles()

            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)

            # Sjekk kollisjon mellom spiller og ressurser
            collisions = pygame.sprite.spritecollide(self.player, self.resources, True)
            if collisions:
                self.score += 1

            # Sjekk kollisjon mellom spiller og prosjektiler
            collisions = pygame.sprite.spritecollide(self.player, self.projectiles, False)
            if collisions:
                running = False

            pygame.display.flip()

        print("Spillet er over. Du klarte å plukke opp", self.score, "ressurser.")

    def create_resource(self):
        resource = Resource()
        self.resources.add(resource)
        self.all_sprites.add(resource)

    def create_projectiles(self):
        for _ in range(self.score):
            speed_x = random.choice([-self.projectile_speed, self.projectile_speed])
            speed_y = random.choice([-self.projectile_speed, self.projectile_speed])
            projectile = Projectile(speed_x, speed_y)
            self.projectiles.add(projectile)
            self.all_sprites.add(projectile)

    def update_projectiles(self):
        for projectile in self.projectiles:
            projectile.update()

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
