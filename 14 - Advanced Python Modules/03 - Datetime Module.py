import datetime

mytime = datetime.time(2,20)
print(mytime)
print(mytime.minute)

print()

today = datetime.date.today()
print(today)

print()

from datetime import datetime
mydatetime = datetime(2022, 12, 2, 14, 23, 44)
print(mydatetime)
print(mydatetime.replace(year=1990))
