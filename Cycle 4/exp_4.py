square=lambda side:side*side
rectangle=lambda length,breadth:length*breadth
triangle=lambda base,height:0.5*base*height
side=float(input("Enter side of square:"))
print("Area of square :",square(side))
length=float(input("Enter length:"))
breadth=float(input("Enter breadth:"))
print("Area of rectangle:",rectangle(length,breadth))
base=float(input("Enter base:"))
height=float(input("Enter height"))
print("Area of triangle:",triangle(base,height))
