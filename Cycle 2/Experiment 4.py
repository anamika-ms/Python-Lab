# Aim:
# Program to count the number of characters (character frequency) in a string.

# Pseudocode:
# 1. Read string.
# 2. Iterate through each character.
# 3. Print character counts.


n=int(input(“Enter the string:”).lower()
s={}
for i in n :
  if i in s :
    s[i]+=1
  else :
    s[i]=1
print(s)

# Output:
# Enter the string :hello
# {‘h’:1, ‘e’:1, ‘l’:2, ‘o’:1}
