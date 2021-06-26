# Первая задача

import math


class Figure:

    def __init__(self,figure):
        self.figure = figure

class Square(Figure):

    def __init__(self,figure,length):
        self.figure = figure
        self.length = length
    
    def areaS(self):
        return self.length*2

    def diag(self):
        return  math.sqrt((self.length**2) + (self.length**2))

    def perimert(self):
        return self.length*4

class Prizma(Square):

    def __init__(self,figure,length,height):
        self.figure = figure
        self.length = length
        self.height = height
    
    def areaP(self):
        return self.length*2 * (self.length + (self.height*2))



s = Square('kvadrat',4)
print(s.figure)
print(s.areaS())
print(s.diag())
print(s.perimert())

p = Prizma('prizma',4,5)
print(p.figure)
print(p.areaP())
print(p.height)


# Вторая задача


class Triangle(Figure):
    def __init__(self,figure,s_1,s_2,s_3,height):
        self.s_1 = s_1
        self.s_2 = s_2
        self.s_3 = s_3
        self.height = height
    
    def tr_per(self):
        return self.s_1 + self.s_2 + self.s_3

    def areaT(self):
        return self.height * self.s_1 * 0.5
    
    def angle(self):
        return math.degrees(self.s_2) # Это не точно


s = Triangle('treug',2,3,4,6)
print('ploshad:', s.areaT())
print(s.angle())












    




