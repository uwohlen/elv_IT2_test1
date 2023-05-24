import pygame
import random

# Definerer konstanter
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 40
MAZE_WIDTH = WIDTH // CELL_SIZE
MAZE_HEIGHT = HEIGHT // CELL_SIZE
PLAYER_COLOR = (255, 0, 0)
ITEM_COLOR = (0, 255, 0)
BOSS_COLOR = (0, 0, 255)
NEGATIVE_ITEM_COLOR = (255, 255, 0)
ENERGY_GAIN = 20
ENERGY_LOSS = 10
BOSS_ENERGY = 100
START_ENERGY = 50

# Definerer klasser
class Maze:
    def __init__(self):
        self.cells = [[0] * MAZE_WIDTH for _ in range(MAZE_HEIGHT)]  # Labyrintens grid

    def generate(self):
        # Genererer labyrinten
        pass

    def draw(self, screen):
        # Tegner labyrinten på skjermen
        for y in range(MAZE_HEIGHT):
            for x in range(MAZE_WIDTH):
                if self.cells[y][x] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = START_ENERGY

    def move(self, dx, dy):
        # Flytter spilleren i gitt retning
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT and maze.cells[new_y][new_x] == 0:
            self.x = new_x
            self.y = new_y

    def pick_item(self, item):
        # Plukker opp en item
        if item.type == "positive":
            self.energy += ENERGY_GAIN
        elif item.type == "negative":
            self.energy -= ENERGY_LOSS

    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Item:
    def __init__(self, x, y, item_type):
        self.x = x
        self.y = y
        self.type = item_type

    def draw(self, screen):
        color = ITEM_COLOR
        if self.type == "negative":
            color = NEGATIVE_ITEM_COLOR
        pygame.draw.rect(screen, color, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Boss:
    def __init__(self):
        self.x = MAZE_WIDTH // 2
        self.y = MAZE_HEIGHT // 2
        self.energy = BOSS_ENERGY

    def attack(self, player):
        # Simulerer bossens angrep på spilleren
        player.energy -= 10

    def draw(self, screen):
        pygame.draw.rect(screen, BOSS_COLOR, (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Initialiserer pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

maze = Maze()
maze.generate()

player = Player(0, 0)
boss = Boss()

items = []
for _ in range(4):
    x = random.randint(0, MAZE_WIDTH - 1)
    y = random.randint(0, MAZE_HEIGHT - 1)
    item_type = random.choice(["positive", "negative"])
    item = Item(x, y, item_type)
    items.append(item)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move(0, -1)
            elif event.key == pygame.K_DOWN:
                player.move(0, 1)
            elif event.key == pygame.K_LEFT:
                player.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.move(1, 0)

    # Sjekker om spilleren plukker opp en item
    for item in items:
        if player.x == item.x and player.y == item.y:
            player.pick_item(item)
            items.remove(item)

    # Sjekker om spilleren har kommet til midten av labyrinten
    if player.x == MAZE_WIDTH // 2 and player.y == MAZE_HEIGHT // 2:
        if player.energy > 0:
            boss.attack(player)
            if boss.energy <= 0:
                print("Du har bekjempet bossen! Du må nå gå ut av labyrinten.")
        else:
            print("Du har ikke nok energi til å bekjempe bossen. Du har tapt!")
        # Nullstiller spillet for neste runde

    # Tegner spillverdenen
    screen.fill((0, 0, 0))
    maze.draw(screen)
    for item in items:
        item.draw(screen)
    player.draw(screen)
    boss.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
