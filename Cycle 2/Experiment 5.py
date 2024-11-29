# Aim:
# Program to add ‘ing’ at the end of a given string. If it already ends with ‘ing’,then add ‘ly’.

# Pseudocode:
# 1. Read string.
# 2. If there is ‘ing’ in the string add ‘ly’.
# 3. Else add ‘ing’.

str1=input("Enter a string")
if "ing" in str1:
  print(str1+"ly")
else:
  print(str1+"ing")

# Output:
# Enter a string: play
# playing
# Enter a string: loving
# lovingly
