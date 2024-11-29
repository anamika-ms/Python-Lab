# Aim: 
# Write a program to calculate the salary of an employee given his basic pay (to be entered by the user). HRA = 10 percent of the basic pay, TA = 5 percent of the basic pay.

# Pseudocode:
# 1. Read basic_pay.
# 2. HRA=(10/100)* basic_pay.
# 3. TA=(5/100)* basic_pay.
# 4. Total_salary = basic_pay +HRA +TA.
# 5. Print Total_salary.

basic_pay=float(input("Enter the basic pay :"))
hra=0.10*basic_pay
ta=0.05*basic_pay
total_salary=basic_pay+hra+ta
print(f"HRA={hra}\nTA={ta}\nThe total salary is : {total_salary}")

# Output:
# Enter your basic pay 10000
# Total salary of employee:11500.0
