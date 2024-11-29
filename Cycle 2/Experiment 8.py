# Aim: 
# Program to create a list of colors from comma-separated color names entered by the user.Display first and last colors.

# Pseudocode:
# 1. Read colors .
# 2. Print first and last color using index.

colors=input("Enter colors (comma-separated)").split(',')
print("first color:",colors[0])
print("last color:",colors[-1])

# Output:
# Enter colors (comma-separated):red,yellow,green
# first color:red
# last color:green

