# Aim : Program to determine the rate of entry ticket in a trade fair based on age.

age=int(input("Enter your age :"))
if age<10:
rate=7
elif age>=10 and age<60:
rate=10
else:
rate=5
print(f"The rate of entry ticket is {rate}.")
