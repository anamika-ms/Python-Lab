# Aim: 
# Program to read two lists, print out all colors from color_list 1 not contained in color_list2.

# Pseudocode:
# 1. Read list1,list2.
# 2. Create sets with list1 and list2.
# 3. Find the diffrence.
# 4. Print diffrence.

list1=input("Enter colors for list 1 seprated by comma:")
list2=input("Enter colors for list2 seprated by comma:")
set1=set(list1.split(','))
set2=set(list2.split(','))
difference=set1-set2
print("Colors in list1 but not in list2:",difference)

# Output:
# Enter colors for list 1 seprated by comma:red,green
# Enter colors for list 2 seprated by comma:green,yellow
# colors in list 1 but not in list 2: {‘red’}
