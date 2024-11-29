# Aim: 
# Accept an integer n and compute n+nn+nnn.

# Pseudocode:
# 1. Read n.
# 2. Calculate result= n+(n*10+n)+(n*100+n*10+n).
# 3. Print result.

n=int(input("Enter a integer :"))
result=n+(n*10+n)+(n*100+n*10+n)
print(f"Result :{n}+{n}{n}+{n}{n}{n}={result}")

# Output:
# Enter your n: 4
# Result:4+44+444=492
