n=int(input("Enter a number:"))
num = n
result = 0
while n > 0:
	digit = n % 10
	result += digit ** 3
	n //= 10
if result == num:
	print(num,"is an armstrong number.")
else:
	print(num,"is not an armstrong number.")
