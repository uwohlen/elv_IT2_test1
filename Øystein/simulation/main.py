import world, renderer, particle, math
from vector2 import Vector2
import rigidbody as rb

def main():
    w = world.World()
    #p = particle.Particle(Vector2(0, 0), Vector2(0, 0), 1, [])
    box = rb.Rigidbody(Vector2(0, 0), Vector2(0, 0), math.pi/4, 0, rb.Box(1, Vector2(1, 1)))
    #circle = rb.Rigidbody(Vector2(0, 0), Vector2(0, 0), 0, 0, rb.Circle(1, 1))
    #w.add(circle)
    w.add(box)

    fps = 60
    ren = renderer.Renderer(w, 600, 400, -6, 6, 4, -4, fps)
    while True:
        box.apply_force(Vector2(0, 0.01), Vector2(0.1, 0))
        #box.apply_force(Vector2(0, -0.01), Vector2(0, 0))
        w.step(1/fps)
        ren.draw()

if __name__ == "__main__":
    main()