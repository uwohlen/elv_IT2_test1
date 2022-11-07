from vector2 import Vector2
from dataclasses import dataclass

@dataclass
class Particle:
    position: Vector2
    velocity: Vector2
    mass: float
    forces: list

    def step(self, dt):
        sum_forces = Vector2(0, 0)
        for force in self.forces:
            sum_forces += force
        
        acceleration = sum_forces/self.mass

        self.velocity += acceleration*dt
        self.position += self.velocity*dt

    def apply_force(self, force):
        self.forces.append(force)

