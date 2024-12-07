n=int(input("Enter a number:"))
print("Factors :")
i=1
while i <= n:
	if n % i == 0:
		print(i,end=" ")
	i += 1
