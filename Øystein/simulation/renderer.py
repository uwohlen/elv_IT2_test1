import pygame, particle, rigidbody, math
from vector2 import Vector2

class Renderer:
    def __init__(self, world, screen_width, screen_height, min_x, max_x, min_y, max_y, fps):
        self.world = world
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.fps = fps
        
        pygame.init()

        self.screen = pygame.display.set_mode([screen_width, screen_height])
        self.clock = pygame.time.Clock()

    def world_to_screen(self, vec2):
        screen_x = (vec2.x - self.min_x) * (self.screen_width / (self.max_x - self.min_x))
        screen_y = (vec2.y - self.min_y) * (self.screen_height / (self.max_y - self.min_y))
        return Vector2(screen_x, screen_y)

    def draw(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        self.screen.fill((0, 0, 0))
        for object in self.world.objects:
            min_vec, max_vec = object.aabb()
            min_vec, max_vec = self.world_to_screen(min_vec), self.world_to_screen(max_vec)
            x, y = min(min_vec.x, max_vec.x), min(min_vec.y, max_vec.y)
            w, h = abs(min_vec.x-max_vec.x), abs(min_vec.y-max_vec.y)
            pygame.draw.rect(self.screen, (127, 127, 127), (x, y, w, h))

            shape = object.shape
            if type(shape) == particle.Particle:
                pos = self.world_to_screen(object.position)
                pygame.draw.circle(self.screen, (255, 255, 255), (pos.x, pos.y), 5)

            elif type(shape) == rigidbody.Box:
                points = [
                    Vector2(-shape.size.x/2, -shape.size.y/2),
                    Vector2(shape.size.x/2, -shape.size.y/2),
                    Vector2(shape.size.x/2, shape.size.y/2),
                    Vector2(-shape.size.x/2, shape.size.y/2)
                ]
                cos = math.cos(object.orientation)
                sin = math.sin(object.orientation)
                screen_points = []
                for i, point in enumerate(points):
                    newx = point.x*cos - point.y*sin + object.position.x
                    newy = point.x*sin + point.y*cos + object.position.y
                    screen_point = self.world_to_screen(Vector2(newx, newy))
                    screen_points.append((screen_point.x, screen_point.y))
                pygame.draw.polygon(self.screen, (255, 255, 255), screen_points)

            elif type(shape) == rigidbody.Circle:
                pos = self.world_to_screen(object.position)
                radius = shape.radius * (self.screen_width / (self.max_x - self.min_x))
                pygame.draw.circle(self.screen, (255, 255, 255), (pos.x, pos.y), radius)

        pygame.display.update()
        self.clock.tick(self.fps)