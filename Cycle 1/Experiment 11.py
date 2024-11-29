# Aim: 
# Write a Python program to solve a quadratic equation.

# Pseudocode:
# 1. Read a,b,c .
# 2. Calculate the discriminant: d = b^2 - 4ac .
# 3. If the discriminant is negative, print There are no real solutions.
# 4. Otherwise, calculate the two real solutions
# a. sol1 = (-b + sqrt(d)) / 2a
# b. sol2 = (-b - sqrt(d)) / 2a
# 5. Print two solutions.

import math
a=float(input("Enter coefficient of a :"))
b=float(input("Enter coefficient of b :"))
c=float(input("Enter coefficient of c :"))
d=b**2-4*a*c
if d>0:
  root1=(-b+math.sqrt(d))/(2*a)
  root2=(-b-math.sqrt(d))/2*a
  print(f"The roots are real and different : {root1},{root2}")
elif d==0:
  root=-b/(2*a)
  print(f"The roots are real and same :{root}")
else:
  real=-b/(2*a)
  imaginary=(math.sqrt(-d))/(2*a)
  print(f"Equation has Two complex roots {real}+{imaginary}i and {real}-{imaginary}i")

# Output:
# Enter coefficient of a 1
# Enter coefficient of b -5
# Enter coefficient of c -14
# The roots are real and different:7.0,-2.0
