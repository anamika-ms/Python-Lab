n=int(input("Enter number of terms :"))
sum=0
num=[]
for i in range(n):
	n1=int(input("enter numbers:"))
	num.append(n1)
for i in num:
	sum+=i
print(num)
print("sum of the list :",sum)
