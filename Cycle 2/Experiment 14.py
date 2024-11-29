# Aim: 
# List comprehensions:
# (a) Generate positive list of numbers from a given list of integers
# (b) Square of N numbers
# (c) Form a list of vowels selected from a given word
# (d) Form a list ordinal value of each element of a word

# Pseudocode:
# 1. Read numbers.
# 2. Print positive numbers.
# 3. Print squares of first n numbers.
# 4. Print vowels from a word.

numbers = [-10, 15, -3, 7, -25, 18, 0]
positive_numbers = [num for num in numbers if num > 0]
print(f"Positive numbers in {numbers} :", positive_numbers)
N = 5
squares = [num ** 2 for num in range(1, N + 1)]
print("Squares of first 5 numbers:", squares)
word = "comprehension"
vowels = [char for char in word if char in 'aeiou']
print(f"Vowels in the word: {word}", vowels)
word = "hello"
ordinal_values = [ord(char) for char in word]
print("Ordinal values of each character in the word : hello", ordinal_values)

# Output:
# Positive numbers in [-10,15,-3,7,-25,18,0] : [15,7,18]
# Squares of first 5 numbers : [1,4,9,16,25]
# Vowels in the word : comprehension [‘o’, ‘e’, ‘e’, ‘i’, ‘o’]
# Ordinal values of each characterin the word : hello [104,101,108,108,111]
