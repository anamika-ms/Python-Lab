def add(*args):
    """Function to add variable length arguments"""
    return sum(args)
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
print("Sum of numbers:", add(*numbers))
