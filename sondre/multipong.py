import pygame
import random
import time
from pygame.locals import (K_LEFT, K_RIGHT)

pygame.init()
pygame.font.init()

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

score = 0
font = pygame.font.Font('freesansbold.ttf', 52)


class GameObject:
    """Base class for game objects"""

    def __init__(self, x_pos, y_pos, color, width, height, window_object):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.width = width
        self.height = height
        self.window_object = window_object

    def draw(self):
        pygame.draw.rect(self.window_object, self.color, pygame.Rect(self.x_pos, self.y_pos, self.width, self.height))


class Paddle(GameObject):
    """Class for paddle"""

    def __init__(self, x_pos, y_pos, color, width, height, window_object):
        super().__init__(x_pos, y_pos, color, width, height, window_object)

    def move(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.x_pos -= 10
        if pressed_keys[K_RIGHT]:
            self.x_pos += 10

        if self.x_pos <= 0:
            self.x_pos = 0
        if self.x_pos + 200 >= self.window_object.get_width():
            self.x_pos = self.window_object.get_width() - 200

    def check_collision_with_ball(self, ball, balls):
        if ball.y_pos < self.y_pos + self.height and \
                ball.height + ball.y_pos > self.y_pos:
            if ball.x_pos < self.x_pos + self.width and \
                    ball.x_pos + ball.width > self.x_pos:
                ball.y_speed = -ball.y_speed
                ball.y_pos = 650
                global score
                score += 1
                if str(score).endswith('0'):
                    create_ball(balls)


class Ball(GameObject):
    """Class for ball"""

    def __init__(self, x_pos, y_pos, color, width, height, window_object, x_speed, y_speed):
        """Constructor"""
        super().__init__(x_pos, y_pos, color, width, height, window_object)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):

        if (self.x_pos <= 0) or ((self.x_pos + self.width) >= self.window_object.get_width()):
            self.x_speed = -self.x_speed

        if self.y_pos <= 0:
            self.y_speed = -self.y_speed

        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

    def check_collision_with_other_ball(self, ball):
        if self.x_pos < ball.x_pos + ball.width and \
                self.x_pos + self.width > ball.x_pos and \
                self.y_pos < ball.y_pos + ball.height and \
                self.height + self.y_pos > ball.y_pos:
            self.x_speed = -self.x_speed
            self.y_speed = -self.y_speed


def create_ball(balls):
    ball = Ball(random.randint(0, 470), random.randint(1, 100), (255, 255, 255), 30, 30, window,
                random.choice((-2, 2)), 3)
    balls.append(ball)


balls = []
paddle = Paddle(150, 680, (255, 255, 255), 200, 20, window)
create_ball(balls)

running = True
while running:

    pygame.time.Clock().tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    pressed_keys = pygame.key.get_pressed()

    window.fill((0, 0, 0))
    score_text = font.render(str(score), True, (255, 255, 255))
    window.blit(score_text, (250, 10))

    paddle.draw()
    for ball in balls:
        ball.draw()
        ball.move()
        paddle.check_collision_with_ball(ball, balls)
        for ball2 in balls:
            if not ball2 == ball:
                ball.check_collision_with_other_ball(ball2)

        if ball.y_pos >= 670:
            ball.color = (255, 0, 0)
            window.fill((0, 0, 0))
            window.blit(score_text, (250, 10))
            paddle.draw()
            ball.draw()

            pygame.display.flip()
            pygame.time.wait(5000)
            running = False

    paddle.move(pressed_keys)

    pygame.display.flip()

pygame.quit()
