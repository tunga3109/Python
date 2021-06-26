import math

class Figure:

    def __init__(self,figure):
        self.figure = figure


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
        return math.degrees(self.s_2)


class Right_triangle(Triangle):

    def __init__(self,length,height,angle):
        self.length = length
        self.height = height
        self.angle = angle
    