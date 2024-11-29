# Aim: 
# Program to accept a list of words and return the length of longest word.

# Pseudocode:
# 1. Read str.
# 2. Split str into list of words.
# 3. Print longest word and its length.

str=input("Enter the list of words separated by space:")
words=str.split()
length=0
for i in words:
  if len(i)>length:
    longestword=i
    length=len(i)
print(f"The longest word is {longestword} and its length is {length}")

# Output:
# Enter the list of words seprated by space: malayalam english hindi
# The longest word is malayalam and its length is 9
