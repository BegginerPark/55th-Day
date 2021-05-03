import datetime

dt = datetime.datetime(2018,12,1)
now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)

print(now)
print(now == dt)
print(mid)