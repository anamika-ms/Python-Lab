# Aim: 
# Program to determine the rate of entry ticket in a trade fair based on age.

# Pseudocode:
# 1. Read age .
# 2. if age is less than 10 , Print Ticket rate 7 .
# 3. Else, if age is less than 60, Print Ticket rate 10.
# 4. Else , Print Ticket rate 5.

age=int(input("Enter your age :"))
if age<10:
  rate=7
elif age>=10 and age<60:
  rate=10
else:
  rate=5
print(f"The rate of entry ticket is {rate}.")

# Output:
# Enter your age :25
# The rate of entry ticket is 7
