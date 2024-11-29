# Aim: 
# Program to prompt the user to enter two lists of integers and check
# (a) whether lists are of the same length.
# (b) whether the list sums to the same value.
# (c) whether any value occurs in both lists.

# Pseudocode:
# 1. Read list1,list2.
# 2. If the lengths are equal , Print same length.
# 3. If the sum of elements in both lists are equal , Print equal sum.
# 4. Find the common value using intersection .
# 5. Print common value.

n=int(input("Enter number of integers to input:"))
list1=[]
for i in range(n):
  num=int(input("Enter integers:"))
  list1.append(num)
n=int(input("Enter number of integers to input:"))
list2=[]
for i in range(n):
  num=int(input("Enter integers:"))
  list2.append(num)
if len(list1)==len(list2):
  print("lists are of the same length.")
else:
  print("The lists are of different lengths.")
if sum(list1)==sum(list2):
  print("The lists sum to the same value.")
else:
  print("The lists do not sum to the same value.")
common_value=set(list1).intersection(list2)
if common_value:
  print(f"Common values in both lists:{common_value}")
else:
  print("There are no common values in both lists.")

# Output:
# Enter number of integers to input : 5
# Enter integers : 1
# Enter integers : 2
# Enter integers : 3
# Enter integers : 4
# Enter integers : 5
# Enter number of integers to input : 5
# Enter integers : 2
# Enter integers : 4
# Enter integers : 8
# Enter integers : 7
# Enter integers : 6
# The lists are of same lengths.
# The lists do not sum to the same value.
# Common values in both lists:{2,4}
