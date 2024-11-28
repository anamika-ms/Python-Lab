# Aim : Program to solve a quadratic equation

import math
a=float(input("Enter coefficient of a :"))
b=float(input("Enter coefficient of b :"))
c=float(input("Enter coefficient of c :"))
d=b**2-4*a*c
if d>0:
root1=(-b+math.sqrt(d))/(2*a)
root2=(-b-math.sqrt(d))/2*a
print(f"The roots are real and different : {root1} {root2}")
elif d==0:
root=-b/(2*a)
print(f"The roots are real and same :{root}")
else:
real=-b/(2*a)
imaginary=(math.sqrt(-d))/(2*a)
print(f"Equation has Two complex roots {real}+{imaginary}i and {real}-{imaginary}i")
