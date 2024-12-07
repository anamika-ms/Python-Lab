def add(a,b):
	return a+b
def subtract(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	return a/b
def calculator():
	while True:
		print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
		choice=int(input("Enter your choice : "))
		a=float(input("Enter first number : "))
		b=float(input("Enter second number : "))
		if choice ==1:
			print("Result : ",add(a,b))
		elif choice==2:
			print("Result : ",subtract(a,b))
		elif choice==3:
			print("Result : ",multiply(a,b))
		elif choice==4:
			print("Result : ",divide(a,b))
		elif choice==5:
			break
		else :
			print("Invalid choice!")
calculator()
