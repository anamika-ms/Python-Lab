# Aim:
# Program to create a single string separated with space from two strings by swapping the character at position 1.

# Pseudocode:
# 1. Read string1,string2.
# 2. Set string3 by slicing and concatenating string1 and string2.
# 3. Print string3.

string1=input("Enter your string:")
string2=input("Enter your string:")
swap_str1=string1[0]+string2[1]+string1[2:]
swap_str2=string2[0]+string1[1]+string2[2:]
string3=swap_str1+" "+swap_str2
print(string3)

# Output:
# Enter 1st string :hello
# Enter 2st string :world
# hollo world
