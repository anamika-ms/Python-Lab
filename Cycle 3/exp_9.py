n=int(input("Enter a number :"))
if str(n) == str(n)[::-1]:
	print(n,"is a palindrome.")
else:
	print(n,"is not a palindrome.")
