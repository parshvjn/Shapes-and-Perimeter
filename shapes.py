class Shapes:
    def circleArea(self, r): # member function
        self.r = r # local variable to circleArea
        self.area = str((22/7)*(r**2))
        return f'{self.area} cm'
    def squareArea(self, l):
        self.l = l
        self.area = l**2
        return f'{self.area} cm'
    def rectArea(self, l, w):
        self.l = l
        self.w = w
        self.area = l*w
        return f'{self.area} cm'
    def triArea(self, b, h):
        self.b = b
        self.h = h
        self.area = (b*h)/2
        return f'{self.area} cm'
    def rhombusArea(self, d1, d2):
        self.d1 = d1
        self.d2 = d2
        self.area = (d1*d2)/2
        return f'{self.area} cm'
    def parallelogramArea(self, b, h):
        self.b = b
        self.h = h
        self.area = b*h
        return f'{self.area} cm'

# HW: peri for all shapes
class ShapesPerimeter:
    def circlePeri(self, r):
        self.r = r
        self.peri = 2*(22/7)*r
        return f'{self.peri} cm'
    def squarePeri(self, l):
        self.l = l
        self.peri = 4*l
        return f'{self.peri} cm'
    def rectPeri(self, l, w):
        self.l = l
        self.w = w
        self.peri = (2*l) + (2*w)
        return f'{self.peri} cm'
    def triPeri(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.peri = s1 + s2 + s3
        return f'{self.peri} cm'
    def rhombusPeri(self, p1, p2): #p1 and p2 are pairs or parrallel sides
        self.p1 = p1
        self.p2 = p2
        self.peri = (2*p1) + (2*p2)
        return f'{self.peri} cm'
    def parallelogramPeri(self, p1, p2): #p1 and p2 are pairs or parrallel sides
        self.p1 = p1
        self.p2 = p2
        self.peri = (2*p1) + (2*p2)
        return f'{self.peri} cm'