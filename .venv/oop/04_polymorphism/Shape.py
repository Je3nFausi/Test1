#polymorphism-to have many forms or faces
#an object can take many forms
#Two ways to achieve polymorphism
#1.Inheritance=An object could be treated of the same type as a parent class
#2."Duck Typing"=Object must have necessary attributes/Methods
from abc import ABC, abstractclassmethod
class Shape:
    def area(self):
       pass
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    

class Square(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def are(self):
        return self.base*self.height*0.5

shapes=[Circle(4),Square(5),Triangle(6,7)]
for shape in shapes:
           print(f"{shape.area()}")