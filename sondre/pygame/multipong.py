import pygame
import random
import time
from pygame.locals import (K_LEFT, K_RIGHT)
from datetime import datetime

# initialize pygame
pygame.init()
pygame.font.init()

# set window size, create window object
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

score = 0
font = pygame.font.Font('freesansbold.ttf', 52)


class GameObject:
    """Base class for game objects"""

    def __init__(self, x_pos, y_pos, color, width, height, window_object):
        """Constructor"""
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.width = width
        self.height = height
        self.window_object = window_object

    def draw(self):
        """Function to draw game objects on screen"""
        pygame.draw.rect(self.window_object, self.color, pygame.Rect(self.x_pos, self.y_pos, self.width, self.height))


class Paddle(GameObject):
    """Class for paddle, inherits from base class GameObject"""

    def __init__(self, x_pos, y_pos, color, width, height, window_object):
        """Constructor"""
        super().__init__(x_pos, y_pos, color, width, height, window_object)

    def move(self, pressed_keys):
        """Function to move the paddle"""
        # Move paddle if left or right arrow is pressed
        if pressed_keys[K_LEFT]:
            self.x_pos -= 10
        if pressed_keys[K_RIGHT]:
            self.x_pos += 10

        # check if paddle is outside screen. If True, move paddle inside
        if self.x_pos <= 0:
            self.x_pos = 0
        if self.x_pos + 200 >= self.window_object.get_width():
            self.x_pos = self.window_object.get_width() - 200

    def check_collision_with_ball(self, ball, balls):
        """Function to check for collision between paddle and ball"""

        # check if ball and paddle collide
        if ball.y_pos < self.y_pos + self.height and \
                ball.height + ball.y_pos > self.y_pos:
            if ball.x_pos < self.x_pos + self.width and \
                    ball.x_pos + ball.width > self.x_pos:
                # Reverse momentum of ball
                ball.y_speed = -ball.y_speed
                ball.y_pos = 650
                # add to score when ball collides with paddle
                global score
                score += 1
                # add another ball if score is a multiple of 10
                if score % 2 == 0:
                    create_ball(balls)


class Ball(GameObject):
    """Class for ball"""

    def __init__(self, x_pos, y_pos, color, width, height, window_object, x_speed, y_speed):
        """Constructor"""
        super().__init__(x_pos, y_pos, color, width, height, window_object)
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move(self):
        """Function to move the ball"""

        # Check if ball collides with the edges of the screen
        if (self.x_pos <= 0) or ((self.x_pos + self.width) >= self.window_object.get_width()):
            self.x_speed = -self.x_speed

        if self.y_pos <= 0:
            self.y_speed = -self.y_speed

        # Move the ball
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

    def check_collision_with_other_ball(self, ball):
        """Function to check collision with other ball"""
        # Check if ball collides with other ball
        if self.x_pos < ball.x_pos + ball.width and \
                self.x_pos + self.width > ball.x_pos and \
                self.y_pos < ball.y_pos + ball.height and \
                self.height + self.y_pos > ball.y_pos:
            # Reverse momentum of ball if it collides
            self.x_speed = -self.x_speed
            self.y_speed = -self.y_speed


def create_ball(balls):
    """Function to create new balls"""
    # Create new ball object
    ball_obj = Ball(random.randint(0, 470), random.randint(1, 100), (255, 255, 255), 30, 30, window,
                    random.choice((-2, 2)), 3)
    # Append ball to list of balls
    balls.append(ball_obj)


def write_score():
    """Function to write score to list"""
    with open('multipong_highscores.txt', mode='a') as f:
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S",)
        highscore = f'{dt_string}: {score} points'
        f.write(f'\n{highscore}')


balls = []
# Create Paddle object
paddle = Paddle(150, 680, (255, 255, 255), 200, 20, window)
# Create new ball
create_ball(balls)

# Main game loop
running = True
while running:

    # Lock framerate to 60fps
    pygame.time.Clock().tick(40)

    # Check if player quits game. If True, end process
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # Get list of pressed keys
    pressed_keys = pygame.key.get_pressed()

    # Fill window with background color, create and display score text
    window.fill((0, 0, 0))
    score_text = font.render(str(score), True, (255, 255, 255))
    window.blit(score_text, (250, 10))

    # Draw Paddle object
    paddle.draw()

    # Draw, move and check collision on every Ball object
    for ball in balls:
        ball.draw()
        ball.move()
        paddle.check_collision_with_ball(ball, balls)
        for ball2 in balls:
            if not ball2 == ball:
                ball.check_collision_with_other_ball(ball2)

        # Check if ball touches the bottom of the screen
        if ball.y_pos >= 670:
            # Color ball red, end game
            ball.color = (255, 0, 0)
            window.fill((0, 0, 0))
            window.blit(score_text, (250, 10))
            # Draw paddle and ball
            paddle.draw()
            ball.draw()

            # Update display
            pygame.display.flip()
            write_score()
            pygame.time.wait(5000)
            running = False

    # Move paddle
    paddle.move(pressed_keys)

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
