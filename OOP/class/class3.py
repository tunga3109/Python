import math

class Figure:

    def __init__(self,figure):
        self.figure = figure

class Triangle(Figure):

    def __init__(self, figure, side_1, side_2, side_3):
        super().__init__(figure)
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
    
    def perimentr(self):
        return self.side_1 + self.side_2 + self.side_3

class Square(Figure):
    def __init__(self,figure,length):
        self.figure = figure
        self.length = length

    def areaS(self):
        return self.length**2

class Rectagle(Square):
    def __init__(self,figure,length,width):
        super().__init__(figure,length)
        self.width = width

    def areaR(self):
        return self.length*self.width



t = Triangle('Treug',1,2,3)
print(t.perimentr())
print(t.figure)


r = Rectagle('Pryam',2,3)
print(r.areaR())
print(r.figure)

k = Square('Kvad',3)
print(k.areaS())
print(k.figure)



