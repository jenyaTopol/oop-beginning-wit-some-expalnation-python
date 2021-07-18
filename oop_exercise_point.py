#exercize with some build in oop functions

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance_from_00(self):
        # sqrt(x**2 + y**2)
        dist = math.sqrt(self.x**2 + self.y**2)
        return dist
    def __str__(self):
        dist = self.distance_from_00()
        return f'Point ({self.x},{self.y}) dist from reshit tzirim: {dist}'
    def __repr__(self):
        # similar to __str__
        # option 1 -- like __Str__
        #dist = self.distance_from_00()
        #return f'Point ({self.x},{self.y}) dist from reshit tzirim: {dist}'
        # option 2 -- python command to create similar object
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        # print (p1 == p3)
        print('----------- inside function __eq__')
        print(f'self is {self}')
        print(f'other is {other}')
        print('trying to compare between them ... if they are equal return true , otherwise false')
        # Compare!
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __gt__(self, other):
        # print (p1 > p2)
        print('----------- inside function __gt__')
        print(f'self is {self}')
        print(f'other is {other}')
        print('trying to decide who is bigger? self or other ... if self return true else- false')
        # Compare!
        if self.distance_from_00() > other.distance_from_00():
            return True
        else:
            return False

p1 = Point(3.1, 7.89)
p2 = Point(-4.5, -5.19)

print('p1= ',p1)
print('p2= ',p2)
print('p1 dist from reshit tzirim:',p1.distance_from_00())

print('p1 repr creation syntax',p1.__repr__())
print('p2 repr creation syntax',p2.__repr__())

print('===========================================================')
p3 = Point(3.1, 7.89)
print('p1=',p1)
print('p3=',p3)
print('p1==p3?',p1 == p3)
print('===========================================================')
print('p1==p2?',p1 == p2)

#def compare_points(point1, point2):
#    if point1.x == point2.x and point1.y == point2.y:
#        return True
#    else:
#        return False
#print(compare_points(p1, p3))
x = 1
y = 2
print(x>y)
print(p1 > p2)
print(p1 > p3)
