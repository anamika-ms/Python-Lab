user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
powers_of_2 = list(map(lambda x: 2 ** x, numbers))
print(f"Powers of 2 for the given numbers: {powers_of_2}")
