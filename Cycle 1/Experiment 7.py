# Aim : Program to accept an integer and compute n+nn+nnn

n=int(input("Enter a integer :"))
result=n+(n*10+n)+(n*100+n*10+n)
print(f"Result :{n}+{n}{n}+{n}{n}{n}={result}")
