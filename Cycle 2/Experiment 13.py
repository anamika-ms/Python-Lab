# Aim: 
# Program to count the occurance of each word in a line of text.

# Pseudocode:
# 1. Read text.
# 2. Split the text and store it in a list.
# 3. Print the word occurance.

Source code:
text = input("Enter a line of text: ")
words = text.split()
word_count = {}
for word in words:
  word = word.lower()
  if word in word_count:
    word_count[word] += 1
  else:
    word_count[word] = 1
print("Word occurrences:", word_count)

# Output:
# Enter a line of text: the flower is a flower
# {'the': 1, 'flower': 2, 'is': 1, 'a': 1}
