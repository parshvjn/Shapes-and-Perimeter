from shapes import Shapes, ShapesPerimeter
from config import *

geometry = Shapes()
print(geometry.circleArea(r))
print(geometry.parallelogramArea(r,l))
print(geometry.rectArea(l,r))
print(geometry.triArea(6000,3))
print(geometry.rhombusArea(7,6))
print(geometry.squareArea(6))
# print(shapes.__path__)
perimeter = ShapesPerimeter()
print(perimeter.circlePeri(r))
print(perimeter.parallelogramPeri(r,l))
print(perimeter.rectPeri(l,r))
print(perimeter.triPeri(6000,3,6))
print(perimeter.rhombusPeri(7,6))
print(perimeter.squarePeri(6))