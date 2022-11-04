import pygame
import game
import time

def main():
    game_width = 10
    game_height = 20
    g = game.Game(game_width, game_height)

    last_tick = time.time()
    tick_length = 1
    
    square_size = 25

    pygame.init()
    screen = pygame.display.set_mode([250, 500])

    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    g.rotate_piece(1)
                elif event.key == pygame.K_DOWN:
                    g.drop()
                    last_tick = time.time()
                elif event.key == pygame.K_LEFT:
                    g.move_piece(-1)
                elif event.key == pygame.K_RIGHT:
                    g.move_piece(1)

        if time.time() - last_tick > tick_length:
            g.tick()
            last_tick = time.time()
        
        screen.fill((0, 0, 0, 255))
        
        squares = g.squares_filled()
        for x in range(game_width):
            for y in range(game_height):
                if squares[y*game_width+x]:
                    pygame.draw.rect(screen, (255, 255, 0, 255), (x*square_size, y*square_size, square_size, square_size))

        pygame.display.flip()
        clock.tick(60)
        
if __name__ == "__main__":
    main()