#Write the definition of a Point class. Objects from this class should have a
# 1)a method show to display the coordinates of the point
# 2)a method move to change these coordinates
# 3)a method dist that computes the distance between 2 points

import math
class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    #show
    def first(self):
        print(f"Coordinates placed at: ({self.x}, {self.y})")
    
    #move
    def second(self, x1, y1):
        self.x = x1
        self.y = y1
        
    #the distance
    def third(self, others):
        return math.sqrt((self.x - others.x)**2 +(self.y - others.y)**2)
    
x1 = int(input("Enter x: "))
y1 = int(input("Enter y: "))
point = Points(x1, y1)
    
x2 = int(input("Enter x1: "))
y2 = int(input("Enter y1: "))
point1 = Points(x2, y2)
    
point.first()
point1.first()
    
the_distance = point.third(point1)
print(f"Distance: {the_distance}")
