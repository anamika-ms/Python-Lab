def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def sum_series(n):
    total = 0
    for i in range(1, n + 1):
        total += (i**3) / factorial(i)
    return total

n = int(input("Enter number of terms: "))
print(f"Sum of series: {sum_series(n)}")
