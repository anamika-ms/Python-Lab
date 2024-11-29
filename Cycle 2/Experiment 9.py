# Aim: 
# Program to prompt the user for a list of integers ,for all values greater than 100 store ‘over’ instead.

# Pseudocode:
# 1. Read num.
# 2. If num >100 , Set num=over.
# 3. Add num to list.
# 4. Print list.

n=int(input("Enter number of integers to input:"))
list1=[]
for i in range(n):
  num=int(input("Enter integer:"))
  if num>100:
    num="over"
  list1.append(num)
print(list1)

# Output:
# Enter number of integers to input : 3
# Enter integers:46
# Enter integers:2446
# Enter integers:0
# [46, ‘over’,0]
