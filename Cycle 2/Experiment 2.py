""" 
Aim:
Program to get a string from an input string where all occurences of first
character are replaced with ‘$’,except for first character.

Pseudocode:
1. Read string.
2. first_char=s[0].
3. newstr=first_char +s[1:].replace(f, ‘$’).
4. Print newstr. 
"""

s=input("Entre a string :")
first_char=s[0]
newstr= first_char +s[1:].replace(f, ‘$’)
print(“{newstr}”)

"""
Output:
Enter a string: onion
Output: oni$n
"""
