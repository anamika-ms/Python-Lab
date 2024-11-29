# Aim: 
# Find biggest of 3 numbers entered.

# Pseudocode:
# 1. Read num1,num2,num3.
# 2. If num1>=num2 and num1>=num2, Print num1 is largest.
# 3. Else if num2>=num1 and num2>=num3, Print num2 is largest.
# 4. Else, Print num3 is largest.

num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
num3=int(input("Enter third number :"))
if num1>num2 & num1>num3:
  print(f"{num1} is biggest.")
elif num2>num3:
  print(f"{num2} is biggest.")
else:
  print(f"{num3} is biggest.")

# Output:
# Enter first number:15
# Enter second number:25
# Enter third number:35
# 35 is biggest number
