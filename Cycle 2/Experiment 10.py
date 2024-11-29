# Aim: 
# Program to form a list of integers ,create a list after removing even numbers.

# Pseudocode:
# 1. Read num.
# 2. If num%2!=0, Add num to list.
# 3. Print list.

n=int(input("Enter number of intgers to input:"))
listed=[]
for i in range(n):
  num=int(input("Enter Integers:"))
  if num%2!=0:
    listed.append(num)
print(f"New list:{listed}")

# Output:
# Enter number of integers to input : 5
# Enter integers : 1
# Enter integers : 2
# Enter integers : 3
# Enter integers : 4
# Enter integers : 5
# New List : [1,3,5]
