#write a python program to calculute the area of regular polygon
import math
def area(sides, length):
    area = (sides * length ** 2) / (4 * math.tan(math.pi / sides))
    return area

sides = int(input("Input number of sides: "))
length = int(input("Input the length of a side: "))
area = area(sides, length)
print("The area of the polygon is: ", area)