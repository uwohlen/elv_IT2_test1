
class Rectangle:

    def __init__(self, width, length, color):

        self.width = width
        self.length = length
        self.color = color

    def area(self):
        area = self.width * self.length
        return area
        

rectangle = Rectangle(3,2, "blue")


print(rectangle.color)

print(rectangle.area())