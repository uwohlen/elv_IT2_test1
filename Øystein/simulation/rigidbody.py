from vector2 import Vector2
import math

class Rigidbody:
    def __init__(self, position, velocity, orientation, angular_velocity, shape):
        self.position = position
        self.velocity = velocity
        self.orientation = orientation
        self.angular_velocity = angular_velocity
        self.shape = shape
        self.forces = []

    def step(self, dt):
        sum_forces = Vector2(0, 0)
        sum_torque = 0
        for force in self.forces:
            sum_forces += force[0]
            sum_torque += force[1].x * force[0].y - force[1].y * force[0].x

        acceleration = sum_forces/self.shape.mass
        angular_acceleration = sum_torque/self.shape.moment_of_inertia

        self.velocity += acceleration*dt
        self.position += self.velocity*dt
        self.angular_velocity += angular_acceleration*dt
        self.orientation += self.angular_velocity*dt

    def apply_force(self, force, offset):
        self.forces.append((force, offset))

    def aabb(self):
        min_vec, max_vec = self.shape.aabb(self.orientation)
        return min_vec+self.position, max_vec+self.position

class Shape:
    def __init__(self, mass, moment_of_inertia):
        self.mass = mass
        self.moment_of_inertia = moment_of_inertia

class Box(Shape):
    def __init__(self, mass, size):
        moment_of_inertia = mass * size.dot(size) / 12
        super().__init__(mass, moment_of_inertia)

        self.size = size

    def aabb(self, orientation):
        points = [
            Vector2(-self.size.x/2, -self.size.y/2),
            Vector2(self.size.x/2, -self.size.y/2),
            Vector2(self.size.x/2, self.size.y/2),
            Vector2(-self.size.x/2, self.size.y/2)
        ]
        cos = math.cos(orientation)
        sin = math.sin(orientation)
        min_vec = Vector2(math.inf, math.inf)
        max_vec = Vector2(-math.inf, -math.inf)
        for point in points:
            newx = point.x*cos - point.y*sin
            newy = point.x*sin + point.y*cos
            if newx < min_vec.x:
                min_vec.x = newx
            if newx > max_vec.x:
                max_vec.x = newx
            if newy < min_vec.y:
                min_vec.y = newy
            if newy > max_vec.y:
                max_vec.y = newy
        return min_vec, max_vec

class Circle(Shape):
    def __init__(self, mass, radius):
        moment_of_inertia = 1/2 * mass * radius*radius
        super().__init__(mass, moment_of_inertia)

        self.radius = radius

    def aabb(self, orientation):
        min_vec = Vector2(-self.radius, -self.radius)
        max_vec = Vector2(self.radius, self.radius)
        return min_vec, max_vec