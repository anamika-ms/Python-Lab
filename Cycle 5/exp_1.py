import calendar
year=int(input("Enter the Year:"))
if(calendar.isleap(year)):
	print(f"{year} is leap year")
else:
	print(f"{year} is not leap year")
