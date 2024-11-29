# Aim: 
# Program to check whether a year is leap year or not.

# Pseudocode:
# 1. Read year.
# 2. If the year is divisible by 4 and not divisible by 100, Print The year is a leap year .
# 3. Else if the year is divisible by 400, Print The year is a leap year .
# 4. Else, Print The year is not a leap year.

year=int(input("Enter the year :"))
if(year%400==0) or (year%100!=0 and year%4==0):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")

# Output:
# Enter the year: 2004
# 2004 is a leap year
# Enter the year: 2023
# 2023 is not a leap year
