# Aim : Program to find biggest of 3 numbers

num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
num3=int(input("Enter third number :"))
if num1>num2 & num1>num3:
print(f"{num1} is biggest.")
elif num2>num3:
print(f"{num2} is biggest.")
else:
print(f"{num3} is biggest.")
