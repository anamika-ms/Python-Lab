# Aim: 
# Program to sort dictionaries in ascending and discending order.

# Pseudocode:
# 1. Read my_dict.
# 2. Print sorted keys in ascending and descending order.
# 3. Print sorted values in ascending and descending order.

my_dict = {'banana': 3, 'apple': 5, 'orange': 2, 'kiwi': 4}
keys_asc = dict(sorted(my_dict.items()))
print("Sorted by keys (ascending):", keys_asc)
keys_desc = dict(sorted(my_dict.items(), reverse=True))
print("Sorted by keys (descending):", keys_desc)
values_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted by values (ascending):", values_asc)
values_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Sorted by values (descending):", values_desc)

# Output:
# Sorted by keys(ascending) : {‘apple’:5, ‘banana’:3, ‘kiwi’:4}
# Sorted by keys(descending) : {‘kiwi’:4, ‘banana’:3, ‘apple’:5}
# Sorted by values(ascending) : {‘banana’:3, ‘kiwi’:4, ‘apple’:5}
# Sorted by values(descending) : {‘apple’:5, ‘kiwi’:4, ‘banana’:3}
