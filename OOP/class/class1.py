import math


class Shape:
    def __init__(self, shape):
        self.shape = shape


class Square(Shape):
    def __init__(self, shape, length):
        super().__init__(shape)
        self.length = length

    def area(self):
        return self.length**2


class Rectangle(Square):
    def __init__(self, shape, length, width):
        super().__init__(shape, length)
        self.width = width

    def areaR(self):
        return self.length*self.width


s = Square("Квадрат", 2)
print(s.shape)
print(s.area())

r = Rectangle("Прямоугольниk", 2, 3)
print(r.shape)
print(r.areaR())