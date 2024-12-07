from datetime import datetime,date
import calendar
current_time=datetime.now()
today=datetime.now()
print(f"Current date and time : ",datetime.now())
print(f"Current year : ",current_time.strftime("%Y"))
yr=date.today()
print(f"Month of the Year :")
print(calendar.month(yr.year,yr.month))
print(f"Week Number of the year :",current_time.strftime("%W"))
print(f"Weekdays of Week :",current_time.strftime("%A"))
print(f"Day of Year :",current_time.strftime("%j"))
print(f"Day of Month :",current_time.strftime("%d"))
print(f"Day of week :",current_time.strftime("%w"))
