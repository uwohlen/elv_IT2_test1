from dataclasses import dataclass

@dataclass
class Vector2:
    x: float
    y: float

    def dot(self, other):
        return self.x*other.x+self.y*other.y

    def __add__(self, other):
        return Vector2(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector2(self.x-other.x, self.y-other.y)

    def __mul__(self, other):
        return Vector2(self.x*other, self.y*other)
    
    def __truediv__(self, other):
        return Vector2(self.x/other, self.y/other)