def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def permutations(n, r):
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

n = int(input("Enter n: "))
r = int(input("Enter r: "))

print(f"Permutations p({n},{r}) = {permutations(n, r)}")
print(f"Combinations c({n},{r}) = {combinations(n, r)}")
