import pygame as pg
import math

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])


class Ball:
    """Klasse for å representere en ball"""

    def __init__(self, x, y, x_speed, y_speed, radius, window_object, color):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.radius = radius
        self.window_object = window_object
        self.color = color

    def draw(self):
        """Metode for å tegne ballen"""
        pg.draw.circle(self.window_object, self.color, (self.x, self.y), self.radius)

    def move(self):
        """Metode for å flytte ballen"""
        # Sjekker om ballen er utenfor høyre/venstre kant
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.window_object.get_width()):
            self.x_speed = -self.x_speed

        if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.window_object.get_width()):
            self.y_speed = -self.y_speed

        # Flytter ballen
        self.x += self.x_speed
        self.y += self.y_speed


# Lager et Ball-objekt
ball1 = Ball(250, 250, 0.1, 0.1, 40, window, (0, 255, 0))
ball2 = Ball(300, 100, -0.1, 0.1, 50, window, (255, 0, 0))


def calculate_distance(obj1, obj2):
    x_distance_2 = (obj1.x - obj2.x)**2
    y_distance_2 = (obj1.y - obj2.y)**2
    distance = math.sqrt(x_distance_2 + y_distance_2)
    return distance


# Gjenta helt til brukeren lukker vinduet
running = True
while running:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Farger bakgrunnen lyseblå
    window.fill((135, 206, 235))

    # Tegner og flytter ballen
    ball1.draw()
    ball1.move()

    ball2.draw()
    ball2.move()

    if calculate_distance(ball1, ball2) <= 0:
        print('collision')
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
