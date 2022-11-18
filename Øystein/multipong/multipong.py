import pygame, random, time

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.balls = [Ball(width/2, height/4, 1, 1, 20, 20, width, height)]
        self.paddle = Paddle(height - 50, 4, 50, 5, self.width, self.height)

        self.next_spawn = time.time() + random.randint(6, 10)

    def update(self):
        if time.time() > self.next_spawn:
            self.balls.append(Ball(
                self.width/2 + random.randint(-self.width/4, self.width/4), 
                self.height/4 + random.randint(-self.height/8, self.height/8), 
                random.random()*4-2, 
                random.random()+0.5,
                20,
                20,
                self.width, 
                self.height))
            self.next_spawn = time.time() + random.randint(6, 10)
        for ball in self.balls:
            ball.update(self.paddle)
            if ball.game_over():
                print(f"Game over! Score: {len(self.balls)}")
                return True
        self.paddle.update()
        return False

    def draw(self, screen):
        for ball in self.balls:
            ball.draw(screen)
        self.paddle.draw(screen)

    def event(self, event):
        self.paddle.event(event)

class Ball:
    def __init__(self, x, y, vel_x, vel_y, width, height, screen_width, screen_height):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, paddle):
        self.x += self.vel_x
        self.y += self.vel_y

        if self.x+self.width >= paddle.x and \
            self.x <= paddle.x+paddle.width and \
            self.y+self.height >= paddle.y and \
            self.y <= paddle.y+paddle.height:
            self.y = paddle.y - self.height
            self.vel_y = -self.vel_y

        if self.x <= 0:
            self.x = 0
            self.vel_x = -self.vel_x
        elif self.x >= self.screen_width - self.width:
            self.x = self.screen_width - self.width
            self.vel_x = -self.vel_x

        if self.y <= 0:
            self.y = 0
            self.vel_y = -self.vel_y

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), [self.x, self.y, self.width, self.height])

    def game_over(self):
        return self.y > self.screen_height

class Paddle:
    def __init__(self, y, speed, width, height, screen_width, screen_height):
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.speed = speed
        self.x = (self.screen_width - self.width) / 2
        self.y = y

        self.left_down = False
        self.right_down = False

    def update(self):
        if self.left_down:
            self.x -= self.speed
        if self.right_down:
            self.x += self.speed

        if self.x < 0:
            self.x = 0
        elif self.x > self.screen_width - self.width:
            self.x = self.screen_width - self.width

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))

    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left_down = True
            elif event.key == pygame.K_RIGHT:
                self.right_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left_down = False
            elif event.key == pygame.K_RIGHT:
                self.right_down = False  

def main():
    WIDTH = 400
    HEIGHT = 600

    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    clock = pygame.time.Clock()
    done = False

    game = Game(WIDTH, HEIGHT)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                done = True
                break
            else:
                game.event(event)
        if done:
            break
        screen.fill((0, 0, 0))

        if game.update():
            pygame.quit()
            done = True
            break
            
        game.draw(screen)

        pygame.display.update()
        clock.tick(60)
        
if __name__ == "__main__":
    main()