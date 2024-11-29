# Aim: 
# Write a Python program to get a string which is n (non-negative integer) copies
# of a given string.

# Pseudocode:
# 1. Read string.
# 2. Read number of repetition , n.
# 3. Print string*n.

string=input("Enter a string:")
n=int(input("Enter a non negative integer:"))
result= string*n
print(f"The result : {result}")

# Output:
# Enter a string: anu
# Enter a non-negative integer:4
# Result: anuanuanuanu
