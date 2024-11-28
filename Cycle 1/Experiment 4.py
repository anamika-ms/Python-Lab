# Aim : Program to calculate the salary of an employee

basic_pay=float(input("Enter the basic pay :"))
hra=0.10*basic_pay
ta=0.05*basic_pay
total_salary=basic_pay+hra+ta
print(f"HRA={hra}\nTA={ta}\nThe total salary is : {total_salary}")
