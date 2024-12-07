import graphics
import graphics.rectangle
import graphics.circle
from graphics.three_d_graphics.cuboid import cuboid_area,cuboid_volume
from graphics.three_d_graphics.sphere import *
length=float(input("Enter Length of Rectangle:"))
width=float(input("Enter Width of Rectangle:"))
print("Rectangle Area :",graphics.rectangle.area(length,width))
print("Rectangle Perimeter :",graphics.rectangle.perimeter(length,width))
print()
radius=float(input("Enter Radius of Circle:"))
print("Circle Area :",graphics.circle.area(radius))
print("Circle Perimeter :",graphics.circle.perimeter(radius))
print()
length=float(input("Enter Length of Cuboid:"))
width=float(input("Enter Width of Cuboid:"))
height=float(input("Enter Height of Cuboid:"))
print("Cuboid Area :",cuboid_area(length,width,height))
print("Cuboid Volume :",cuboid_volume(length,width,height))
print()
radius=float(input("Enter Radius of Sphere:"))
print("Sphere Area :",area(radius))
print("Sphere Perimeter :",volume(radius))



