# Aim: 
# Program to merge two dictionaries.

# Pseudocode:
# 1. Read dict1,dict2.
# 2. Merge dict1 and dict2.
# 3. Print merged dictionary.

dict1={'banana':3,'apple':5}
dict2={'orange':2,'kiwi':4}
print(dict1)
print(dict2)
dict1.update(dict2)
print(f"Merged:{dict1}")

# Output:
# {‘banana’:3, ‘apple’:5}
# {‘orange’:2, ‘kiwi’:4}
# Merged : {‘banana’:3, ‘apple’:5 ‘orange’:2, ‘kiwi’:4}
