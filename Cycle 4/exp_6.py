user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
multiples_of_3 = list(map(lambda x: 3 * x, numbers))
print(f"Multiples of 3 for the given numbers: {multiples_of_3}")

