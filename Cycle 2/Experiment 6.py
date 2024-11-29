# Aim: 
# Program to store a list of first names then count the occurance of ‘a’ within the list .

# Pseudocode:
# 1. Read names.
# 2. Count occurance of ‘a’.
# 3. Print count.

Source code:
names=input("Enter first names separated by commas:")
count_a=names.lower().count('a')
print(f"The letter 'a' appears {count_a} times in the list of names")

# Output:
# Enter first names separated by commas:anu,anamika,anjali
# The letter ‘a’ appears 5 times in the list of names
