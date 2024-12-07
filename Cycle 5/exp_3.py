import calendar
from datetime import date,timedelta
today=date.today()
yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)
print("Yesterday = ",yesterday.strftime('%Y-%m-%d'),calendar.day_name[yesterday.weekday()])
print("Today = ",today.strftime('%Y-%m-%d'),calendar.day_name[today.weekday()])
print("Tomorrow = ",tomorrow.strftime('%Y-%m-%d'),calendar.day_name[tomorrow.weekday()])
