import pygame
import random

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 500
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])


class Button:
    def __init__(self, x, y, width, height, first_time, buttonText, onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.first_time = first_time

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

    def process(self):

        self.buttonSurface.fill(accent_color)
        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            self.buttonSurface.fill(text_color)

            if self.onePress:
                self.onclickFunction()

            elif not self.alreadyPressed:
                self.onclickFunction()
                self.alreadyPressed = True

        else:
            self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        window.blit(self.buttonSurface, self.buttonRect)


class Box:

    def __init__(self, id):
        self.id = id
        contains_cat = False


class StartButton(Button):

    def __init__(self, x, y, width, height, first_time, buttonText):
        super().__init__(x, y, width, height, first_time, buttonText)



box0 = Box(0)
box1 = Box(1)
box2 = Box(2)
box3 = Box(3)
box4 = Box(4)


boxes = [box0, box1, box2, box3, box4]

background_color = (38, 38, 53)
text_color = (243, 243, 249)
accent_color = (130, 135, 156)
first_time = True
font = pygame.font.Font('freesansbold.ttf', 40)
text = 'At your doorstep there are 5 boxes. \n' \
        'One of the boxes contains the cat. \n' \
        'Every morning you guess which box the cat is in. \n' \
        'If you guess correctly, you win. \n' \
        'If not, the cat moves one box up or down at night.'


start_button = StartButton(425, 270, 150, 100, first_time, 'Start')


def blit_text(surface, text, pos, font, color=text_color):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.




while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()



    '''
    boxes[random.randint(0, 4)].contains_cat = True
    guess = input('Guess which box the cat is in')
    if guess == '0' and boxes[0].contains_cat:
        print('You found the cat')
    elif guess == '1' and boxes[1].contains_cat:
        print('You found the cat')
    elif guess == '2' and boxes[2].contains_cat:
        print('You found the cat')
    elif guess == '3' and boxes[3].contains_cat:
        print('You found the cat')
    elif guess == '4' and boxes[4].contains_cat:
        print('You found the cat')
    else:
        print('You did not find the cat')'''

    window.fill((38, 38, 53))
    if start_button.first_time:
        blit_text(window, text, (20, 20), font,)
        start_button.process()

    pygame.display.flip()
