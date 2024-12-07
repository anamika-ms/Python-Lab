n=int(input("Enter the value :"))
primes = []
for num in range(2,n+1):
	is_prime = True
	for i in range(2,int(num ** 0.5)+1):
		if num % i == 0:
			is_prime = False
			break
	if is_prime :
		primes.append(num)
for i in range(0,len(primes),2):
	print(primes[i],end=" ")
	print( )

