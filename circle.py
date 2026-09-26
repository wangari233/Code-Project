from math import pi

class Circle:
    def __init__(Self,radius):
        Self.radius = radius
    def area(Self):
        return round(pi* (Self.radius ** 2), 2)
c1 = Circle (5)
print(c1.area())    
            