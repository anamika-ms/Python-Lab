""" 
Aim: Create a string from the given string where the first and last character are
exchanged.

Pseudocode:
1. Read str.
2. newstr=str[-1]+str[1:-1]+str[0].
3. Print newstr.
"""

str="python"
newstr=str[-1]+str[1:-1]+str[0]
print(newstr)

"""
Output:
nythop
"""
